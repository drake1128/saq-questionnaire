# 2026 頸動脈支架訓練課程教學模組 — 設計規格

**日期**：2026-05-22
**Owner**：drake1128 (心血管介入學會 週邊血管介入委員會)
**主辦**：中華民國心臟學會 / TSCI
**部署目標**：TSCI 網站（兩階段部署，見 §6）

---

## 1. 背景與目標

### 1.1 背景

每年由心臟介入學會週邊委員會舉辦的「頸動脈支架訓練課程 (Carotid Artery Stenting Training Course)」。今年要為學員提供**手機可操作的數位教學模組**，做兩件事：

1. **上課中**：學員邊聽講邊看手機，補充投影片畫面 + 重點摘要
2. **課後**：以「查核表 (Checklist)」方式自我複習，追蹤完成度

### 1.2 目標

- 把 2022 與 2024 兩屆所有講師的投影片整合進一套 HTML 教學模組
- 模組需 mobile-first，掃 QR 即可使用
- 學員進度可持久化（localStorage），不需登入
- 最終由 TSCI 網站上架

### 1.3 非目標 (Out of Scope)

- 不做帳號系統 / 登入 / 後端
- 不做即時多人協作或留言功能
- 不做影片串流（純文字 + 投影片靜態圖）
- 本期不做英文版（醫學名詞保留英文，介面/解說中文）

---

## 2. 課程內容 — 整合後 9 章

整合 2022 與 2024 兩屆共 13 份講義，去重後合併為 9 章。每章標註所有歷年講者來源。

| # | 章節主題 | Speaker(s) | 整合情境 |
|---|---|---|---|
| 1 | Ultrasound Diagnosis of Carotid Artery Stenosis | 湯頌君 (2022) / 葉馨喬 (2024) | 同主題、不同講師 |
| 2 | CT / MR for ICAS | 李崇維 (2022) | 單講師 |
| 3 | Carotid Stenosis & Occlusion | 黃國川 (2022) | 單講師 |
| 4 | General Interventional Techniques of CAS | 蘇峻弘 (2022) | 單講師 |
| 5 | Embolic Protection Device (EPD) | 黃成偉 (2022, 2024) | 同講師、兩年份 |
| 6 | Stent Design & TTT Carotid Stent | 蔡翰林 (2022 TTT / 2024 Stent design) | 同講師、不同主題 |
| 7 | Carotid TSCI | 柯呈諭 (2022, 2024) | 同講師、兩年份 |
| 8 | Surgical Approaches for Carotid Artery Disease | 黃致遠 (2024) | 單講師 |
| 9 | Difficult CAS — Tips & Tricks | 方修御 (2024) | 單講師 |

**多講師合併規則：**

- **同主題、不同講師**（Ch1）：核心概念合併為一卡片並同時標註兩位講者來源；各自獨有的補充保留為獨立卡片。
- **同講師、不同年份**（Ch5、Ch7）：以較新年份（2024）為主軸；舊年份有但新年份沒有的補充加為額外卡片。
- **同講師、不同主題**（Ch6）：當成兩個 sub-section，section header 分隔。

---

## 3. 整體架構

### 3.1 形狀

**Hub + 9 個獨立 Chapter HTML**（已確認 Option B）

- 每章一個 `.html`，可獨立分享、獨立 QR、獨立給講師預覽
- Hub 是入口 + 進度總覽
- 跨章節進度透過共用 `localStorage` key 同步

### 3.2 檔案配置

放置於既有 repo：`saq-questionnaire-main/`

```
saq-questionnaire-main/
├── cas-2026-hub.html                      # Hub 主頁
├── cas-2026-01-ultrasound.html
├── cas-2026-02-ct-mr.html
├── cas-2026-03-occlusion.html
├── cas-2026-04-techniques.html
├── cas-2026-05-epd.html
├── cas-2026-06-stent-design.html
├── cas-2026-07-tsci.html
├── cas-2026-08-surgical.html
├── cas-2026-09-difficult.html
├── cas-2026-shared.js                     # 共用 progress/utility 邏輯
├── images-cas-2026/                       # 圖片資產
│   ├── 01-ultrasound/
│   │   ├── 2022-tang-sj-seq12.png
│   │   └── 2024-yeh-hc-seq08.png
│   ├── 02-ct-mr/
│   ├── ...
│   └── 09-difficult/
└── docs/cas-2026/                         # Sidecar 投影片總覽頁
    ├── 01-ultrasound-slides-overview.html
    └── ...
```

