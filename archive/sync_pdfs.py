import os
import json
import time # 用於加入時間戳記
from googleapiclient.discovery import build
from google.oauth2 import service_account

# --- 1. 從 GitHub 環境變數讀取安全資訊 ---
# 這些變數來自於您在 GitHub Secrets 設定的 GOOGLE_CREDENTIALS 和 PDF_FOLDER_ID
try:
    CREDENTIALS_JSON = os.environ.get('GOOGLE_CREDENTIALS') 
    FOLDER_ID = os.environ.get('PDF_FOLDER_ID')

    if not CREDENTIALS_JSON or not FOLDER_ID:
        raise ValueError("環境變數 (Secrets) 讀取失敗。請檢查 GOOGLE_CREDENTIALS 和 PDF_FOLDER_ID 是否已設定。")
    
except Exception as e:
    print(f"初始化錯誤: {e}")
    # 在 GitHub Actions 中，如果發生錯誤，腳本將終止並顯示失敗
    exit(1)


# --- 2. 認證 Google Drive API ---
try:
    # 將 JSON 字串解析為 Python 字典，用於認證
    info = json.loads(CREDENTIALS_JSON)
    # 使用服務帳戶資訊來建立憑證物件
    credentials = service_account.Credentials.from_service_account_info(
        info, 
        # 僅需要讀取 (唯讀) 權限
        scopes=['https://www.googleapis.com/auth/drive.readonly'] 
    )
    # 建立 Drive API 客戶端
    service = build('drive', 'v3', credentials=credentials)

except Exception as e:
    print(f"Google API 認證或服務建立失敗: {e}")
    exit(1)


# --- 3. 呼叫 API 獲取檔案列表 ---
try:
    # QL (Query Language) 查詢條件：
    # 1. 'FOLDER_ID' in parents : 檔案必須在指定的資料夾內
    # 2. mimeType='application/pdf' : 只找 PDF 檔案
    # 3. trashed=false : 排除已放入垃圾桶的檔案
    query = f"'{FOLDER_ID}' in parents and mimeType='application/pdf' and trashed=false"
    
    # fields 參數只要求 'id' (檔案 ID) 和 'name' (檔案名稱) 兩個欄位，以提高效率
    results = service.files().list(
        q=query, 
        fields="files(id, name)",
        orderBy="name" # 依檔案名稱排序
    ).execute()
    
    files = results.get('files', [])

except Exception as e:
    print(f"Google Drive API 呼叫失敗: {e}")
    exit(1)


# --- 4. 生成 HTML 內容 ---

# 取得當前時間，用於顯示網頁更新時間
update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

html_content = f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>學生自學資源 - 自動更新</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; border: 1px solid #ccc; padding: 10px; border-radius: 5px; }}
        a {{ text-decoration: none; color: #007bff; font-weight: bold; }}
        a:hover {{ text-decoration: underline; }}
        .update-time {{ margin-top: 30px; font-size: 0.9em; color: #666; }}
    </style>
</head>
<body>
    <h1>最新課程 PDF 檔案列表</h1>
    <ul>
"""

if not files:
    html_content += "<li>目前資料夾中沒有 PDF 檔案。</li>"
else:
    for file in files:
        # 使用 Google Drive 的直接檢視/下載連結格式 (效率較高)
        # 格式：https://drive.google.com/uc?id=FILE_ID&export=view
        # export=view 會在瀏覽器中開啟 PDF 預覽
        file_link = f"https://drive.google.com/uc?id={file['id']}&export=view" 
        
        html_content += f"""
        <li><a href="{file_link}" target="_blank">{file['name']}</a></li>"""

html_content += f"""
    </ul>
    <p class="update-time">資料更新時間： {update_time} (UTC)</p>
    <p>此列表由 GitHub Actions 自動同步 Google Drive 內容。</p>
</body>
</html>
"""

# --- 5. 寫入 index.html 檔案 ---
try:
    # 確保以 UTF-8 編碼寫入，避免中文亂碼
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("index.html 已成功更新！")

except Exception as e:
    print(f"寫入 index.html 失敗: {e}")
    exit(1)

# 腳本執行成功，退出代碼 0
exit(0)
