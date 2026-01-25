# TSOC Echo Learning 網站擴展計畫

## 專案概述

將「Echo Book Reading 2025」資料夾中的21章心臟超音波教材轉換為互動式網頁學習系統。

## 現有資源

### 已完成頁面
- `tsoc-echo-learning-2025.html` - Hub 主頁面（含6個切面基礎教學 + 進階主題導航）
- `echo-basics.html` - 基礎原理（Ch 00-03）
- `echo-hemodynamics.html` - 舒張功能（Ch 04）
- `echo-cardiomyopathy.html` - 心肌病變（Ch 05-07）
- `echo-ischemic.html` - 缺血性心臟病（Ch 08）
- `echo-aortic-valve.html` - 主動脈瓣疾病（Ch 09-10）
- `echo-mitral-valve.html` - 二尖瓣疾病（Ch 11-12）
- `echo-right-heart.html` - 右心疾病（Ch 13, 16）
- `echo-prosthetics-endocarditis.html` - 人工瓣膜與心內膜炎（Ch 14-15）
- `echo-aorta-pericardium.html` - 主動脈與心包膜（Ch 17-18）
- `echo-masses-chd.html` - 腫塊與先天性心臟病（Ch 19-20）

### PDF 教材對照表

| 章節 | 主題 | 講義檔案 | 網頁狀態 |
|------|------|----------|----------|
| 00 | FOCUS | Chapter 00 FOCUS.pdf | ✅ echo-basics.html |
| 01 | 超音波原理 | Chapter 01 - Principles 講義.pdf | ✅ echo-basics.html |
| 02 | 影像擷取 | Chapter 02 - How to Image 講義.pdf | ✅ echo-basics.html |
| 03 | 心腔與壁 | Chapter 03 - Heart Chambers 講義.pdf | ✅ echo-basics.html |
| 04 | 舒張功能 | Chapter 04 - Diastolic 講義.pdf | ✅ echo-hemodynamics.html |
| 05 | 擴張型心肌病 | Chapter 05 - DCM 講義.pdf | ✅ echo-cardiomyopathy.html |
| 06 | 肥厚型心肌病 | Chapter 06 - HCM 講義.pdf | ✅ echo-cardiomyopathy.html |
| 07 | 限制型心肌病 | Chapter 07 - Restrictive 講義.pdf | ✅ echo-cardiomyopathy.html |
| 08 | 冠狀動脈疾病 | Chapter 08 - CAD 講義.pdf | ✅ echo-ischemic.html |
| 09 | 主動脈瓣狹窄 | Chapter 09 - AS 講義.pdf | ✅ echo-aortic-valve.html |
| 10 | 主動脈瓣逆流 | Chapter 10 - AR 講義.pdf | ✅ echo-aortic-valve.html |
| 11 | 二尖瓣狹窄 | Chapter 11 - MS 講義.pdf | ✅ echo-mitral-valve.html |
| 12 | 二尖瓣逆流 | Chapter 12 - MR 講義.pdf | ✅ echo-mitral-valve.html |
| 13 | 三尖瓣疾病 | Chapter 13 - Tricuspid 講義.pdf | ✅ echo-right-heart.html |
| 14 | 人工瓣膜 | Chapter 14 - Prosthetic 講義.pdf | ✅ echo-prosthetics-endocarditis.html |
| 15 | 心內膜炎 | Chapter 15 - Endocarditis 講義.pdf | ✅ echo-prosthetics-endocarditis.html |
| 16 | 右心疾病 | Chapter 16 - Right Heart 講義.pdf | ✅ echo-right-heart.html |
| 17 | 主動脈疾病 | Chapter 17 - Aortic Disease 講義.pdf | ✅ echo-aorta-pericardium.html |
| 18 | 心包膜疾病 | Chapter 18 - Pericardial 講義.pdf | ✅ echo-aorta-pericardium.html |
| 19 | 腫瘤與腫塊 | Chapter 19 - Tumors 講義.pdf | ✅ echo-masses-chd.html |
| 20 | 先天性心臟病 | Chapter 20 - CHD 講義.pdf | ✅ echo-masses-chd.html |

---

## 網站架構

### 主入口
`tsoc-echo-learning-2025.html` → Hub 頁面，導向各子頁面

### 子頁面規劃

```
echo-basics.html          ← 章節 00-03 (基礎) ✅
echo-hemodynamics.html    ← 章節 04 (舒張功能) ✅
echo-cardiomyopathy.html  ← 章節 05-07 (心肌病) ✅
echo-ischemic.html        ← 章節 08 (缺血性) ✅
echo-aortic-valve.html    ← 章節 09-10 (主動脈瓣) ✅
echo-mitral-valve.html    ← 章節 11-12 (二尖瓣) ✅
echo-right-heart.html     ← 章節 13, 16 (右心) ✅
echo-prosthetics-endocarditis.html ← 章節 14-15 (人工瓣、心內膜炎) ✅
echo-aorta-pericardium.html ← 章節 17-18 (主動脈、心包) ✅
echo-masses-chd.html      ← 章節 19-20 (腫塊、先天性) ✅
```

---

## 實作進度

### Phase 1: 架構設定 ✅
- [x] 建立共用導航元件
- [x] 設定統一樣式
- [x] 主頁面加入子頁面導航

### Phase 2: 基礎章節 ✅
- [x] echo-basics.html (Ch 00-03)

### Phase 3: 血流動力學 ✅
- [x] echo-hemodynamics.html (Ch 04)

### Phase 4: 心肌病變 ✅
- [x] echo-cardiomyopathy.html (Ch 05-07)

### Phase 5: 缺血性心臟病 ✅
- [x] echo-ischemic.html (Ch 08)

### Phase 6: 主動脈瓣 ✅
- [x] echo-aortic-valve.html (Ch 09-10)

### Phase 7: 二尖瓣 ✅
- [x] echo-mitral-valve.html (Ch 11-12)

### Phase 8: 右心系統 ✅
- [x] echo-right-heart.html (Ch 13, 16)

### Phase 9: 人工瓣 & 感染 ✅
- [x] echo-prosthetics-endocarditis.html (Ch 14-15)

### Phase 10: 主動脈 & 心包 ✅
- [x] echo-aorta-pericardium.html (Ch 17-18)

### Phase 11: 腫塊 & 先天性 ✅
- [x] echo-masses-chd.html (Ch 19-20)

### Phase 12: 整合 ⬜
- [ ] 全站導航測試
- [ ] 進度追蹤功能（跨頁面）
- [ ] 行動裝置測試

---

## 每頁內容格式

1. **學習目標** - 本節重點
2. **關鍵概念** - 核心知識
3. **測量表格** - 正常值與分級
4. **臨床要點** - 掃描技巧
5. **注意事項** - 常見錯誤
6. **測驗題目** - 3-5題
7. **縮寫對照** - 本章術語
8. **相關章節** - 延伸閱讀

---

## 技術規格

- 使用 React + Tailwind CSS
- 保持現有設計風格
- 支援深色模式
- 行動裝置優先

---

## 進度符號說明

- ⬜ 待開始
- 🔄 進行中
- ✅ 已完成

---

*最後更新: 2026-01-25*