### 3.3 共用資源

沿用既有檔案，**不重做**：

- `design-system.css` — 配色、字級、按鈕、卡片基本樣式
- `achievements.js` — 進度與徽章邏輯
- `achievements-ui.css` — 徽章視覺
- `achievements-config.js` — 徽章條件設定

新增：

- `cas-2026-shared.js` — 跨 9 章進度同步、章節資料表、QR 產生器

### 3.4 命名 Convention

| 項目 | 規範 |
|---|---|
| Chapter HTML | `cas-2026-NN-<topic-slug>.html` |
| 圖片資料夾 | `images-cas-2026/NN-<topic-slug>/` |
| 圖片檔案 | `<year>-<speaker-slug>-seq<XX>.png` (e.g., `2022-huang-cw-seq03.png`) |
| Chapter ID | HTML 內以 `data-chapter="cas-NN"` 標記，achievements.js 用此辨識 |
| localStorage key | `cas-2026-progress`（單一根 key，下方依 chapter ID 分子節點） |

---

## 4. Chapter 頁面模板

9 章共用同一模板，只換內容、不換結構。

### 4.1 頁面結構順序

```
1. Sticky Header
   - 左上「← 回 Hub」
   - 章節標題
   - 進度條 (N / Total cards)
2. Speaker Attribution Block
   - 講師姓名、年份
3. Learning Objectives Block
   - 3-5 條學習目標（bullet list）
4. Card List (5-8 cards per chapter)
   - 每張卡片：標題、投影片圖、重點解說 (1-3 句)、可選 Tip box、來源標註、右上 checkbox
5. Quick Check (3 MCQs)
   - 即時回饋（答對綠勾、答錯解釋）
6. Chapter Navigation
   - 上一章 / 下一章按鈕
```

### 4.2 視覺主題

- **使用既有 `design-system.css` 預設**：淺色背景 + 心血管藍主色 `#1a365d`
- 比 `carotid-stenting-app.html` 深色更適合臨床長時間閱讀
- 字體：Noto Sans TC（既有 stack）

### 4.3 互動邏輯

| 行為 | 實作 |
|---|---|
| 卡片右上 checkbox 勾選 | 寫入 `localStorage["cas-2026-progress"]["cas-NN"]["card-X"] = true`，Header 進度條即時更新 |
| Quick Check 作答 | 點選即時顯示對錯 + 解釋；3 題答對 ≥ 2 觸發 `achievements.js` 解鎖「Ch-NN 完成」徽章 |
| 章節導覽 | Ch1 上一章 disabled；Ch9 下一章導向 Hub 的「課程完成」狀態 |
| 進度持久化 | 不登入；以瀏覽器 localStorage 為單一 source of truth |

### 4.4 手機優化

- 卡片單欄、寬 100%
- 圖片 `max-width: 100%`、`object-fit: contain`
- Checkbox 點擊區 ≥ 44 × 44 px
- Sticky header 高度 ≤ 80 px 不擋內容

### 4.5 著作權標註

每張圖片下方固定格式：

```
📌 來源：<講師姓名>醫師 <年份> / 中華民國心臟學會 CAS 訓練課程 / slide #<原 slide 編號>
```

Hub 頁與每章頁末固定聲明：

> 本教學資源圖片來源為各講師於歷年「頸動脈支架訓練課程」之授課投影片，僅供本課程學員學術教育使用。

---

## 5. 投影片圖片抽取 Pipeline

### 5.1 原始素材

**總計 13 份檔案**：2022 年 7 份、2024 年 6 份。

