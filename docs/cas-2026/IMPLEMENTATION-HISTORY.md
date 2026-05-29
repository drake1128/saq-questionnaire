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
| **文獻引用** | 11 PDFs + 1 XML + 主總表 + 3 chapter findings (2026-05-24 加入) | `docs/cas-2026/references/` |
| **Pipeline 工具** | extract / generate_sidecar / process_selections / run_pipeline | `tools/cas-2026-pipeline/` |
| **Sidecar 縮圖頁** | 9 個 user-review HTMLs (一次性工具) | `docs/cas-2026/*-slides-overview.html` |
| **用戶選圖 JSON** | 9 個 (備份) | `tools/cas-2026-pipeline/selections/` |
| **Spec** | 設計規格 | `docs/superpowers/specs/2026-05-22-cas-2026-training-module-design.md` |
| **Plan** | 12-task 實作計畫 | `docs/superpowers/plans/2026-05-22-cas-2026-training-module.md` |

**統計** (含 2026-05-24 文獻整合後)：
- **80 卡片** (原 66 + 14 從 2021-2026 guidelines/reviews 加入)
- **27 道 MCQ** (Quiz 未動)
- **99 張圖片** (91 投影片 + 8 PDF 提取)
- **11 篇引用 PDFs + 1 篇 XML** 收藏在 references/

**2026-05-24 文獻整合摘要：**
| Ch | 變動 | 引用 |
|---|---|---|
| 1 | +Card 9 (Bos IPH HR 2.42), Card 7+8 IAC 2023 註 | Bos JACC 2021 |
| 2 | +Card 9 (VW-MRI), Card 10 (ESCR 多參數) | Zhang 2025 MA, ESCR 2023 |
| 3 | Card 5 重寫 (CMOSS warning), +Card 8 (時間窗+CIRSE+ACST-2) | CMOSS JAMA 2023 |
| 4 | +Card 8 (TFCAS/TR/TCAR), Card 3 tip | ESVS 2023, Dixit 2026 |
| 5 | Card 3 重寫, +Card 6 (layered), +Card 7 (TCAR flow reversal) | Giannopoulos 2024 MA |
| 6 | +Card 8 (dual-layer paradigm), +Card 9 (CGuard vs Roadsaver) | Mazurek 2022 (n=68,422) |
| 7 | +Card 9 (TCAR/ROADSTER-2), Card 1+objectives 註明範圍 | ESVS Rec 82, Zarrintan VQI |
| 8 | +Card 9 (ACST-2 K-M), +Card 10 (cost-eff) | Halliday Lancet 2021 |
| 9 | Card 2 ABSOLUTE contraindication tip, +Card 9 (transradial) | CIRSE 2024, Batista 2024 |

**2026-05-25 收尾工作：**

| 工作 | 變動 | Commit |
|---|---|---|
| DOI / PMID 全部超連結化 | 11 DOIs → `doi.org`、21 PMIDs → `pubmed.ncbi.nlm.nih.gov`；全部 `target="_blank" rel="noopener"`；含 Lancet DOI 內嵌括弧的特殊處理 | `6455a41` |
| PDF 圖片精修 | Ch1 page09 刪除（純文字無 figure）；Ch1 page08 crop 9-77%（去 journal header + caption）；Ch8 ACST-2 page07 crop 4-62%（-68% 檔案大小，只留 4-panel K-M） | `7c764c1` |

**待考慮的 follow-up（5 張 PDF 圖目前 acceptable 但 user 可能想再 crop）：**
- Ch2 `2023-saba-ESCR-partI-page16.png` — Table 7 整頁，table 內容密
- Ch2 `2023-saba-ESCR-partII-page06.png` — Table 2 plaque feature
- Ch7 `2023-zarrintan-VQI-page06.png` — 4 K-M + 2 forest plot
- Ch8 `2025-akkara-costeff-page06.png` — 2 forest plot
- Ch9 `2024-batista-transradial-page07.png` — 4 forest plot

「修圖再說」狀態 — 等 user 看完上線版再決定要不要 crop。

**2026-05-26 講師徵詢草稿：**

