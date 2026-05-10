# TEER vs Surgical Mitral Repair — Clinical Decision Aid

**Spec date**: 2026-05-10
**Status**: Approved scope (DMR + FMR; no T-TEER in this iteration)
**Output**: `teer-decision-aid.html`
**Style template**: Same family as `laao-neurology-decision-aid.html` and `dementia-pci-decision-tool.html` — light theme, bilingual zh/en, share button, embedded quiz, references with DOI links.

## Goal

A clinical decision aid that helps mixed audiences (cardiologists, CT surgeons, heart-failure team, advanced practice nurses, and informed family members) reason about Mitral TEER (MitraClip / PASCAL) vs surgical mitral valve repair vs medical/GDMT therapy. The tool emphasizes **balanced evidence framing** — particularly the COAPT vs MITRA-FR tension in functional MR — rather than producing automated recommendations.

## Audience

Multi-tier (匹配 LAAO 工具策略):
- **Primary**: Heart-team clinicians (cardiologists making the referral, CT surgeons evaluating operative risk, HF specialists optimizing GDMT)
- **Secondary**: APNs and ward staff for patient education context
- **Tertiary**: Highly informed patients/family — primarily through bilingual talking-point cards

## Non-goals

- **No automated "recommendation engine"**. Calculator scope is limited to STS / EuroSCORE II. The tool intentionally does NOT take MR type + STS + EF + anatomy → output a single answer. That would (a) overstate certainty, (b) bypass heart-team judgment, (c) create medico-legal exposure.
- **No T-TEER (TriClip / PASCAL Tricuspid)** in this iteration. Deferred to a future module.
- No surgical valve replacement decision logic for severe MR (focus is repair-eligible).
- No AF / atrial cardiomyopathy / atrial-FMR deep dive (mention only).

## Sections (10)

### 1. Disclaimer + intro
Bilingual. State scope (DMR + FMR), users (cardio + CT surg + HF team + APN + family), heart-team-first principle.

### 2. MR pathophysiology primer
- **DMR (Primary / Degenerative)**: Carpentier types I/II/IIIa/IIIb, prolapse, leaflet flail, scallop nomenclature (A1/2/3, P1/2/3).
- **FMR (Secondary / Functional)**: annular dilation, papillary muscle tethering, atrial-FMR vs ventricular-FMR (key clinical distinction).
- **Proportionate vs Disproportionate MR** — central concept that explains COAPT/MITRA-FR divergence:
  - Disproportionate MR (severe MR + smaller LV) → benefits from MR reduction → COAPT-like positive result.
  - Proportionate MR (MR severity tracks LV dilation) → MR reduction doesn't fix the underlying cardiomyopathy → MITRA-FR-like neutral result.

### 3. Surgical risk quick estimator
- Interactive checkbox-style **approximation** of STS-PROM key risk factors (age tiers, prior cardiac surgery, EF, NYHA, renal, lung, frailty proxy).
- Output: 4-tier stratification (low &lt;3% / intermediate 3–8% / high 8–15% / prohibitive ≥15%) matching ACC/AHA & ESC VHD guideline categories for "high surgical risk → favor TEER".
- **Clearly labeled** as an approximation, with disclaimer linking to the full STS Adult Cardiac Surgery Risk Calculator for actual decisions.
- Single calculator (not STS + EuroSCORE both — STS approximation alone, since US/Asia practice predominantly cites STS).

### 4. DMR pathway — Surgery vs TEER vs Watchful waiting
- **Position statement**: Surgery (mitral valve repair, ideally) remains gold standard for symptomatic severe primary MR. Operative mortality &lt;1% at high-volume centers; durability excellent.
- **TEER role**: alternative when STS high, anatomy hostile, &gt;75 yrs, frailty, multiple comorbidities; or when surgical repair likely not durable.
- **Trial cards** (3 side-by-side):
  - **REPAIR-MR** (RCT, 2024 ACC LBCT) — TEER vs surgery in primary MR, intermediate-risk; key results.
  - **CLASP IID** (PASCAL vs MitraClip, 2023) — non-inferiority across both devices in DMR; informs device choice.
  - **EVOREST / Edwards PASCAL real-world** — early experience, anatomic versatility.
- **Anatomy considerations**: leaflet length, MV area, calcification, jet location.

### 5. FMR pathway — GDMT → TEER → Surgery (rare)
- **The Big Tension**: COAPT (positive primary outcome) vs MITRA-FR (neutral). Explain WHY:
  - COAPT: smaller LV, more severe MR, fully optimized GDMT.
  - MITRA-FR: larger LV, less proportionately severe MR, less optimized GDMT.
- **Proportionate vs Disproportionate MR framework** (Grayburn 2019) — bridge concept.
- **RESHAPE-HF2 (NEJM 2024)** — modest benefit, somewhere between COAPT and MITRA-FR; nuanced.
- **Surgical FMR repair** — limited role post-STICH-MR / CTSnet evidence (poor durability, no mortality benefit). One-paragraph mention.
- **Trial cards** (3 side-by-side): COAPT, MITRA-FR, RESHAPE-HF2.
- **Compact comparison table**: population, LV size, MR severity, GDMT, primary outcome.