| 格式 | 數量 | 檔案 | 處理方式 |
|---|---|---|---|
| `.pptx` | 7 份 | 李崇維 2022、黃國川 2022、蘇峻弘 2022、黃成偉 2022、柯呈諭 2022、柯呈諭 2024、方修御 2024 | LibreOffice headless → PDF → pdftoppm 300 DPI |
| `.ppt` | 2 份 | 湯頌君 2022、葉馨喬 2024 | LibreOffice headless 升級為 pptx → 同上 |
| `.pptm` | 1 份 | 蔡翰林 2022 (TTT) | 忽略巨集當 pptx 處理 |
| `.pdf` | 3 份 | 黃致遠 2024、黃成偉 2024、蔡翰林 2024 (Stent design) | pdftoppm 直接切圖 |

### 5.2 三階段流程

**Step 1 — 自動批次轉檔（Claude 執行）**

- 將 9 份原始檔全部頁面轉為 300 DPI png
- 輸出到 `docs/cas-2026/<NN-topic>/<year>-<speaker-slug>/` 暫存
- 預估耗時：30 分鐘

**Step 2 — Sidecar Overview Review（User 執行）**

- 每章生成一個 `docs/cas-2026/NN-<topic>-slides-overview.html`
- 頁面顯示該章所有 slide 縮圖 + 勾選方塊
- User 在手機 / 桌面瀏覽器勾選「採用的 slide」
- 按「匯出選中清單」產出 JSON
- 預估耗時：30-45 分鐘（9 章累計）

Sidecar overview HTML 示意：

```
📚 Ch1 Ultrasound — Slides Overview
─────────────────────────────────────
2022 湯頌君醫師 (47 slides)
  [縮圖1] [縮圖2] [縮圖3] ...
   ☐      ☑      ☐
2024 葉馨喬醫師 (38 slides)
  [縮圖1] [縮圖2] [縮圖3] ...
   ☑      ☐      ☑
─────────────────────────────────────
[匯出選中清單 → JSON]
```

**Step 3 — 嵌入 Chapter HTML（Claude 執行）**

- 讀 Step 2 匯出的 JSON
- 將選中圖片從暫存搬到 `images-cas-2026/NN-<topic>/`
- 在 chapter HTML 對應 card 寫入 `<img>` 標籤 + 著作權標註
- 此步驟與 chapter HTML 撰寫同時進行

### 5.3 已知風險

- **物件疊加 / 動畫 slide**：若原 ppt 用多個物件分步出現（例如箭頭逐步顯示），單張靜態截圖無法呈現順序。處理方式：在 Step 1 完成後標記出這類 slide，與 User 決定是否拆解為多張或改文字描述。

---

## 6. Hub 頁與部署

### 6.1 Hub 頁 (`cas-2026-hub.html`)

**內容區塊：**

1. **Course Header** — 標題、主辦單位、年份
2. **Progress Overview** — 整體進度條、已完成/學習中/未開始章數
3. **Chapter Grid** — 9 章 cards，每張顯示章名、講師、cards 數、Quick Check 題數、該章進度 %
4. **Achievements Strip** — 已獲得徽章顯示
5. **Action Bar** — 分享 QR、匯出學習記錄
6. **Footer** — 著作權聲明

**功能：**

- 跨 9 章進度從 `localStorage` 讀取後即時呈現
- 點 chapter card 跳到該章 HTML
- 分享按鈕沿用 `carotid-stenting-app.html` 既有的 share-button 機制
- 匯出學習記錄：產出 JSON 檔（學員可附在 CME 申請）

### 6.2 部署策略 — 兩階段

**Stage 1：GitHub Pages（開發 + 試用）**

- 直接放入既有 `drake1128/saq-questionnaire` repo
- URL：`drake1128.github.io/saq-questionnaire/cas-2026-hub.html`
- 用途：講師預覽、課前測試、迭代修改
- 不開新 repo（與既有 SAQ 系列共用基礎建設）

**Stage 2：TSCI 上架**

TSCI 網站架構未知 → 規格暫列三種候選方案，由 User 與 TSCI 確認後選定：

