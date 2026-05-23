# CAS 2026 教學模組 — 實作歷程記錄

> **下次 Claude 進來請從這份文件接續。** Memory 內 [[cas-2026-course-project]] 指向這裡。

**Session 日期**: 2026-05-22 → 2026-05-23 (一次性連續 session)
**Owner**: drake1128 (TSCI 週邊血管介入委員會)
**狀態**: ✅ **Stage 1 部署完成** (GitHub Pages) | ⏳ 待臨床審查 + 真實手機 QA
**Repo**: `drake1128/saq-questionnaire` on `main` branch

---

## 🎯 專案目的

替 2026 年「頸動脈支架訓練課程」(中華民國心臟學會) 建立**手機可操作的數位教學模組**：

- 上課時學員邊聽邊看手機補充內容
- 課後用 checklist 模式自我複習
- 整合 2022 + 2024 兩屆共 13 份講師投影片成 9 章
- 最終目標：上架到 TSCI 網站

---

## 📦 交付物總覽

| 類別 | 內容 | 位置 |
|---|---|---|
| **Hub** | `cas-2026-hub.html` | repo root |
| **9 章 HTML** | `cas-2026-NN-<slug>.html` | repo root |
| **共用 JS** | `cas-2026-shared.js` (progress + metadata) | repo root |
| **圖片** | 91 張精選 PNG @ 100 DPI ≈ 43 MB (從 527 張抽出) | `images-cas-2026/NN-*/` |
| **Pipeline 工具** | extract / generate_sidecar / process_selections / run_pipeline | `tools/cas-2026-pipeline/` |
| **Sidecar 縮圖頁** | 9 個 user-review HTMLs (一次性工具) | `docs/cas-2026/*-slides-overview.html` |
| **用戶選圖 JSON** | 9 個 (備份) | `tools/cas-2026-pipeline/selections/` |
| **Spec** | 設計規格 | `docs/superpowers/specs/2026-05-22-cas-2026-training-module-design.md` |
| **Plan** | 12-task 實作計畫 | `docs/superpowers/plans/2026-05-22-cas-2026-training-module.md` |

**統計**：66 卡片 × 1-3 句解說 + 27 道 MCQ + 91 張投影片圖

---

## 🌐 部署資訊

**Stage 1 (已完成)**: GitHub Pages
- Hub: https://drake1128.github.io/saq-questionnaire/cas-2026-hub.html
- 各章 URL: `https://drake1128.github.io/saq-questionnaire/cas-2026-NN-<slug>.html`

**Stage 2 (未做)**: TSCI 網站上架
- 三選一方案待 user 與 TSCI 確認 (見 spec §6.2)
- A) TSCI 連結到 GitHub Pages / B) TSCI 完整 host / C) iframe 嵌入

---

## 🏗️ 架構決議速查