由 user (謝慕揚, drake1128) 出面，向 10 位曾授課老師發出徵詢信。已建立 **10 份 Gmail drafts**：

| # | 老師 | 章節 | TO |
|---|---|---|---|
| 1 | 湯頌君 | Ch1 (2022) | ⏳ tbd-tang-sj@placeholder.invalid |
| 2 | 葉馨喬 | Ch1 (2024) | ⏳ tbd-yeh-hc@placeholder.invalid |
| 3 | 李崇維 | Ch2 | ✅ rad.chungweilee@gmail.com |
| 4 | 黃國川 | Ch3 | ⏳ tbd-huang-kc@placeholder.invalid |
| 5 | 蘇峻弘 | Ch4 | ⏳ tbd-su-ch@placeholder.invalid |
| 6 | 黃成偉 | Ch5 (2022+2024) | ⏳ tbd-huang-cw@placeholder.invalid |
| 7 | 蔡翰林 | Ch6 (2022 TTT + 2024 Stent) | ⏳ tbd-tsai-hl@placeholder.invalid |
| 8 | 柯呈諭 | Ch7 (2022+2024) | ⏳ tbd-ko-cy@placeholder.invalid |
| 9 | 黃致遠 | Ch8 | ⏳ tbd-huang-cy@placeholder.invalid |
| 10 | 方修御 | Ch9 | ⏳ tbd-fang-hy@placeholder.invalid |

只有李崇維 email 從 PPTX text extraction 找到；其餘 9 位需要由 user 從 Gmail 草稿夾手動填 TO 後送出。

**每封信內容包含：**
- 緣起說明（課程時間不夠、討論不充分）
- 解方介紹（手機可操作互動模組、預習 + 課後測驗）
- 對應章節 URL + 該章相關最新文獻 highlights
- 三個請求：審視內容、同意素材使用、邀稿個人沙龍照／獨照

**收到老師肖像照後的工作：** 為網站新增「講師介紹」區塊 / cards（目前 HTML 尚未實作）。等到第一批照片回來再做。

---

## 🔬 2026-05-29 → 30：Ch1 講師回饋修訂 + 引用查證更正

**觸發：** 葉馨喬醫師（Ch1 2024 講師，shinjoeyeh@gmail.com）回信，同意素材使用、提供肖像照，並針對 Ch1 提出修改建議（含一份新投影片檔附件）。

**新來源檔：** `C:\Users\drake\Downloads\Ultrasound imaging for carotid arteries 2026.ppt`（共 28 張）。用 **PowerPoint COM** 抽出第 10、24 張 → `images-cas-2026/01-ultrasound/2026-yeh-hc-seq010.png`、`2026-yeh-hc-seq024.png`（命名沿用既有 `YYYY-yeh-hc-seqNNN` 慣例）。抽圖前先 dump slide text 比對，確認 P10 = vulnerable plaque morphology、P24 = modified SRU/IAC ICA 速度標準，與信中描述相符。

**依信完成的 4 項修訂：**

| 卡片 | 修改 |
|---|---|
| Card 3 B-mode 斑塊形態學 | 投影片改用新檔 P10；說明補上 echolucent/echodense + **GSM ≤25** |
| Card 6 狹窄血流動力學 | 參考管徑 B 之「**近端**正常段」→「**遠端**正常段」（NASCET 量法） |
| Card 7 狹窄分級標準 | 投影片改用新檔 P24；PSV 閾值更新為 **<180=<50%、180–230=50–69%、>230=≥70%** |
| Card 7 + 8 | 移除錯誤的「IAC 2023」引用（見下） |

**🚩 引用查證更正（兩件，均為 hallucinated / 誤植 citation）：**

1. **「IAC 2023 共識文件」不存在。** 葉醫師於信中質疑（查無此文件）。查證後確認真正出處就是她 P24 投影片底下所引的那篇——
   **Gornik HL, et al. *Optimization of duplex velocity criteria for diagnosis of ICA stenosis: a report of the IAC Vascular Testing Division Carotid Diagnostic Criteria Committee.* Vasc Med 2021;26(5):515–525（PMID 34009060）。**
   是 IAC 文件沒錯，但年份是 **2021 不是 2023**，且只談**原生動脈**（將 SRU 2003 的 ≥50% PSV 閾值由 ≥125 提高到 ≥180），**完全未涵蓋 post-stent**。Card 7/8 的「IAC 2023」字樣已全部改為正確引用。