### 6. Anatomy / Eligibility checklist (reference)
- Non-interactive. Bullet-form quick reference for what makes a patient TEER-eligible:
  - Leaflet length ≥10 mm
  - MV area ≥4.0 cm²
  - No severe MAC (mitral annular calcification)
  - Mean gradient &lt;5 mmHg expected post-clip
  - Jet location amenable (central A2-P2 preferred)
  - LVEF ≥20% (FMR), LVEF preserved (DMR)

### 7. Heart team referral pathway (5-step flowchart)
1. Confirm severe MR by imaging — TTE → TEE if uncertain
2. Classify DMR vs FMR (mechanism, anatomy, EF, LV size)
3. Optimize GDMT (FMR) or watchful waiting / repair planning (DMR asymptomatic)
4. STS / EuroSCORE risk + anatomy review → heart team conference
5. Procedure → 30-day, 6-month, 12-month follow-up

### 8. Family talking points (中英對照)
~5 bilingual cards:
- 「TEER 不是換瓣膜，是用夾子把鬆開的瓣葉夾起來」
- 退化性 MR vs 功能性 MR 的差異 (用簡單比喻)
- 為什麼有些人外科開刀比較好、有些人 TEER 比較好
- 住院、恢復、再介入的差異
- 病人決策角色：heart team 一起討論

### 9. Self-assessment quiz (7 MCQs)
Bilingual stems, options, explanations:
1. DMR Carpentier classification — distinguishing types
2. Why is surgery still gold standard in low-risk DMR?
3. COAPT vs MITRA-FR — what was the key population difference?
4. Proportionate vs disproportionate MR — definition + significance
5. RESHAPE-HF2 contribution to the FMR debate
6. Which anatomy is hostile to TEER?
7. Best practice for shared decision making in severe symptomatic FMR with optimized GDMT

### 10. References
DOI/PMID-linked:
- Stone GW et al. COAPT — TEER for HF. NEJM 2018;379:2307-18.
- Obadia JF et al. MITRA-FR. NEJM 2018;379:2297-306.
- Anker SD et al. RESHAPE-HF2. NEJM 2024.
- Lim DS et al. CLASP IID 1-yr results. JACC 2023.
- Ailawadi G et al. REPAIR-MR (TEER vs surgery in primary MR, intermediate-risk). Late-breaking at ACC 2024; full publication forthcoming — link to ACC press release as interim source.
- Grayburn PA et al. Proportionate vs Disproportionate Sec MR. JACC Cardiovasc Imaging 2019;12:353-62.
- Otto CM et al. 2020 ACC/AHA Guideline for VHD (updated 2022 Focused Update).
- Vahanian A et al. 2021 ESC/EACTS VHD Guideline (with 2023 updates).
- (FMR surgery context) Goldstein D et al. STICH-MR / CTSN trial. NEJM 2014;370:23-32.

## Components

| Unit | Purpose | Interface |
|------|---------|-----------|
| Header / hospital badge | Identity | Static HTML |
| Share button | LINE / Email / Copy / QR | Existing pattern from LAAO (reused) |
| MR primer section | DMR vs FMR + proportionate concept | Static bilingual content |
| STS calculator | Risk stratification | Checkbox-driven; same JS pattern as `calcChads()` in LAAO |
| Trial cards (DMR) | REPAIR-MR / CLASP IID / EVOREST | CSS grid (2-col → 1-col mobile) |
| Trial cards (FMR) | COAPT / MITRA-FR / RESHAPE-HF2 | Same grid pattern, color-coded by verdict |
| Comparison table | Side-by-side trial populations | HTML `<table>` |
| Eligibility checklist | Anatomy reference | Static list |
| Decision flowchart | 5-step pathway | Same `.flow-step` pattern as LAAO |
| Family talking cards | Bilingual SDM aids | `.talk-card` pattern |
| Quiz engine | 7 MCQs with bilingual explanations | Same JS as LAAO (reused) |
| References block | Citations | `<ol>` with hyperlinks |

## Data flow

Pure static + client-side JS. No backend, no persistence. Quiz state lives in module-scope variables. STS calculator is reactive to checkbox events.

## Error handling

- All inputs are checkbox/click-driven; no free text → no validation needed.
- Quiz protects against double-click on options (`qAnswered` flag).
- Share-button QR generation uses external API; if network blocked, the LINE/Email/Copy fallbacks still function.

## Testing

- Visual smoke test via Playwright (same pattern as LAAO):
  - Page renders, title correct
  - STS calculator responds to checkboxes
  - Quiz renders and progresses
  - Share button menu opens with QR + LINE + Email + Copy
  - All 6 trial cards visible (3 DMR + 3 FMR)
  - Comparison table renders

## Integration

- Add card to `index.html` in **病人與家屬衛教 Patient Education** category, after `laao-neurology-decision-aid.html`. Bump section count from 14 → 15.
- Tags: `patient`, `staff`, `guideline`, `education`, `teer`, `mitraclip`, `pascal`, `mitral`, `mr`, `coapt`, `mitra-fr`, `reshape-hf2`, `repair-mr`, `valvular`, `heart team`, `shared decision making`, `中英對照`, etc.

## Open questions / future enhancements

- T-TEER addition (separate iteration)
- Atrial functional MR — emerging concept; minimal coverage now
- Concomitant TEER + ablation / TEER + LAAO — not in scope

---

*Drafted with Claude Opus 4.7 per brainstorming session 2026-05-10. Awaiting user review.*