| 決議 | 選項 | 為什麼 |
|---|---|---|
| 形狀 | **Hub + 9 獨立 chapter HTMLs** | 模組化、可逐章 QR、講師獨立改 |
| 章節模板 | **混合卡片 + 卡片 checkbox + 章末 3-MCQ** | 上課/課後共用一套，UI 一致 |
| 圖片抽取 | **Claude 自動 + sidecar review + 嵌入** | 用 LibreOffice/PowerPoint COM + PyMuPDF |
| 時程 | **9 章同時做** (非 pilot iterate) | User 選定，drafted in parallel by 9 subagents |
| Theme | **沿用 design-system.css** (淺色 + #1a365d) | 與 saq-questionnaire-main 既有風格一致 |
| Repo | **沿用 drake1128/saq-questionnaire** | 共用 design-system / achievements 基建 |

**進度狀態 schema** (`cas-2026-shared.js`):
```js
localStorage['cas-2026-progress'] = {
  'cas-01': {
    cards: { 'card-1': true, 'card-2': false, ... },
    quiz: { '1': {value:'B', correct:true}, ... },
    totalCards: 8,  // written by chapter HTML on load
    completed: true // when ≥2 quiz answers correct
  },
  'cas-02': { ... },
  ...
}
```

---

## 📜 9 章對照表

| # | Slug | Title | Speaker(s) | Cards | 主要內容 |
|---|---|---|---|---|---|
| 1 | ultrasound | Ultrasound Diagnosis | 湯頌君 2022 + 葉馨喬 2024 | 8 | PSV/EDV、ICA/CCA ratio、plaque morphology |
| 2 | ct-mr | CT / MR for ICAS | 李崇維 2022 | 8 | CTA technique、perfusion、DSA gold standard、FMD |
| 3 | occlusion | Stenosis & Occlusion | 黃國川 2022 | 7 | Circle of Willis、watershed、EC-IC bypass、CEA |
| 4 | techniques | General CAS Techniques | 蘇峻弘 2022 | 7 | 入路、arch I/II/III、push-pull、post-dilation |
| 5 | epd | Embolic Protection Device | 黃成偉 2022, 2024 | 5 | Distal filter vs proximal、flow suspension |
| 6 | stent-design | Stent Design & TTT | 蔡翰林 2022 TTT / 2024 Stent | 7 | Closed/open cell、free cell area、conformability |
| 7 | tsci | Carotid TSCI | 柯呈諭 2022, 2024 | 8 | CAS vs CEA 指引、CREST、ESC 2024 update |
| 8 | surgical | Surgical Approaches | 黃致遠 2024 | 8 | CEA、shunt、patch、eCEA、案例排序 |
| 9 | difficult | Difficult CAS Tips & Tricks | 方修御 2024 | 8 | 迂曲弓、Bovine、radial 入路、anchoring |

---

## ⚠️ 待 User 處理的 Open Items

### A. **臨床內容審查** (必要，部署前最重要)

我 draft 的卡片內容根據投影片做了「最佳詮釋」。Subagent 已自報的疑慮：

| 章 | 疑慮 |
|---|---|
| Ch1 Card 7 | PSV 閾值 (125/230 cm/s) 引自投影片表格，與 SRU 2003 一致 — 可能要更新到 2021 ESC guideline 或院內標準 |
| Ch1 Card 8 | 術後 in-stent restenosis 閾值 (>300 cm/s, ratio >4.75) 引自 Nederkoorn 2009 — 確認是否有更新標準 |
| Ch3 Card 6,7 | Slide #38/#39 我用 "suspected Moyamoya" 字眼 — 請確認診斷 |
| Ch3 Card 3 | Slide #24 (NTUH MRA) 我沒看到明確標註 stenosis/occlusion 位置 — 請補充 |
| Ch4 | seq057 在指示但實際資料夾沒抽出 — 已用 seq058/059 取代 |
| Ch7 | 章節內容是 CAS vs CEA 指引 (因投影片就是這樣)，**非狹義 TCAR/ENROUTE 流程** — 章名 "TSCI" 是否要改成 "CAS Decision & Evidence"？ |

### B. **真實手機 QA** (部署完即可)

部署後手機開 https://drake1128.github.io/saq-questionnaire/cas-2026-hub.html，驗：
- [ ] Hub 進度條與 9 章卡片正常
- [ ] 章節卡片可點進去
- [ ] Card checkbox 可勾、進度同步、reload 仍記得
- [ ] Quiz 點答案有顏色回饋
- [ ] 全部 prev/next 串接正確
- [ ] 圖片在手機螢幕載入正常

### C. **Stage 2 部署到 TSCI** (待 user 與 TSCI 確認)

選 A / B / C 方案 — 見 spec §6.2。在 Stage 1 跑順之後再做。

### D. **未做的可選功能** (本期排除)

- 課程完成證書 (PDF / 截圖式)
- CME 時數認證打卡
- 跨裝置同步 (本版僅 localStorage)
- 課程英文版

---

## 🗓️ Git Commit 時間軸 (本 session)

從 `883ba89` (pre-session) 起：

| Phase | Commit | 摘要 |
|---|---|---|
| 規劃 | `b126a6a` | Spec + Plan 文件 |
| A1 | `54c6845` → `5128242` | cas-2026-shared.js + 修正 overallProgress |
| A2 | `0a0b470` → `5c11f4d` | Chapter 模板 + 安全性修補 |
| A3 | `ac53ce1` → `5941c1d` | Chapter IIFE + defensive guards |
| B4 | `d86f607` → `e402c40` | Pipeline scaffolding + Python 3.13 pin 放寬 |
| B5 | `7b0a266` → `61e68b1` | extract_slides.py + COM 錯誤處理 |
| B6 | `8576ea8` → `f00080c` | 批次跑 9 章抽圖 (527 slides) + clipboard fallback |
| User | (review) | drake1128 在 sidecar 選 91 張投影片 |
| D7 | `53206d0` + `1a8acfd` | process_selections + 選圖 JSONs |
| D8 | `e6fa655` | **9 章內容**填入 (9 個 parallel subagents) |
| D9 | `5ee418d` | Hub 頁 |
| E11 | `6442474` | sitemap.xml + index.html 註冊 |
| E12 | (push) | Push 到 GitHub Pages |

---

## 🔧 如果要再回來改東西，從哪裡開始？

| 想做的事 | 看哪裡 |
|---|---|
| 改某章的卡片解說 / MCQ | 直接編 `cas-2026-NN-<slug>.html` 內對應 `.card` 或 `.quiz-question` |
| 換掉某張圖 | 改 `<img src>` 路徑；新圖放到 `images-cas-2026/NN-*/` |
| 新增一張卡片 | 在 `#cards-container` 內 append `.card`，記得 `data-card-key="card-N"` 唯一 |
| 改章節順序 / 名稱 | 改 `cas-2026-shared.js` 內 CHAPTERS array + 各 chapter HTML 內 `data-chapter` + nav links |
| 重新抽圖 (講師更新講義) | 把新檔放到 `Carotid 頸動脈支架訓練課程歷年投影片 2026/`，更新 `tools/cas-2026-pipeline/chapter_sources.json`，刪 `docs/cas-2026/NN-*/` 對應的 staging folder，重跑 `python run_pipeline.py 100`（**100 DPI 是手機螢幕足夠的解析度** — 不要回到 200，會讓 repo 多 100 MB） |
| 加新章節 | 1) 新增到 CHAPTERS array；2) 新增到 chapter_sources.json；3) 新增到 CHAPTER_TITLES dict；4) 新增 chapter HTML；5) 更新 Hub 的 chapter grid；6) 加 sitemap.xml entry |
| 重新部署 | `git push origin main` (GitHub Pages 自動部署) |