2. **Card 8 的 Nederkoorn 2009 引用被誤描述，且數字為兩篇混用。**
   - Nederkoorn PJ, Brown MM. BMC Neurol 2009;9:36（PMID 19624830）**確實存在，但它是 review + study protocol**（PubMed 標 "Review"），並非導出/驗證閾值的原始研究——僅可作為「stent ↓ compliance → ↑velocity」概念回顧。
   - 原文「PSV >300 或 ratio >4.75」其實是兩篇單中心小研究混拼：**PSV >300 + EDV >90 + ICA/CCA >4** 出自 **Zhou W, J Vasc Surg 2008;47:74–80（PMID 18178456）**（僅 18 lesion / 11 人）；**ratio ≥4.75（+PSV ≥350）** 出自 **Stanziale SF, J Endovasc Ther 2005;12:346–53（PMID 15943510）**。
   - 已更正 Card 8 **body、image alt、source line、注意 tip、Quick Check Q2 解說** 共 5 處：改列兩組正確歸屬的閾值、註明「無統一共識、均小型單中心研究」、Nederkoorn 降格為概念回顧。

**文獻 PDF 歸檔**（`docs/cas-2026/references/01-ultrasound/`）：
- `2021-Gornik-IAC-ICA-velocity-criteria-VascMed.pdf`（Europe PMC OA；publisher owner-encrypt，閱讀正常但無法複製）
- `2009-Nederkoorn-stented-ICA-velocity-review-BMCNeurol.pdf`（BMC OA）
- Zhou 2008 / Stanziale 2005 為付費期刊（無 OA PMC），僅留 citation + PMID 連結。
- 另備一份在 `C:\Users\drake\Downloads\CAS2026-Ch1-references\`。

**對外通訊：** 已建立一份 **Gmail 回信草稿**（thread `19e64b695a76d56c`，未寄出），向葉醫師確認 4 項修訂並誠實說明「IAC 2023」查證結果。⏳ Card 8 的 Nederkoorn/Stanziale/Zhou 更正尚未寫進該草稿。

**Commits：**
| Commit | 摘要 |
|---|---|
| `fa166ca` | Ch1 套用葉醫師 slide/閾值修訂、IAC 2023→Gornik 2021 |
| `1c6db08` | Ch1 Card 8 post-stent ISR 引用與閾值更正（Stanziale/Zhou） |

**Lesson（給未來）：** 任何「某某 guideline/consensus 說…」的引用都要實際查到 PMID 才寫；本次兩處 citation 都在臨床審查階段被講師/查證抓到（呼應記憶 [[feedback_questionnaire_scoring_qc]]、[[reference_carotid_duplex_iac2021_criteria]]）。投影片標題年份（如 P24 寫「2023」）≠ 原始文獻年份，勿直接當引用年。

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

📖 **2026-05-24 加：** `docs/cas-2026/references/REFERENCES-2021-2026.md` 整理了 9 章對應 2021-2026 最新 guideline / review / trial (含 ACST-2, ESVS 2023, CIRSE 2024, ESCR 2023, CMOSS, Mazurek dual-layer stent MA 等)。讀那份「🔴 最重要 8 件事」section 可快速找到 HTML 內容潛在的過時點。

我 draft 的卡片內容根據投影片做了「最佳詮釋」。Subagent 已自報的疑慮：

| 章 | 疑慮 |
|---|---|
| Ch1 Card 7 | ✅ **已解決 (2026-05-29)** — 改用葉醫師新檔 P24，閾值更新為 IAC/Gornik 2021（≥50% 改 ≥180 cm/s）。見上方 2026-05-29 區塊 |
| Ch1 Card 8 | ✅ **已解決 (2026-05-30)** — 原 Nederkoorn 2009 引用誤植已更正為 Stanziale 2005 + Zhou 2008，並註明無共識。見上方 2026-05-29 區塊 |
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
