# Cardiovascular Education Hub - Development Notes

## Project Overview
心血管照護教學資源中心 (Cardiovascular Care Education Hub)
NTUH Hsinchu Branch - Cardiovascular Center

---

## Recent Updates

### 2026-03-25: 資料夾整理 & KCCQ 計分修正

**資料夾清理：**
- 將 22 個未被 HTML 連結的檔案（PDF、PNG、DOCX、TEX、TXT、MD）移至 `Archive Folder/`
- 刪除無用的 `nul` 檔案
- 更新 `.gitignore`：加入 `Archive Folder/` 和 `firebase-debug.log`

**KCCQ 計分修正（`kccq.html`）：**

| Bug | 嚴重度 | 說明 | 修正方式 |
|-----|--------|------|----------|
| SB 症狀負擔 value=6 未重新編碼 | 嚴重 | Q7-Q11「沒有此症狀」(value=6) 應等同「完全不困擾」(value=5)，修正前兩者分數差 20 分 | value=6 重新編碼為 5 |
| SB 分母錯誤 | 嚴重 | 分母 25 (30-5) 應為 20 (25-5)，因 value=6 已重新編碼 | 分母改為 20 |
| SF 症狀頻率混合量尺 | 中度 | Q2-Q5 為 6 級、Q6 為 5 級，直接加總會低估 Q6 權重 | 改為逐題轉換 0-100 後取平均 |
| 缺少臨床概要分數 (CS) | 中度 | CS = (PL + TSS) / 2 是臨床試驗常用的核心複合分數，但未計算顯示 | 新增 CS 計算與顯示 |

**Git commits:** `2f37449`

---

### 2026-03-23: SAQ 計分修正

**SAQ 計分修正（`seattle-saq.html`）：**

| Bug | 嚴重度 | 說明 | 修正方式 |
|-----|--------|------|----------|
| Q10 心絞痛穩定度數值反轉 | 嚴重 | 「好很多」應為 5 但原為 1，方向完全相反 | 反轉數值 |
| Q14 治療滿意度反向計分錯誤 | 嚴重 | 「非常麻煩」應為 1，「完全不麻煩」應為 4 | 修正反向計分 |
| Q18 選項值打字錯誤 | 中度 | 第 4 選項 value="2" 應為 value="4" | 修正 typo |
| Q18 缺少選項 | 中度 | 原為非標準 4 選項，改回原始 SAQ 5 級滿意度量尺 | 補回第 5 選項 |
| DP 疾病認知分母錯誤 | 中度 | 分母 10 應為 12（3 題 × 5 級，範圍 15-3=12） | 分母改為 12 |
| SAQSS 複合分數公式錯誤 | 中度 | 原為 (PL+AF)/2，應為 (PL+AF+DP)/3（依 SAQ-7 標準，Chan 2014） | 改為三域平均 |

**Git commits:** `22ce197`, `bfe0ea9`

---

### ⚠️ 問卷計分 QC 檢查清單（Questionnaire Scoring QC Checklist）

**未來生成或修改問卷類檔案時，務必逐項檢查：**

1. **數值方向一致性**：所有題目是否遵循「分數越高 = 狀態越好」（或反之），特別注意反向計分題目
2. **選項數量正確**：每題選項數是否與原始問卷一致（例如 5 級 vs 6 級）
3. **Radio value 無打字錯誤**：逐一核對 value="1", "2", "3"... 有無跳號或重複
4. **分母/範圍計算**：轉換公式 `(sum - min) / (max - min) * 100` 的分母是否正確
5. **混合量尺處理**：同一 domain 內若有不同級數的題目，須逐題轉換後再平均，不可直接加總
6. **特殊選項處理**：「不適用」「非因此疾病受限」等選項是否正確排除或重新編碼
7. **複合分數公式**：CS、OS、SAQSS 等複合分數的計算公式是否與文獻一致
8. **參考文獻核對**：計分方式應對照原始發表文獻（Spertus 1995 for SAQ; Green 2000 for KCCQ）

---

### 2025-01-11: Cardiology Ward Orientation App
**File:** `cardiology-ward-orientation-2025.html`

Created comprehensive orientation guide for new NPs and residents at 2AB ward and CCU.

**Completed sections:**
- 同意書指引 (Consent Forms Guide)
- 導管室相關 (Cath Lab Procedures) - includes pre-cath checklist, 6P assessment, sheath removal protocol
- 特殊術式指引 (Procedure Guidelines) - CAD, PPM, EPS, LAAO, ICAS, PAOD
- 臨床工作規範 (Clinical Work Rules)
- 病歷書寫規範 (Medical Record Writing)
- 出院規劃 (Discharge Planning)
- 快速查詢 (Quick Reference) - contacts only

**Sections hidden (pending revision):**
- 每週學術活動 (Weekly Academic Schedule)
- 教學活動 (Teaching Activities)
- 重要分機 (Phone Extensions)

**Authors:**
- NP 黃秋燕
- 2A病房主任 潘恆宇 醫師
- CCU病房主任 許如瑩 醫師
- 心血管中心主任 謝慕揚 醫師

---

## To-Do List

### High Priority

- [ ] **Add phone numbers in ward module**
  - Collect accurate extension numbers for:
    - 導管室
    - 心臟超音波室
    - 2A護理站
    - 2B護理站
    - CCU
    - 心臟內科門診
  - Verify numbers before publishing

- [ ] **Revise teaching schedule (每週學術活動)**
  - Confirm current schedule with department
  - Update times, locations, and activities
  - Verify mandatory vs optional sessions

- [ ] **Add patient treatment arrangements section**
  - **Hemodialysis coordination:**
    - Contact dialysis room (洗腎室) to arrange HD schedule
    - Coordinate with cath lab to adjust procedure timing
    - Ensure HD is scheduled appropriately before/after cath procedures
  - **Goal:** Make considerate efforts for good time arrangements
  - Consider adding checklist for patients requiring HD + cath

### Medium Priority

- [ ] Revise 教學活動 (Teaching Activities) section
  - Update morning conference requirements
  - Confirm teaching record requirements
  - Update M&M conference schedule

### Low Priority

- [ ] Add more procedure-specific consent form details
- [ ] Add NHI coverage notes where applicable
- [ ] Consider adding medication dosing quick reference

---

## File Structure

```
saq-questionnaire-main/
├── index.html                              # Main hub page
├── cardiology-ward-orientation-2025.html   # Ward orientation app (NEW)
├── ccu-orientation-manual.html             # CCU manual
├── cto-pci-patient-education.html          # CTO PCI patient education
├── DEVELOPMENT-NOTES.md                    # This file
└── ... (other teaching apps)
```

---

## Notes for Future Development

1. **Hidden sections can be restored** by adding them back to:
   - Home page grid in `HomePage` component
   - `navItems` array in `App` component

2. **Phone extensions data** is still in the code (`quickReference.extensions`), just not displayed

3. **Patient arrangement section** should be added to either:
   - 導管室相關 (Cath Lab) section, or
   - New dedicated section for special patient coordination

---

## Contact

For questions about this project, contact the Cardiovascular Center team.