---

## 🧰 環境依賴

- **OS**: Windows 11 (路徑含繁體中文)
- **Python**: 3.13.2
- **Python 套件**: PyMuPDF (fitz)、pywin32、Jinja2 — 見 `tools/cas-2026-pipeline/requirements.txt` (用 `>=` pin)
- **Microsoft Office**: PowerPoint 必裝 (COM 抽 .ppt/.pptx/.pptm → PDF)
- **Node**: 任意 LTS (用於 sanity check scripts，非 runtime 依賴)
- **Git remote**: `github.com/drake1128/saq-questionnaire`

---

## 📝 學到的 lessons (給未來)

1. **9 章 parallel subagents 跑 content 寫得很順** — 因為每章是獨立檔案，沒有 git race；用 "draft + don't commit; controller batch commits" 模式避開衝突。
2. **PowerPoint COM 比 LibreOffice headless 在 Windows 穩定** — 計畫原本要 LibreOffice，實作改 COM 避免額外裝。
3. **Google Drive 路徑含中文字串** — Bash 全程用 `git -C "path"` 不 `cd`；Python 用 `Path(r"...")` raw string。
4. **localStorage progress schema 的 dependent state (totalCards) 寫在 progress 內，不要寫在 CHAPTERS array** — 早期設計 bug，T1 review 抓到並修。
5. **5 cards 對 EPD 章節稍少但仍可接受** — 圖太少時不要硬擠卡片數量；質 > 量。

---

## 📖 補充 reading

- 設計規格全文：[spec](../superpowers/specs/2026-05-22-cas-2026-training-module-design.md)
- 實作計畫全文：[plan](../superpowers/plans/2026-05-22-cas-2026-training-module.md)
- 共用 repo pattern：見記憶 [[teaching-repo-saq]]
- User profile：見記憶 [[user-role]]
- 通訊風格：見記憶 [[feedback-communication-style]]
