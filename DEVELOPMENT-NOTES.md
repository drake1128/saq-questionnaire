# Cardiovascular Education Hub - Development Notes

## Project Overview
心血管照護教學資源中心 (Cardiovascular Care Education Hub)
NTUH Hsinchu Branch - Cardiovascular Center

---

## Recent Updates

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
