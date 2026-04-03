---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Noto Sans TC', 'Segoe UI', sans-serif;
    background: #0f172a;
    color: #e2e8f0;
  }
  h1 { color: #38bdf8; font-size: 2.2em; }
  h2 { color: #22d3ee; font-size: 1.6em; border-bottom: 2px solid #334155; padding-bottom: 8px; }
  h3 { color: #fbbf24; font-size: 1.2em; }
  strong { color: #f472b6; }
  a { color: #60a5fa; }
  table { font-size: 0.8em; width: 100%; border-collapse: collapse; }
  th { background: #1e293b; color: #38bdf8; padding: 10px; text-align: left; }
  td { padding: 8px 10px; border-bottom: 1px solid #334155; }
  tr:nth-child(even) { background: rgba(255,255,255,0.03); }
  code { background: #1e293b; color: #fbbf24; padding: 2px 6px; border-radius: 4px; }
  blockquote { border-left: 4px solid #f472b6; padding-left: 16px; color: #94a3b8; font-style: italic; }
  section.lead h1 { font-size: 2.8em; text-align: center; }
  section.lead p { text-align: center; font-size: 1.1em; color: #94a3b8; }
  .columns { display: flex; gap: 24px; }
  .col { flex: 1; }
  .highlight { background: linear-gradient(135deg, rgba(56,189,248,0.15), rgba(34,211,238,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(56,189,248,0.3); }
  .warn { background: linear-gradient(135deg, rgba(244,114,182,0.15), rgba(244,114,182,0.05)); border-radius: 12px; padding: 16px; border: 1px solid rgba(244,114,182,0.3); }
  footer { color: #64748b; font-size: 0.6em; }
---

<!-- _class: lead -->

# 心房顫動整流（Cardioversion）
# 文獻回顧與臨床實務

**新竹分院心臟血管中心**
2026-04-03

---

## 縮寫對照表 Abbreviations

| 縮寫 | 全稱 | 中文 |
|------|------|------|
| AF | Atrial Fibrillation | 心房顫動 |
| AFL | Atrial Flutter | 心房撲動 |
| ECV | Electrical Cardioversion | 電擊整流 |
| PCV | Pharmacological Cardioversion | 藥物整流 |
| NSR | Normal Sinus Rhythm | 正常竇性節律 |
| TEE | Transesophageal Echocardiography | 經食道超音波 |
| HF / HFrEF | Heart Failure / HF with Reduced EF | 心衰竭 / 低射出分率心衰竭 |
| VT / VF | Ventricular Tachycardia / Fibrillation | 心室頻脈 / 心室顫動 |

---

## 背景：為什麼要討論 Cardioversion？

- AF 是最常見的持續性心律不整
- 傳統觀念（2002 年後）傾向 **rate control**，ECV 執行率低
- **2020 年 EAST-AFNET 4** 翻轉觀念 → 早期 rhythm control 有益
- 我們的臨床目標：**透過恢復竇律，減少心衰竭負擔**

<div class="highlight">

**核心問題：**
1. ECV 執行率為何偏低？
2. PCV vs ECV 的中風風險誰比較高？
3. Rhythm control 真的能降低心衰竭嗎？

</div>

---

## 第一部分：ECV 為什麼執行率低？

### AFFIRM 與 RACE 的影響（2002）

<div class="columns">
<div class="col">

**AFFIRM Trial** — Wyse DG et al., *NEJM* 2002
- Rhythm control vs rate control **無存活差異**
- Rhythm control 組住院更多、藥物副作用更大
- [DOI: 10.1056/NEJMoa021328](https://doi.org/10.1056/NEJMoa021328)

</div>
<div class="col">

**RACE Trial** — Van Gelder IC et al., *NEJM* 2002
- Rate control **不劣於** rhythm control
- 進一步強化 AFFIRM 結論
- [DOI: 10.1056/NEJMoa021375](https://doi.org/10.1056/NEJMoa021375)

</div>
</div>

> 這兩個試驗讓整個領域偏向 rate control，ECV 逐漸被「冷落」長達近 20 年

---

## ECV 低使用率的實際障礙

### Brandes A et al., *Europace* 2020

| 障礙因素 | 說明 |
|----------|------|
| 鎮靜 / 麻醉需求 | 需要麻醉科支援，增加程序安排難度 |
| 復發率偏高 | 未用抗心律不整藥時，1 年復發率約 50% |
| Post-AFFIRM 心態 | 「rate control 就好」的根深蒂固觀念 |
| 程序安排困難 | 需協調設備、人力、禁食等 |
| 抗凝血顧慮 | 擔心整流導致血栓栓塞 / 中風 |

[PubMed: 32091085](https://pubmed.ncbi.nlm.nih.gov/32091085/)

---

## 第二部分：PCV vs ECV 的中風風險

### 核心結論

<div class="warn">

**PCV 與 ECV 的血栓栓塞風險無顯著差異**
風險取決於病人因素（CHA₂DS₂-VASc）與抗凝血狀態，而非整流方式

</div>

---

## FinCV Study — 最直接的證據

**Airaksinen KEJ et al., *JACC* 2013**

- 芬蘭全國資料，**5,116 次 cardioversion**
- 30 天血栓栓塞風險：**約 0.7%**
- PCV vs ECV：**無統計學顯著差異**
- 獨立危險因子：心衰竭、糖尿病、AF 持續 >12 小時

[DOI: 10.1016/j.jacc.2013.04.089](https://doi.org/10.1016/j.jacc.2013.04.089)

### FinCV — 急性 AF 子分析（Eur Heart J 2013）

- AF <48 小時的栓塞率同樣低（~0.7%）
- 整流方式（PCV vs ECV）**不是獨立預測因子**
- [PubMed: 23800496](https://pubmed.ncbi.nlm.nih.gov/23800496/)

---

## ACUTE Trial — TEE 引導策略

**Klein AL et al., *NEJM* 2001**

<div class="columns">
<div class="col">

### TEE-guided 策略
- TEE 排除血栓 → 立即整流
- 栓塞率：**~0.8%**
- 出血風險 **較低**
- 更早恢復竇律

</div>
<div class="col">

### 傳統策略
- 抗凝 3 週 → 整流
- 栓塞率：**~0.8%**（相似）
- 出血風險較高
- 等待期間 AF 可能自行終止或惡化

</div>
</div>

[DOI: 10.1056/NEJM200105103441901](https://doi.org/10.1056/NEJM200105103441901)

---

## 整體 Cardioversion 血栓風險摘要

| 指標 | 數值 |
|------|------|
| 整體栓塞率（30 天） | **0.5 – 1.0%** |
| 充分抗凝後栓塞率 | **< 0.5%** |
| PCV vs ECV 差異 | **無顯著差異** |
| 主要危險因子 | CHA₂DS₂-VASc 成分（HF、DM、年齡、中風史） |

### 指引建議
- AF ≥48hr 或不明持續時間 → 整流前抗凝 **≥3 週**，或 **TEE-guided**
- 整流後持續抗凝 **≥4 週**
- 血行動力學不穩定 → **立即整流，不需等待抗凝**

---

## 第三部分：Rhythm Control 能否降低心衰竭？

### 答案：能。關鍵證據來自 EAST-AFNET 4

---

## EAST-AFNET 4 — 改變遊戲規則的試驗

**Kirchhof P et al., *NEJM* 2020**

- **2,789 位**早期 AF 患者（診斷 ≤1 年）
- 早期 rhythm control（含 ECV、抗心律不整藥、ablation）

### 主要結果

| 終點 | 早期 Rhythm Control | Rate Control | HR |
|------|--------------------|--------------|----|
| 心血管死亡 + 中風 + HF 住院 + ACS | **較低** | 參考 | **0.79** |

<div class="highlight">

**重要意義：** 翻轉了 AFFIRM 時代「rate control 就好」的觀念。
早期 rhythm control 可以同時降低**中風、心衰竭住院、心血管死亡**。

</div>

[DOI: 10.1056/NEJMoa2019422](https://doi.org/10.1056/NEJMoa2019422)

---

## EAST-AFNET 4 心衰竭子分析

**Rillig A, Kirchhof P et al., *Eur Heart J* 2021**

- 在 HF 亞群中，早期 rhythm control 的**相對獲益比整體更大**
- 直接支持：對 AF 合併 HF 的病人，應積極進行 rhythm control

[PubMed: 34447995](https://pubmed.ncbi.nlm.nih.gov/34447995/)

### CASTLE-AF — Marrouche NF et al., *NEJM* 2018

- AF + HFrEF，catheter ablation 恢復竇律
- 全因死亡率 **HR 0.53**（降低 47%）
- 心衰竭住院顯著降低
- [DOI: 10.1056/NEJMoa1707855](https://doi.org/10.1056/NEJMoa1707855)

---

## 臨床指引摘要

<div class="columns">
<div class="col">

### 2024 ESC AF Guidelines
Van Gelder IC et al., *Eur Heart J*
- AF-CARE pathway
- 採用 CHA₂DS₂-VA（移除性別）
- 強調**早期 rhythm control**
- [DOI: 10.1093/eurheartj/ehae176](https://doi.org/10.1093/eurheartj/ehae176)

</div>
<div class="col">

### 2023 AHA/ACC/HRS Guidelines
Joglar JA et al., *Circulation*
- PCV 與 ECV 栓塞風險相當
- 整流前後抗凝建議
- Class I：血行動力學不穩定 → 立即整流
- [DOI: 10.1161/CIR.0000000000001193](https://doi.org/10.1161/CIR.0000000000001193)

</div>
</div>

---

## 臨床重點整理

| 問題 | 答案 |
|------|------|
| ECV 為什麼執行率低？ | AFFIRM/RACE 後 rate control 觀念主導 + 鎮靜需求 + 復發率高 |
| PCV vs ECV 中風風險？ | **無顯著差異**（FinCV），取決於 CHA₂DS₂-VASc 與抗凝狀態 |
| 整體栓塞風險？ | ~0.5-1.0%/30 天，充分抗凝 < 0.5% |
| Rhythm control 能降低 HF？ | **能** — EAST-AFNET 4 證實，HF 亞群獲益更大 |

<div class="highlight">

**Take-home message：** 不要因為擔心中風而不做 cardioversion。
充分抗凝下風險很低（<0.5%），而早期恢復竇律可顯著減少心衰竭負擔。

</div>

---

## 延伸學習資源

### 手機教學模組
掃描 QR Code 或開啟連結，可在手機上互動式學習 AF 病房處置：

**心房顫動病房處置教學 App**
https://drake1128.github.io/saq-questionnaire/af-ward-teaching-app.html

涵蓋：心率控制藥物、整流決策、CHA₂DS₂-VA 計算、藥物劑量速查

---

<!-- _class: lead -->

# 謝謝
# Thank You

**歡迎回饋與討論**
新竹分院心臟血管中心