| 方案 | 描述 | 適用情境 |
|---|---|---|
| A. TSCI 連結到 GitHub Pages | TSCI 課程頁加按鈕外連 github.io URL | TSCI 簡易、更新由作者主控 |
| B. TSCI 完整 host | 整包 html + images zip 給 TSCI 上傳 | URL 乾淨、看起來是官方資源 |
| C. iframe 嵌入 | TSCI 頁面 iframe 嵌入 github.io 內容 | URL 是 TSCI、內容由作者維護 |

**預設策略**：先完成 Stage 1，待課程確定後依 TSCI 偏好選定 Stage 2 方案。

### 6.3 QR Code 分發

- **整套課程 QR**：Hub 頁網址，印在議程封面、報到處
- **單章 QR**：各 chapter 網址，印在該章節投影片首頁與講師介紹旁
- QR 由 Hub 頁的 share-button 即時產生（沿用 `carotid-stenting-app.html` 既有實作）

---

## 7. 開發時程與順序

### 7.1 試做策略

**已確認 Option B — 9 章同時做**

- 不採 pilot-then-iterate；直接以模板批次完成全部
- 模板穩定性靠「先寫一支 reference chapter，邏輯驗證後複製套用」確保

### 7.2 建議工作順序

1. **Step A**：搭建模板基礎
   - 建立 `cas-2026-shared.js`、定義 localStorage schema
   - 建立 chapter HTML 模板（暫用假內容）
   - 確認 design-system.css 跨章節一致
2. **Step B**：跑 Pipeline Step 1
   - 9 份原始檔批次轉 png
   - 產出 9 個 sidecar overview 頁
3. **Step C**：User Review Slides
   - User 在 sidecar 勾選採用 slide → 匯出 JSON
4. **Step D**：填內容
   - 9 章 chapter HTML 並行撰寫
   - 圖片嵌入、卡片內容、Quick Check 題目
5. **Step E**：Hub 頁
   - 串接 9 章進度資料
   - QR 與分享功能
6. **Step F**：跨章節 QA
   - 手機實測（iOS Safari / Android Chrome）
   - 進度持久化驗證
7. **Step G**：部署 Stage 1
   - Push 到 saq-questionnaire repo、確認 GitHub Pages 可訪問

### 7.3 課程日期相依性

2026 年課程日期 User 尚未提供 → 規格不對日期做硬綁定。

待 User 確認後，於開發 plan 階段補上：
- 課程前 ≥ 2 週完成 Stage 1
- 課程前 ≥ 1 週完成 Stage 2 上架

---

## 8. 資料與隱私

- 不蒐集任何學員個資（無登入、無 cookie、無 analytics 預設）
- 學習進度僅存於該裝置 `localStorage`
- 匯出學習記錄為 JSON 檔，由學員自行下載保存
- 若日後需 CME 時數認證，再評估增加去識別化打卡機制（**本期不做**）

---

## 9. 已確認事項一覽

| 主題 | 決議 |
|---|---|
| 架構 | Hub + 9 chapter HTMLs（Option B） |
| 章節數 | 9 章（2022 + 2024 整合去重） |
| 講師標註 | 多講師併呈、年份+姓名 |
| Chapter 模板 | 混合卡片 + 卡片右上 checkbox + 章末 Mini-Quiz（Option C） |
| 圖片抽取 | Claude 批次自動 + sidecar review + 嵌入（Option A）|
| 時程策略 | 9 章同時做（Option B） |
| Theme | 沿用 design-system.css 淺色 + 心血管藍 |
| Repo | 沿用 drake1128/saq-questionnaire |
| 部署 | 兩階段（GitHub Pages → TSCI） |

---

## 10. 待 User 後續確認事項

1. 2026 年課程**實際日期**
2. 2026 年**講師名單**是否與 2022/2024 完全相同（如有新講師加入需追加章節或更換素材）
3. TSCI 網站**部署方案**（A/B/C 三選一）
4. Hub 是否需要「課程完成證書」生成（PDF / 截圖式）— 本規格暫**不**包含，待 User 決定是否追加

---

## 11. 下一步

完成本規格 User 審核後，invoke `writing-plans` skill 產出實作計畫，計畫將涵蓋 §7.2 列出的 Step A → G 每一步的具體任務與檢核點。
