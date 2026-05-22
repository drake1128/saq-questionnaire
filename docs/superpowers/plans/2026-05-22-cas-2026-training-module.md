# CAS 2026 Training Module Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a mobile-first teaching module (1 Hub + 9 Chapter HTMLs) for the 2026 CAS Training Course, with an image pipeline that extracts slides from 13 source files (.ppt/.pptx/.pptm/.pdf) and a user-in-the-loop sidecar review workflow for selecting which slides to embed.

**Architecture:** Vanilla HTML/CSS/JS (no React). Each chapter is an independent self-contained HTML using a shared template structure. Cross-chapter progress synced via `localStorage`. Image extraction is a one-time Python pipeline using PowerPoint COM (for .ppt-family) and PyMuPDF (for PDF rendering). Sidecar HTMLs let the user select slides; selected PNGs are copied into `images-cas-2026/` and referenced by chapter HTMLs.

**Tech Stack:** HTML5, CSS3, vanilla JS, Python 3.11+, PyMuPDF (`fitz`), pywin32 (PowerPoint COM on Windows), existing `design-system.css` + `achievements.js` from `saq-questionnaire-main`.

**Reference spec:** `docs/superpowers/specs/2026-05-22-cas-2026-training-module-design.md`

**Working directory:** `G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main\`

---

## Phase Overview

| Phase | Tasks | Owner | Description |
|---|---|---|---|
| A | 1-3 | Claude | Bootstrap shared infra, chapter template, hub structure |
| B | 4-6 | Claude | Image pipeline (extract, sidecar, batch) |
| C | — | **User** | Review sidecars, export selection JSONs |
| D | 7-9 | Claude | Ingest selections, draft & populate 9 chapters |
| E | 10-12 | Claude + User | Mobile QA, sitemap update, GitHub Pages deploy |

---

## Phase A — Shared Infrastructure & Template

### Task 1: Bootstrap shared.js with progress schema and course metadata

**Files:**
- Create: `cas-2026-shared.js`

- [ ] **Step 1: Create `cas-2026-shared.js` with localStorage helpers**

```js
// cas-2026-shared.js
// Cross-chapter progress sync and course metadata for CAS 2026 module.

const CAS2026 = (() => {
  const STORAGE_KEY = 'cas-2026-progress';
  const TOTAL_CHAPTERS = 9;

  const CHAPTERS = [
    { id: 'cas-01', no: 1, slug: 'ultrasound',     title: 'Ultrasound Diagnosis',         speakers: '湯頌君 (2022) / 葉馨喬 (2024)' },
    { id: 'cas-02', no: 2, slug: 'ct-mr',          title: 'CT / MR for ICAS',             speakers: '李崇維 (2022)' },
    { id: 'cas-03', no: 3, slug: 'occlusion',      title: 'Stenosis & Occlusion',         speakers: '黃國川 (2022)' },
    { id: 'cas-04', no: 4, slug: 'techniques',     title: 'General CAS Techniques',       speakers: '蘇峻弘 (2022)' },
    { id: 'cas-05', no: 5, slug: 'epd',            title: 'Embolic Protection Device',    speakers: '黃成偉 (2022, 2024)' },
    { id: 'cas-06', no: 6, slug: 'stent-design',   title: 'Stent Design & TTT',           speakers: '蔡翰林 (2022 TTT / 2024 Stent)' },
    { id: 'cas-07', no: 7, slug: 'tsci',           title: 'Carotid TSCI',                 speakers: '柯呈諭 (2022, 2024)' },
    { id: 'cas-08', no: 8, slug: 'surgical',       title: 'Surgical Approaches',          speakers: '黃致遠 (2024)' },
    { id: 'cas-09', no: 9, slug: 'difficult',      title: 'Difficult CAS Tips & Tricks',  speakers: '方修御 (2024)' },
  ];

  function loadProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
    } catch (e) {
      return {};
    }
  }

  function saveProgress(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  }

  function setCardChecked(chapterId, cardKey, checked) {
    const p = loadProgress();
    p[chapterId] = p[chapterId] || { cards: {}, quiz: {}, completed: false };
    p[chapterId].cards[cardKey] = !!checked;
    saveProgress(p);
  }

  function isCardChecked(chapterId, cardKey) {
    const p = loadProgress();
    return !!(p[chapterId] && p[chapterId].cards && p[chapterId].cards[cardKey]);
  }

  function chapterProgress(chapterId, totalCards) {
    const p = loadProgress();
    const cards = (p[chapterId] && p[chapterId].cards) || {};
    const done = Object.values(cards).filter(Boolean).length;
    return { done, total: totalCards, pct: totalCards ? Math.round(done * 100 / totalCards) : 0 };
  }

  function overallProgress() {
    const p = loadProgress();
    let done = 0;
    let total = 0;
    CHAPTERS.forEach(ch => {
      const c = (p[ch.id] && p[ch.id].cards) || {};
      done += Object.values(c).filter(Boolean).length;
      total += ch.totalCards || 0; // populated by chapter HTML on load
    });
    return { done, total, pct: total ? Math.round(done * 100 / total) : 0 };
  }

  function exportRecord() {
    return {
      exportedAt: new Date().toISOString(),
      course: 'CAS 2026',
      progress: loadProgress(),
    };
  }

  return { STORAGE_KEY, CHAPTERS, loadProgress, saveProgress, setCardChecked, isCardChecked, chapterProgress, overallProgress, exportRecord };
})();

if (typeof window !== 'undefined') window.CAS2026 = CAS2026;
```

- [ ] **Step 2: Manually test in browser console**

Open any HTML in the repo (e.g. `index.html`) in browser, then in DevTools console:

```js
// Load the script:
const s = document.createElement('script');
s.src = 'cas-2026-shared.js';
document.head.appendChild(s);
// Wait, then:
CAS2026.setCardChecked('cas-01', 'card-1', true);
CAS2026.isCardChecked('cas-01', 'card-1');  // → true
CAS2026.chapterProgress('cas-01', 8);        // → { done: 1, total: 8, pct: 13 }
location.reload();
// After reload:
CAS2026.isCardChecked('cas-01', 'card-1');  // → true (persistence works)
```

Expected: All assertions pass, value persists across reload.

- [ ] **Step 3: Commit**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add cas-2026-shared.js
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "feat(cas-2026): add shared progress and metadata module"
```

---

### Task 2: Create chapter HTML template (cas-2026-01-ultrasound.html as canonical reference)

**Files:**
- Create: `cas-2026-01-ultrasound.html`

This task builds the **canonical chapter HTML** with placeholder content. Later tasks clone this for chapters 2-9 and fill real content. The template includes: sticky header with progress bar, speaker block, learning objectives, card list with checkbox + image slot, Quick Check (3 MCQs), chapter navigation.

- [ ] **Step 1: Create `cas-2026-01-ultrasound.html` with the full template structure**

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ch1 Ultrasound Diagnosis — CAS 2026</title>
<link rel="stylesheet" href="design-system.css">
<link rel="stylesheet" href="achievements-ui.css">
<style>
  body { font-family: "Noto Sans TC","Microsoft JhengHei",Arial,sans-serif; background:#f5f7fa; color:#2d3748; line-height:1.6; margin:0; padding:0; }
  .container { max-width:800px; margin:0 auto; padding:16px; }

  .sticky-header { position:sticky; top:0; background:linear-gradient(135deg,#1a365d,#2b6cb0); color:#fff; padding:12px 16px; z-index:100; box-shadow:0 2px 8px rgba(0,0,0,.15); }
  .sticky-header .row { display:flex; align-items:center; gap:12px; }
  .back-btn { color:#fff; text-decoration:none; font-size:14px; }
  .chapter-title { font-size:1.05rem; font-weight:600; flex:1; }
  .progress-line { margin-top:8px; font-size:.85rem; opacity:.9; display:flex; align-items:center; gap:8px; }
  .progress-bar { flex:1; height:6px; background:rgba(255,255,255,.25); border-radius:3px; overflow:hidden; }
  .progress-bar-fill { height:100%; background:#48bb78; transition:width .3s; width:0%; }

  .speaker-block, .objectives-block { background:#fff; border-radius:10px; padding:16px 20px; margin-top:16px; box-shadow:0 1px 4px rgba(0,0,0,.08); }
  .speaker-block h3, .objectives-block h3 { font-size:.95rem; color:#1a365d; margin:0 0 8px 0; }
  .objectives-block ul { margin:0; padding-left:20px; }
  .objectives-block li { margin-bottom:4px; }

  .card { background:#fff; border-radius:10px; margin-top:16px; box-shadow:0 1px 4px rgba(0,0,0,.08); overflow:hidden; }
  .card-header { display:flex; align-items:flex-start; gap:12px; padding:16px 20px; }
  .card-title { flex:1; font-weight:600; font-size:1rem; color:#1a365d; }
  .card-check { width:24px; height:24px; accent-color:#38a169; cursor:pointer; min-width:24px; min-height:24px; }
  .card-img { width:100%; display:block; }
  .card-img-wrap { background:#f7fafc; }
  .card-body { padding:12px 20px 16px 20px; font-size:.95rem; color:#4a5568; }
  .card-tip { margin-top:8px; padding:10px 12px; background:#ebf8ff; border-left:4px solid #3182ce; border-radius:4px; font-size:.88rem; }
  .card-source { margin-top:8px; font-size:.75rem; color:#718096; }

  .quiz-block { background:#fff; border-radius:10px; padding:20px; margin-top:24px; box-shadow:0 1px 4px rgba(0,0,0,.08); }
  .quiz-block h3 { color:#1a365d; margin-bottom:12px; }
  .quiz-question { margin-bottom:20px; }
  .quiz-options label { display:block; padding:10px 12px; margin:6px 0; background:#f7fafc; border-radius:6px; cursor:pointer; transition:background .2s; }
  .quiz-options label:hover { background:#edf2f7; }
  .quiz-options input { margin-right:8px; }
  .quiz-options label.correct { background:#c6f6d5; }
  .quiz-options label.incorrect { background:#fed7d7; }
  .quiz-explain { margin-top:8px; padding:8px 12px; background:#fffaf0; border-left:4px solid #dd6b20; border-radius:4px; font-size:.88rem; display:none; }

  .nav-bar { display:flex; justify-content:space-between; margin-top:24px; gap:12px; }
  .nav-btn { flex:1; padding:12px; background:#2b6cb0; color:#fff; text-align:center; border-radius:8px; text-decoration:none; font-weight:600; }
  .nav-btn.disabled { background:#cbd5e0; pointer-events:none; }
  .nav-btn.hub { background:#1a365d; }

  .footer { margin-top:24px; padding:16px; font-size:.75rem; color:#718096; text-align:center; }
</style>
</head>
<body data-chapter="cas-01" data-chapter-no="1">

<div class="sticky-header">
  <div class="row">
    <a href="cas-2026-hub.html" class="back-btn">← 回 Hub</a>
    <div class="chapter-title">Ch1 · Ultrasound Diagnosis of Carotid Artery Stenosis</div>
  </div>
  <div class="progress-line">
    📊 <span id="progress-text">0 / 0</span>
    <div class="progress-bar"><div class="progress-bar-fill" id="progress-fill"></div></div>
    <span id="progress-pct">0%</span>
  </div>
</div>

<div class="container">

  <div class="speaker-block">
    <h3>📚 講師</h3>
    <div>湯頌君醫師 (2022) / 葉馨喬醫師 (2024)</div>
  </div>

  <div class="objectives-block">
    <h3>🎯 學習目標</h3>
    <ul>
      <li>(placeholder) 認識頸動脈狹窄超音波測量標準</li>
      <li>(placeholder) 區別 PSV / EDV / ICA-CCA ratio 之臨床意義</li>
      <li>(placeholder) 辨識 plaque morphology 與 vulnerability 特徵</li>
    </ul>
  </div>

  <div id="cards-container">
    <!-- Cards will be inserted here; this template uses inline cards (no JS render). -->
    <div class="card" data-card-key="card-1">
      <div class="card-header">
        <div class="card-title">1. (placeholder) PSV 測量基準</div>
        <input type="checkbox" class="card-check" aria-label="我懂了">
      </div>
      <div class="card-img-wrap"><img class="card-img" src="" alt="placeholder slide" style="display:none"></div>
      <div class="card-body">
        (placeholder) 重點解說 1-3 句。
        <div class="card-tip">💡 Tip: (placeholder) 探頭角度應 ≤ 60 度。</div>
        <div class="card-source">📌 來源：湯頌君醫師 2022 / 中華民國心臟學會 CAS 訓練課程 / slide #—</div>
      </div>
    </div>
  </div>

  <div class="quiz-block">
    <h3>🧠 Quick Check</h3>
    <div class="quiz-question" data-q="1">
      <div><strong>Q1.</strong> (placeholder question)</div>
      <div class="quiz-options">
        <label><input type="radio" name="q1" value="A"> A. (placeholder)</label>
        <label><input type="radio" name="q1" value="B" data-correct="true"> B. (placeholder, correct)</label>
        <label><input type="radio" name="q1" value="C"> C. (placeholder)</label>
        <label><input type="radio" name="q1" value="D"> D. (placeholder)</label>
      </div>
      <div class="quiz-explain">(placeholder explanation)</div>
    </div>
  </div>

  <div class="nav-bar">
    <a class="nav-btn disabled">← 上一章</a>
    <a class="nav-btn hub" href="cas-2026-hub.html">🏠 Hub</a>
    <a class="nav-btn" href="cas-2026-02-ct-mr.html">下一章 Ch2 →</a>
  </div>

  <div class="footer">
    本教學資源圖片來源為各講師於歷年「頸動脈支架訓練課程」之授課投影片，僅供本課程學員學術教育使用。
  </div>

</div>

<script src="cas-2026-shared.js"></script>
<script src="achievements.js"></script>
<script>
  // Placeholder; full interaction wired in Task 3 & 4.
  document.addEventListener('DOMContentLoaded', () => {
    console.log('[cas-01] loaded; chapter id =', document.body.dataset.chapter);
  });
</script>

</body>
</html>
```

- [ ] **Step 2: Open in browser to verify layout**

Open `file:///G:/我的雲端硬碟/004%20教學資料%20at%20Hsinchu%20院內/Teaching%20materials%20CV%20education%20web%20at%20github/saq-questionnaire-main/cas-2026-01-ultrasound.html` (or via local server) in Chrome with DevTools mobile viewport (375 × 812).

Expected: Header stays sticky on scroll. Card, quiz block, nav bar all render. No console errors except (acceptable) 404 for empty `<img src="">` — fixed in Task 7.

- [ ] **Step 3: Commit**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add cas-2026-01-ultrasound.html
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "feat(cas-2026): add Ch1 template with placeholder content"
```

---

### Task 3: Wire chapter interactivity (checkbox + progress + quiz feedback) into the template

**Files:**
- Modify: `cas-2026-01-ultrasound.html` (replace placeholder `<script>` at bottom)

- [ ] **Step 1: Replace the bottom `<script>` block in `cas-2026-01-ultrasound.html`**

Replace the existing `<script>` (the one that says "Placeholder; full interaction wired in Task 3 & 4") with:

```html
<script>
(function () {
  const chapterId = document.body.dataset.chapter;
  const cards = document.querySelectorAll('.card');
  const totalCards = cards.length;
  const progressText = document.getElementById('progress-text');
  const progressFill = document.getElementById('progress-fill');
  const progressPct  = document.getElementById('progress-pct');

  // Register total card count for hub.
  const stored = CAS2026.loadProgress();
  stored[chapterId] = stored[chapterId] || { cards:{}, quiz:{}, completed:false };
  stored[chapterId].totalCards = totalCards;
  CAS2026.saveProgress(stored);

  function refreshProgress() {
    const p = CAS2026.chapterProgress(chapterId, totalCards);
    progressText.textContent = `${p.done} / ${p.total}`;
    progressFill.style.width = p.pct + '%';
    progressPct.textContent = p.pct + '%';
  }

  // Wire each card's checkbox.
  cards.forEach(card => {
    const key = card.dataset.cardKey;
    const cb  = card.querySelector('.card-check');
    cb.checked = CAS2026.isCardChecked(chapterId, key);
    cb.addEventListener('change', () => {
      CAS2026.setCardChecked(chapterId, key, cb.checked);
      refreshProgress();
    });
  });

  refreshProgress();

  // Wire quiz radio buttons for instant feedback.
  document.querySelectorAll('.quiz-question').forEach(q => {
    const explain = q.querySelector('.quiz-explain');
    q.querySelectorAll('input[type=radio]').forEach(r => {
      r.addEventListener('change', () => {
        q.querySelectorAll('.quiz-options label').forEach(l => l.classList.remove('correct','incorrect'));
        const selected = q.querySelector('input[type=radio]:checked');
        const label = selected.closest('label');
        const isCorrect = selected.dataset.correct === 'true';
        label.classList.add(isCorrect ? 'correct' : 'incorrect');
        if (!isCorrect) {
          // Highlight correct answer too:
          const correctInput = q.querySelector('input[data-correct="true"]');
          if (correctInput) correctInput.closest('label').classList.add('correct');
        }
        explain.style.display = 'block';

        // Record quiz answer.
        const p = CAS2026.loadProgress();
        const qnum = q.dataset.q;
        p[chapterId] = p[chapterId] || { cards:{}, quiz:{}, completed:false };
        p[chapterId].quiz[qnum] = { value: selected.value, correct: isCorrect };
        // Mark completed if ≥ 2 quiz answers correct.
        const quizEntries = Object.values(p[chapterId].quiz);
        const correctCount = quizEntries.filter(e => e.correct).length;
        if (correctCount >= 2) {
          p[chapterId].completed = true;
          if (window.Achievements && typeof Achievements.unlock === 'function') {
            Achievements.unlock(`cas-2026-${chapterId}-complete`);
          }
        }
        CAS2026.saveProgress(p);
      });
    });
  });
})();
</script>
```

- [ ] **Step 2: Verify in browser**

Open the chapter HTML, open DevTools console. Then:

```js
// Tick the card checkbox in UI → progress should update "0 / 1" → "1 / 1" (0% → 100%)
// Click an incorrect quiz answer → red highlight, explanation shows, correct answer goes green
// Reload page → checkbox state and quiz answer should NOT persist for quiz (by design)
// But card checkbox state SHOULD persist.
CAS2026.loadProgress();
// → { 'cas-01': { cards: {'card-1': true}, quiz: {'1': {...}}, totalCards: 1, completed: false } }
```

Expected: card check state persists across reload; progress bar updates; quiz gives instant feedback. Console has no errors.

- [ ] **Step 3: Commit**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add cas-2026-01-ultrasound.html
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "feat(cas-2026): wire chapter checkbox/progress/quiz interactions"
```

---

## Phase B — Image Extraction Pipeline

### Task 4: Create Python pipeline scaffolding and dependency check

**Files:**
- Create: `tools/cas-2026-pipeline/requirements.txt`
- Create: `tools/cas-2026-pipeline/check_env.py`

- [ ] **Step 1: Create `tools/cas-2026-pipeline/requirements.txt`**

```
PyMuPDF==1.24.10
pywin32==306; sys_platform == "win32"
Jinja2==3.1.4
```

- [ ] **Step 2: Create `tools/cas-2026-pipeline/check_env.py`**

```python
"""Verify required dependencies for the CAS 2026 image pipeline."""
import sys
import importlib

REQUIRED = ['fitz', 'jinja2']
if sys.platform == 'win32':
    REQUIRED.append('win32com.client')

def main():
    missing = []
    for mod in REQUIRED:
        try:
            importlib.import_module(mod)
            print(f'  OK   {mod}')
        except ImportError:
            print(f'  FAIL {mod}')
            missing.append(mod)

    if missing:
        print(f'\nMissing modules: {missing}')
        print('Install with: pip install -r tools/cas-2026-pipeline/requirements.txt')
        sys.exit(1)

    if sys.platform == 'win32':
        try:
            import win32com.client
            ppt = win32com.client.Dispatch('PowerPoint.Application')
            print('  OK   PowerPoint COM dispatch')
            ppt.Quit()
        except Exception as e:
            print(f'  FAIL PowerPoint COM: {e}')
            sys.exit(1)

    print('\nAll dependencies OK.')

if __name__ == '__main__':
    main()
```

- [ ] **Step 3: Install and run env check**

```powershell
pip install -r "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main\tools\cas-2026-pipeline\requirements.txt"
python "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main\tools\cas-2026-pipeline\check_env.py"
```

Expected output:
```
  OK   fitz
  OK   jinja2
  OK   win32com.client
  OK   PowerPoint COM dispatch

All dependencies OK.
```

If PowerPoint COM fails: ensure Microsoft Office is installed on this Windows machine.

- [ ] **Step 4: Commit**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add tools/cas-2026-pipeline/
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "build(cas-2026): pipeline scaffolding and env check"
```

---

### Task 5: Implement slide extraction (ppt-family → PDF → PNG)

**Files:**
- Create: `tools/cas-2026-pipeline/extract_slides.py`
- Create: `tools/cas-2026-pipeline/test_extract_slides.py`

- [ ] **Step 1: Write the failing test**

```python
# tools/cas-2026-pipeline/test_extract_slides.py
"""Tests for slide extraction.

Note: These tests require sample input files. The "smoke test" uses an actual
2022 source file to verify end-to-end behavior.
"""
import os
import shutil
import tempfile
import unittest
from pathlib import Path

import extract_slides as es

SOURCE_DIR = Path(r"G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Carotid 頸動脈支架訓練課程歷年投影片 2026")
SAMPLE_PPTX = SOURCE_DIR / "2022年_05_黃成偉醫師_Embolic protection device.pptx"
SAMPLE_PDF  = SOURCE_DIR / "2024年_06_黃成偉醫師_Embolic protection device.pdf"

class TestExtract(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='cas2026_test_'))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_extract_pptx_produces_pngs(self):
        if not SAMPLE_PPTX.exists():
            self.skipTest(f'Sample missing: {SAMPLE_PPTX}')
        out = es.extract(SAMPLE_PPTX, self.tmp, dpi=150)  # lower DPI for test speed
        self.assertGreater(len(out), 0, 'no PNGs produced')
        for p in out:
            self.assertTrue(p.exists())
            self.assertEqual(p.suffix, '.png')
            self.assertGreater(p.stat().st_size, 1000, f'tiny file: {p}')

    def test_extract_pdf_produces_pngs(self):
        if not SAMPLE_PDF.exists():
            self.skipTest(f'Sample missing: {SAMPLE_PDF}')
        out = es.extract(SAMPLE_PDF, self.tmp, dpi=150)
        self.assertGreater(len(out), 0)

if __name__ == '__main__':
    unittest.main()
```

- [ ] **Step 2: Run test, expect failure (module not found)**

```powershell
cd "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main\tools\cas-2026-pipeline"
python -m unittest test_extract_slides.py -v
```

Expected: `ModuleNotFoundError: No module named 'extract_slides'`

- [ ] **Step 3: Create `extract_slides.py`**

```python
"""Extract slides from PowerPoint / PDF source files into per-page PNGs.

Pipeline:
  .ppt / .pptx / .pptm  --(PowerPoint COM SaveAs PDF)-->  .pdf  --(PyMuPDF)-->  .png pages
  .pdf                                                       --(PyMuPDF)-->  .png pages

Usage (CLI):
  python extract_slides.py <input_file> <output_dir> [--dpi 300]
"""
from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

import fitz  # PyMuPDF

PPT_EXTS = {'.ppt', '.pptx', '.pptm'}
PDF_EXTS = {'.pdf'}

def _ppt_to_pdf(src: Path, tmp_dir: Path) -> Path:
    """Convert a PowerPoint-family file to PDF via PowerPoint COM on Windows."""
    if sys.platform != 'win32':
        raise RuntimeError('PowerPoint COM only supported on Windows. '
                           'For non-Windows, install LibreOffice and switch to soffice.')
    import win32com.client
    out = tmp_dir / (src.stem + '.pdf')
    ppt_app = win32com.client.Dispatch('PowerPoint.Application')
    # Note: Some PowerPoint installs require Visible=True.
    try:
        pres = ppt_app.Presentations.Open(str(src.resolve()), WithWindow=False)
        # 32 = ppSaveAsPDF in PowerPoint FileFormat enum
        pres.SaveAs(str(out.resolve()), 32)
        pres.Close()
    finally:
        ppt_app.Quit()
    return out

def _pdf_to_pngs(pdf_path: Path, out_dir: Path, dpi: int = 300) -> list[Path]:
    """Render each PDF page to a PNG in out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf_path))
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    paths: list[Path] = []
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        out_file = out_dir / f'slide-{i:03d}.png'
        pix.save(str(out_file))
        paths.append(out_file)
    doc.close()
    return paths

def extract(src: Path, out_dir: Path, dpi: int = 300) -> list[Path]:
    """Extract slides from `src` (ppt-family or pdf) to `out_dir`.

    Returns sorted list of generated PNG paths.
    """
    src = Path(src)
    out_dir = Path(out_dir)
    suffix = src.suffix.lower()
    if suffix in PPT_EXTS:
        with tempfile.TemporaryDirectory() as td:
            pdf = _ppt_to_pdf(src, Path(td))
            return _pdf_to_pngs(pdf, out_dir, dpi=dpi)
    if suffix in PDF_EXTS:
        return _pdf_to_pngs(src, out_dir, dpi=dpi)
    raise ValueError(f'Unsupported file type: {suffix}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output_dir')
    parser.add_argument('--dpi', type=int, default=300)
    args = parser.parse_args()
    paths = extract(Path(args.input), Path(args.output_dir), dpi=args.dpi)
    print(f'Extracted {len(paths)} pages.')
    for p in paths:
        print(' ', p)

if __name__ == '__main__':
    main()
```

- [ ] **Step 4: Run tests, expect pass**

```powershell
cd "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main\tools\cas-2026-pipeline"
python -m unittest test_extract_slides.py -v
```

Expected: 2 tests pass (or 2 skipped if sample files missing — fail otherwise). Each .pptx → .pdf → .png pipeline cycle completes in 30-90 seconds depending on slide count.

- [ ] **Step 5: Commit**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add tools/cas-2026-pipeline/extract_slides.py tools/cas-2026-pipeline/test_extract_slides.py
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "feat(cas-2026): slide extraction script (ppt→pdf→png)"
```

---

### Task 6: Sidecar overview HTML generator + batch runner

**Files:**
- Create: `tools/cas-2026-pipeline/sidecar_template.html.j2`
- Create: `tools/cas-2026-pipeline/generate_sidecar.py`
- Create: `tools/cas-2026-pipeline/chapter_sources.json`
- Create: `tools/cas-2026-pipeline/run_pipeline.py`

- [ ] **Step 1: Create `tools/cas-2026-pipeline/chapter_sources.json`** — declarative mapping of chapters to source files

```json
{
  "01-ultrasound": [
    { "year": 2022, "speaker": "湯頌君", "slug": "tang-sj", "file": "2022年_01_湯頌君醫師_Ultrasound Diagnosis of Carotid Artery Stenosis.ppt" },
    { "year": 2024, "speaker": "葉馨喬", "slug": "yeh-hc", "file": "2024年_01_葉馨喬醫師_Ultrasound Diagnosis of Carotid Artery Stenosis.ppt" }
  ],
  "02-ct-mr": [
    { "year": 2022, "speaker": "李崇維", "slug": "lee-cw", "file": "2022年_02_李崇維醫師_ICAS CT MR.pptx" }
  ],
  "03-occlusion": [
    { "year": 2022, "speaker": "黃國川", "slug": "huang-kc", "file": "2022年_03_黃國川醫師_Carotid stenosis occlusion.pptx" }
  ],
  "04-techniques": [
    { "year": 2022, "speaker": "蘇峻弘", "slug": "su-ch", "file": "2022年_04_蘇峻弘醫師_General interventional techniques of carotid stenting.pptx" }
  ],
  "05-epd": [
    { "year": 2022, "speaker": "黃成偉", "slug": "huang-cw", "file": "2022年_05_黃成偉醫師_Embolic protection device.pptx" },
    { "year": 2024, "speaker": "黃成偉", "slug": "huang-cw", "file": "2024年_06_黃成偉醫師_Embolic protection device.pdf" }
  ],
  "06-stent-design": [
    { "year": 2022, "speaker": "蔡翰林", "slug": "tsai-hl-ttt", "file": "2022年_06_蔡翰林醫師_TTT carotid stent.pptm" },
    { "year": 2024, "speaker": "蔡翰林", "slug": "tsai-hl-stent", "file": "2024年_07_蔡翰林醫師_Stent design.pdf" }
  ],
  "07-tsci": [
    { "year": 2022, "speaker": "柯呈諭", "slug": "ko-cy", "file": "2022年_07_柯呈諭醫師_Carotid TSCI.pptx" },
    { "year": 2024, "speaker": "柯呈諭", "slug": "ko-cy", "file": "2024年_04_柯呈諭醫師_Carotid TSCI.pptx" }
  ],
  "08-surgical": [
    { "year": 2024, "speaker": "黃致遠", "slug": "huang-cy", "file": "2024年_05_黃致遠醫師_Surgical approaches for carotid artery disease.pdf" }
  ],
  "09-difficult": [
    { "year": 2024, "speaker": "方修御", "slug": "fang-hy", "file": "2024年_08_方修御醫師_Difficult carotid artery stenting tips and tricks.pptx" }
  ]
}
```

- [ ] **Step 2: Create `tools/cas-2026-pipeline/sidecar_template.html.j2`**

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Slides Overview — {{ chapter_title }}</title>
<style>
  body { font-family: "Noto Sans TC","Microsoft JhengHei",Arial,sans-serif; background:#f5f7fa; margin:0; padding:16px; }
  h1 { color:#1a365d; }
  .source-block { background:#fff; border-radius:8px; padding:16px; margin-bottom:24px; box-shadow:0 1px 4px rgba(0,0,0,.08); }
  .source-block h2 { margin-top:0; color:#2b6cb0; font-size:1.05rem; }
  .slides-grid { display:grid; grid-template-columns:repeat(auto-fill, minmax(160px,1fr)); gap:12px; }
  .slide { border:2px solid #e2e8f0; border-radius:6px; padding:6px; cursor:pointer; transition:all .15s; background:#fff; }
  .slide.selected { border-color:#38a169; background:#f0fff4; }
  .slide img { width:100%; display:block; border-radius:4px; }
  .slide .meta { font-size:.75rem; text-align:center; color:#4a5568; margin-top:4px; }
  .slide .meta strong { color:#1a365d; }
  .actions { position:sticky; bottom:0; background:#fff; padding:12px; border-top:1px solid #e2e8f0; display:flex; gap:12px; align-items:center; }
  button { padding:10px 16px; background:#2b6cb0; color:#fff; border:none; border-radius:6px; cursor:pointer; font-size:.95rem; font-weight:600; }
  button:hover { background:#1a365d; }
  .counter { font-size:.95rem; color:#4a5568; flex:1; }
  pre.json-output { background:#1a202c; color:#e2e8f0; padding:12px; border-radius:6px; max-height:300px; overflow:auto; font-size:.85rem; }
</style>
</head>
<body data-chapter="{{ chapter_id }}">

<h1>📚 {{ chapter_title }} — Slides Overview</h1>
<p>點擊投影片縮圖選為「採用」（綠框）。完成後按右下 <strong>匯出 JSON</strong>。</p>

{% for src in sources %}
<div class="source-block" data-source-key="{{ src.year }}-{{ src.slug }}">
  <h2>{{ src.year }} {{ src.speaker }}醫師（{{ src.slides|length }} slides）</h2>
  <div class="slides-grid">
    {% for slide in src.slides %}
    <div class="slide" data-seq="{{ slide.seq }}" data-rel-path="{{ slide.rel_path }}">
      <img src="{{ slide.rel_path }}" loading="lazy">
      <div class="meta">slide #<strong>{{ slide.seq }}</strong></div>
    </div>
    {% endfor %}
  </div>
</div>
{% endfor %}

<div class="actions">
  <span class="counter">已選 <strong id="count">0</strong> 張</span>
  <button id="copy-json">📋 複製 JSON</button>
  <button id="download-json">⬇ 下載 JSON</button>
</div>

<pre id="json-output" class="json-output" style="display:none;"></pre>

<script>
const chapterId = document.body.dataset.chapter;

// Restore selection from localStorage on load.
const STORAGE_KEY = 'cas-2026-slide-selection:' + chapterId;
const stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
const storedSet = new Set(stored.map(s => `${s.source}|${s.seq}`));

document.querySelectorAll('.slide').forEach(el => {
  const sourceKey = el.closest('.source-block').dataset.sourceKey;
  const seq = el.dataset.seq;
  if (storedSet.has(`${sourceKey}|${seq}`)) el.classList.add('selected');
  el.addEventListener('click', () => {
    el.classList.toggle('selected');
    updateCount();
  });
});

function collectSelected() {
  const out = [];
  document.querySelectorAll('.slide.selected').forEach(el => {
    out.push({
      source: el.closest('.source-block').dataset.sourceKey,
      seq: parseInt(el.dataset.seq, 10),
      relPath: el.dataset.relPath,
    });
  });
  return out;
}

function updateCount() {
  const sel = collectSelected();
  document.getElementById('count').textContent = sel.length;
  localStorage.setItem(STORAGE_KEY, JSON.stringify(sel));
}
updateCount();

document.getElementById('copy-json').addEventListener('click', async () => {
  const data = { chapter: chapterId, selected: collectSelected() };
  await navigator.clipboard.writeText(JSON.stringify(data, null, 2));
  alert('JSON 已複製到剪貼簿');
});

document.getElementById('download-json').addEventListener('click', () => {
  const data = { chapter: chapterId, selected: collectSelected() };
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `cas-2026-${chapterId}-selection.json`;
  a.click();
  URL.revokeObjectURL(url);
});
</script>

</body>
</html>
```

- [ ] **Step 3: Create `tools/cas-2026-pipeline/generate_sidecar.py`**

```python
"""Generate sidecar slide-overview HTMLs (one per chapter) for user review."""
from __future__ import annotations

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

CHAPTER_TITLES = {
    '01-ultrasound':  'Ch1 Ultrasound Diagnosis',
    '02-ct-mr':       'Ch2 CT / MR for ICAS',
    '03-occlusion':   'Ch3 Stenosis & Occlusion',
    '04-techniques':  'Ch4 General CAS Techniques',
    '05-epd':         'Ch5 Embolic Protection Device',
    '06-stent-design':'Ch6 Stent Design & TTT',
    '07-tsci':        'Ch7 Carotid TSCI',
    '08-surgical':    'Ch8 Surgical Approaches',
    '09-difficult':   'Ch9 Difficult CAS Tips & Tricks',
}

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SIDECAR_DIR = REPO_ROOT / 'docs' / 'cas-2026'
EXTRACTED_ROOT = SIDECAR_DIR  # PNGs live under docs/cas-2026/<chapter>/<year>-<slug>/

def list_slides(folder: Path):
    if not folder.exists():
        return []
    pngs = sorted(folder.glob('slide-*.png'))
    return [
        {
            'seq': int(p.stem.split('-')[1]),
            'rel_path': p.relative_to(SIDECAR_DIR).as_posix(),
        }
        for p in pngs
    ]

def generate_for_chapter(chapter_id: str, sources_meta: list[dict]) -> Path:
    env = Environment(loader=FileSystemLoader(Path(__file__).parent), autoescape=True)
    tmpl = env.get_template('sidecar_template.html.j2')

    sources = []
    for s in sources_meta:
        folder = SIDECAR_DIR / chapter_id / f'{s["year"]}-{s["slug"]}'
        slides = list_slides(folder)
        sources.append({
            'year': s['year'],
            'speaker': s['speaker'],
            'slug': s['slug'],
            'slides': slides,
        })

    out_path = SIDECAR_DIR / f'{chapter_id}-slides-overview.html'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        tmpl.render(
            chapter_id=chapter_id,
            chapter_title=CHAPTER_TITLES[chapter_id],
            sources=sources,
        ),
        encoding='utf-8',
    )
    return out_path

def main():
    sources_path = Path(__file__).parent / 'chapter_sources.json'
    chapter_sources = json.loads(sources_path.read_text(encoding='utf-8'))
    for chapter_id, sources_meta in chapter_sources.items():
        out = generate_for_chapter(chapter_id, sources_meta)
        print(f'  Generated {out.name} ({sum(len(list_slides(SIDECAR_DIR / chapter_id / f"{s["year"]}-{s["slug"]}")) ) for s in sources_meta} slides)')

if __name__ == '__main__':
    main()
```

- [ ] **Step 4: Create `tools/cas-2026-pipeline/run_pipeline.py`** — the batch runner that does extraction then sidecar generation

```python
"""Run the full image extraction + sidecar generation pipeline for all 9 chapters."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import extract_slides
import generate_sidecar

SOURCE_DIR = Path(r"G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Carotid 頸動脈支架訓練課程歷年投影片 2026")
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SIDECAR_DIR = REPO_ROOT / 'docs' / 'cas-2026'

def main(dpi: int = 200):
    sources_path = Path(__file__).parent / 'chapter_sources.json'
    chapter_sources = json.loads(sources_path.read_text(encoding='utf-8'))

    for chapter_id, sources_meta in chapter_sources.items():
        print(f'\n=== {chapter_id} ===')
        for s in sources_meta:
            src_file = SOURCE_DIR / s['file']
            out_dir  = SIDECAR_DIR / chapter_id / f'{s["year"]}-{s["slug"]}'
            if not src_file.exists():
                print(f'  SKIP missing source: {src_file.name}')
                continue
            if out_dir.exists() and any(out_dir.glob('slide-*.png')):
                print(f'  SKIP already extracted: {out_dir.name}')
                continue
            print(f'  Extracting {src_file.name} → {out_dir.name}')
            paths = extract_slides.extract(src_file, out_dir, dpi=dpi)
            print(f'    {len(paths)} slides')

    print('\n--- Generating sidecar HTMLs ---')
    generate_sidecar.main()

if __name__ == '__main__':
    dpi = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    main(dpi=dpi)
```

- [ ] **Step 5: Run the pipeline end-to-end (this is the actual extraction)**

```powershell
cd "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main\tools\cas-2026-pipeline"
python run_pipeline.py 200
```

Expected: 9 chapter folders created under `docs/cas-2026/`, each with sub-folders per source, each containing `slide-001.png … slide-NNN.png`. Then 9 sidecar HTMLs created at `docs/cas-2026/<chapter>-slides-overview.html`. Total wall time: 5-15 minutes depending on PowerPoint startup overhead.

If a source file fails to extract, note the failure and continue. Re-run with that file removed from `chapter_sources.json` if necessary.

- [ ] **Step 6: Spot-check sidecar HTMLs in browser**

Open `docs/cas-2026/05-epd-slides-overview.html` (Ch5 has both years, good test) in browser. Verify:
- All thumbnails render
- Clicking a thumbnail toggles green border
- Counter increments
- "下載 JSON" produces a JSON file

- [ ] **Step 7: Commit pipeline code (NOT the extracted PNGs — they go in `.gitignore`)**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add tools/cas-2026-pipeline/
echo "docs/cas-2026/*/" >> "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main/.gitignore"
echo "!docs/cas-2026/*-slides-overview.html" >> "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main/.gitignore"
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add .gitignore
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add docs/cas-2026/*.html
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "feat(cas-2026): batch pipeline, sidecar generator, 9 review pages"
```

---

## Phase C — User Review Checkpoint

### CHECKPOINT: User reviews sidecar HTMLs and exports selection JSONs

This phase has **no Claude work**. The user:

1. Opens each `docs/cas-2026/NN-<topic>-slides-overview.html` in browser (desktop or phone)
2. Clicks thumbnails to mark "use" (target ~5-8 slides per chapter)
3. Clicks "⬇ 下載 JSON" to save selection
4. Places downloaded JSON files into `tools/cas-2026-pipeline/selections/` directory

Output: 9 files named `cas-2026-01-ultrasound-selection.json` … `cas-2026-09-difficult-selection.json`.

Expected user time: 30-45 minutes total.

**Claude does not proceed past this checkpoint until selections are present.**

---

## Phase D — Content Population

### Task 7: Process selection JSONs and copy chosen PNGs to images-cas-2026/

**Files:**
- Create: `tools/cas-2026-pipeline/process_selections.py`

- [ ] **Step 1: Create `tools/cas-2026-pipeline/process_selections.py`**

```python
"""Read user-exported selection JSONs and copy chosen PNGs to images-cas-2026/."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SIDECAR_DIR = REPO_ROOT / 'docs' / 'cas-2026'
IMAGES_ROOT = REPO_ROOT / 'images-cas-2026'
SELECTIONS_DIR = Path(__file__).parent / 'selections'

def process_one(selection_file: Path):
    data = json.loads(selection_file.read_text(encoding='utf-8'))
    chapter_id = data['chapter']  # e.g. '05-epd'
    chapter_imgs = IMAGES_ROOT / chapter_id
    chapter_imgs.mkdir(parents=True, exist_ok=True)
    copied = []
    for entry in data['selected']:
        source = entry['source']      # e.g. '2022-huang-cw'
        seq = entry['seq']            # int
        src_png = SIDECAR_DIR / chapter_id / source / f'slide-{seq:03d}.png'
        if not src_png.exists():
            print(f'  MISSING {src_png}')
            continue
        dst_png = chapter_imgs / f'{source}-seq{seq:03d}.png'
        shutil.copy2(src_png, dst_png)
        copied.append(dst_png)
    print(f'  {chapter_id}: copied {len(copied)} images')
    return copied

def main():
    if not SELECTIONS_DIR.exists():
        raise SystemExit(f'No selections directory: {SELECTIONS_DIR}')
    sel_files = sorted(SELECTIONS_DIR.glob('cas-2026-*-selection.json'))
    if not sel_files:
        raise SystemExit('No selection JSON files found.')
    for sf in sel_files:
        print(f'Processing {sf.name}')
        process_one(sf)

if __name__ == '__main__':
    main()
```

- [ ] **Step 2: Run it (assumes user has placed JSONs in selections/)**

```powershell
cd "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main\tools\cas-2026-pipeline"
python process_selections.py
```

Expected: For each chapter, prints "copied N images". After running, `images-cas-2026/NN-<topic>/` folders contain renamed PNGs (e.g. `2022-huang-cw-seq012.png`).

- [ ] **Step 3: Verify by listing**

```powershell
ls "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main\images-cas-2026\05-epd\"
```

Expected: PNGs visible with naming `<year>-<slug>-seq<NNN>.png`.

- [ ] **Step 4: Commit the script and the images**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add tools/cas-2026-pipeline/process_selections.py images-cas-2026/
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "feat(cas-2026): selection processor and chapter images"
```

---

### Task 8: Build the 9 chapter HTMLs from the template (one task; iterate over chapters)

This is a content-population task. For each chapter, Claude:

1. **Reads selected PNGs** in `images-cas-2026/NN-<topic>/`
2. **Drafts card content** from the slides (titles, 1-3-sentence key point, optional tip)
3. **Drafts 3 MCQ questions** that test the chapter's core concepts
4. **Clones the template** (`cas-2026-01-ultrasound.html`) to `cas-2026-NN-<topic>.html`
5. **Fills**: header title, `data-chapter` / `data-chapter-no`, speaker block, objectives, card list, quiz, prev/next nav

**Iteration order:** 01 → 02 → 03 → … → 09 (so Ch1 keeps its title; Ch9's "next chapter" points back to hub).

**Files (created one per chapter):**
- Modify: `cas-2026-01-ultrasound.html` (replace placeholder content with real content)
- Create: `cas-2026-02-ct-mr.html` … `cas-2026-09-difficult.html`

- [ ] **Step 1: For Chapter 01 (Ultrasound), gather inputs**

List the images:
```powershell
ls "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main\images-cas-2026\01-ultrasound\"
```

Read each PNG visually (use Read tool on a PNG to view via Claude's multimodal vision). Identify what concept each illustrates.

- [ ] **Step 2: Draft Chapter 01 content**

For each image, decide:
- Card title (≤ 30 chars, e.g., "PSV 測量基準")
- Key point body (1-3 sentences)
- Optional Tip box (clinical pearl)
- Image source line (year, speaker, slide #)

Draft 3 MCQs:
- Each has 4 options with exactly one marked `data-correct="true"`
- Each has a short explanation
- Questions should test core concepts, not trivia

Drafting heuristic: cover the chapter's learning objectives — if a card doesn't relate to an objective, drop it; if an objective has no card, add one.

- [ ] **Step 3: Replace placeholder content in `cas-2026-01-ultrasound.html`**

Replace these placeholder blocks with drafted content:
- `.objectives-block ul` — real bullets
- `#cards-container` — N real `.card` divs, each with `data-card-key="card-N"`, real title, real image `<img>` (no `display:none`), real body
- `.quiz-block` — 3 real `.quiz-question` divs, each with q-num, options, explanation
- Sticky header title (keep "Ch1 · Ultrasound Diagnosis of Carotid Artery Stenosis")
- Speaker block (already correct)
- Nav bar: prev disabled, next → Ch2

Card example with real image (replace placeholder):

```html
<div class="card" data-card-key="card-1">
  <div class="card-header">
    <div class="card-title">1. PSV 測量基準</div>
    <input type="checkbox" class="card-check" aria-label="我懂了">
  </div>
  <div class="card-img-wrap">
    <img class="card-img" src="images-cas-2026/01-ultrasound/2022-tang-sj-seq012.png" alt="PSV measurement criteria">
  </div>
  <div class="card-body">
    PSV (peak systolic velocity) ≥ 125 cm/s 代表 ≥ 50% 內頸動脈狹窄；≥ 230 cm/s 代表 ≥ 70%。
    <div class="card-tip">💡 Tip: 測量時探頭與血流夾角應 ≤ 60 度以避免高估。</div>
    <div class="card-source">📌 來源：湯頌君醫師 2022 / 中華民國心臟學會 CAS 訓練課程 / slide #12</div>
  </div>
</div>
```

- [ ] **Step 4: Verify Ch01 in browser**

Open `cas-2026-01-ultrasound.html` in mobile viewport (375×812). Verify:
- All images load (no broken icons)
- Click each checkbox → progress bar moves
- Reload → checkbox state persists
- Answer all 3 MCQs correctly → console (or `CAS2026.loadProgress()`) shows `completed: true`

- [ ] **Step 5: Commit Ch01**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add cas-2026-01-ultrasound.html
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "feat(cas-2026): populate Ch01 (Ultrasound)"
```

- [ ] **Step 6: Repeat Steps 1-5 for Chapters 02 → 09**

Each chapter follows the exact same pattern as Steps 1-5 but with:
- File: `cas-2026-NN-<slug>.html`
- `data-chapter`: `cas-NN`
- `data-chapter-no`: `N`
- Header title: from `CHAPTERS` in `cas-2026-shared.js`
- Speaker block: speakers field from `CHAPTERS`
- Images: from `images-cas-2026/NN-<slug>/`
- Nav prev: `cas-2026-(N-1)-*.html` (Ch1 has prev disabled)
- Nav next: `cas-2026-(N+1)-*.html` (Ch9's next → hub)

**Critical chapters with multi-speaker merge logic (recall from spec §2):**
- Ch01 (Ultrasong 湯/葉): merge overlapping concepts into single card, keep unique cards from each
- Ch05 (EPD 黃成偉 ×2): 2024 is base, add 2022-only cards as supplements
- Ch06 (Stent 蔡翰林 TTT vs Stent design): two sub-sections within the chapter
- Ch07 (TSCI 柯呈諭 ×2): 2024 is base, add 2022 supplements

Commit each chapter independently:

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add cas-2026-NN-<slug>.html
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "feat(cas-2026): populate ChNN (<title>)"
```

---

### Task 9: Build the Hub page

**Files:**
- Create: `cas-2026-hub.html`

- [ ] **Step 1: Create `cas-2026-hub.html`**

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CAS 2026 訓練課程 — Hub</title>
<link rel="stylesheet" href="design-system.css">
<link rel="stylesheet" href="achievements-ui.css">
<style>
  body { font-family:"Noto Sans TC","Microsoft JhengHei",Arial,sans-serif; background:#f5f7fa; color:#2d3748; margin:0; padding:0; line-height:1.6; }
  .container { max-width:800px; margin:0 auto; padding:16px; }
  .hub-header { background:linear-gradient(135deg,#1a365d,#2b6cb0); color:#fff; padding:32px 24px; text-align:center; border-radius:12px; margin-bottom:24px; }
  .hub-header h1 { font-size:1.75rem; margin:0 0 8px 0; }
  .hub-header p { margin:4px 0; opacity:.9; font-size:.95rem; }
  .progress-card { background:#fff; border-radius:10px; padding:20px; margin-bottom:20px; box-shadow:0 1px 4px rgba(0,0,0,.08); }
  .progress-card h3 { color:#1a365d; margin:0 0 12px 0; }
  .progress-bar { height:10px; background:#e2e8f0; border-radius:5px; overflow:hidden; margin:8px 0; }
  .progress-bar-fill { height:100%; background:linear-gradient(90deg,#48bb78,#38a169); transition:width .3s; width:0%; }
  .progress-stats { display:flex; justify-content:space-around; margin-top:12px; font-size:.9rem; color:#4a5568; }
  .progress-stats div { text-align:center; }
  .progress-stats strong { display:block; font-size:1.3rem; color:#1a365d; }
  .chapter-grid { display:grid; gap:12px; margin-bottom:24px; }
  .chapter-card { background:#fff; border-radius:10px; padding:16px 20px; box-shadow:0 1px 4px rgba(0,0,0,.08); text-decoration:none; color:inherit; display:flex; align-items:center; gap:16px; transition:transform .15s, box-shadow .15s; }
  .chapter-card:hover { transform:translateY(-2px); box-shadow:0 4px 12px rgba(0,0,0,.12); }
  .chapter-no { width:48px; height:48px; background:#1a365d; color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; flex-shrink:0; }
  .chapter-info { flex:1; min-width:0; }
  .chapter-info .title { font-weight:600; color:#1a365d; }
  .chapter-info .speakers { font-size:.8rem; color:#718096; margin-top:2px; }
  .chapter-pct { font-size:.85rem; color:#4a5568; white-space:nowrap; }
  .chapter-pct.done { color:#38a169; font-weight:600; }
  .actions { display:flex; gap:12px; margin-top:16px; }
  .action-btn { flex:1; padding:12px; background:#2b6cb0; color:#fff; text-align:center; border-radius:8px; text-decoration:none; font-weight:600; cursor:pointer; border:none; font-size:1rem; }
  .footer { margin-top:24px; padding:16px; font-size:.75rem; color:#718096; text-align:center; }
</style>
</head>
<body>

<div class="container">

  <div class="hub-header">
    <h1>🩺 CAS 2026 訓練課程</h1>
    <p>頸動脈支架介入學員學習模組</p>
    <p>中華民國心臟學會 · 週邊血管介入委員會</p>
  </div>

  <div class="progress-card">
    <h3>您的學習進度</h3>
    <div class="progress-bar"><div class="progress-bar-fill" id="overall-fill"></div></div>
    <div class="progress-stats">
      <div><strong id="stat-done">0</strong>已完成章</div>
      <div><strong id="stat-inprogress">0</strong>學習中章</div>
      <div><strong id="stat-untouched">9</strong>未開始章</div>
      <div><strong id="stat-pct">0%</strong>整體進度</div>
    </div>
  </div>

  <div class="chapter-grid" id="chapter-grid"></div>

  <div class="actions">
    <button class="action-btn" id="share-btn">📤 分享 QR Code</button>
    <button class="action-btn" id="export-btn">📊 匯出學習記錄</button>
  </div>

  <div class="footer">
    本教學資源圖片來源為各講師於歷年「頸動脈支架訓練課程」之授課投影片，僅供本課程學員學術教育使用。
  </div>

</div>

<script src="cas-2026-shared.js"></script>
<script src="achievements.js"></script>
<script>
(function () {
  const grid = document.getElementById('chapter-grid');
  const progress = CAS2026.loadProgress();

  let doneCount = 0, inProgressCount = 0, untouchedCount = 0;
  let totalCards = 0, totalDone = 0;

  CAS2026.CHAPTERS.forEach(ch => {
    const chProg = progress[ch.id] || { cards:{}, quiz:{}, totalCards:0, completed:false };
    const total = chProg.totalCards || 0;
    const done  = Object.values(chProg.cards || {}).filter(Boolean).length;
    const pct   = total ? Math.round(done * 100 / total) : 0;

    totalCards += total; totalDone += done;
    if (chProg.completed) doneCount++;
    else if (done > 0) inProgressCount++;
    else untouchedCount++;

    const card = document.createElement('a');
    card.className = 'chapter-card';
    card.href = `cas-2026-${ch.no.toString().padStart(2,'0')}-${ch.slug}.html`;
    card.innerHTML = `
      <div class="chapter-no">${ch.no}</div>
      <div class="chapter-info">
        <div class="title">${ch.title}</div>
        <div class="speakers">${ch.speakers}</div>
      </div>
      <div class="chapter-pct ${chProg.completed ? 'done' : ''}">
        ${chProg.completed ? '✅ 完成' : (total ? `${pct}%` : '⏳ 未開始')}
      </div>
    `;
    grid.appendChild(card);
  });

  document.getElementById('stat-done').textContent = doneCount;
  document.getElementById('stat-inprogress').textContent = inProgressCount;
  document.getElementById('stat-untouched').textContent = untouchedCount;
  const overallPct = totalCards ? Math.round(totalDone * 100 / totalCards) : 0;
  document.getElementById('stat-pct').textContent = overallPct + '%';
  document.getElementById('overall-fill').style.width = overallPct + '%';

  document.getElementById('share-btn').addEventListener('click', () => {
    const url = location.href;
    if (navigator.share) {
      navigator.share({ title:'CAS 2026 訓練課程', url });
    } else {
      navigator.clipboard.writeText(url);
      alert('已複製課程網址到剪貼簿：\n' + url);
    }
  });

  document.getElementById('export-btn').addEventListener('click', () => {
    const data = CAS2026.exportRecord();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type:'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `cas-2026-progress-${new Date().toISOString().slice(0,10)}.json`;
    a.click();
  });
})();
</script>

</body>
</html>
```

- [ ] **Step 2: Verify the Hub**

1. First visit each chapter HTML, tick a few cards / answer a quiz to populate progress
2. Then open `cas-2026-hub.html`
3. Confirm:
   - 9 chapter cards render with correct titles, speakers
   - Per-chapter progress % matches what was set
   - Overall progress bar and 4 stat numbers update correctly
   - Click any chapter card → navigates to that chapter HTML
   - Share button works (mobile native share or clipboard fallback)
   - Export button downloads a JSON file

- [ ] **Step 3: Commit**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add cas-2026-hub.html
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "feat(cas-2026): hub page with cross-chapter progress and export"
```

---

## Phase E — QA & Deployment

### Task 10: Cross-chapter mobile QA

**Files:**
- (None — verification task)

- [ ] **Step 1: Run a clean-state mobile QA pass**

In Chrome DevTools, toggle device emulation to iPhone 12 Pro (390 × 844). For each of `cas-2026-hub.html` and 9 chapter HTMLs, verify:

| Check | Pass criteria |
|---|---|
| Header sticky | Stays at top on scroll |
| Touch targets | Checkboxes ≥ 24×24 px; quiz options ≥ 44 px tall |
| Image overflow | All images fit within viewport, no horizontal scroll |
| Font legibility | ≥ 14 px body text; no truncated lines |
| Nav buttons | Prev/Next/Hub all wired correctly |
| Console | No JS errors on any page |
| Persistence | Tick boxes → close tab → reopen → state preserved |

- [ ] **Step 2: Run a real-phone QA pass**

Push current state to GitHub Pages (Task 12) or serve locally via Python:

```powershell
cd "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main"
python -m http.server 8000
```

Then open `http://<dev-machine-ip>:8000/cas-2026-hub.html` on actual iPhone / Android, repeat key checks (touch targets feel right, sticky header behaves on iOS Safari, images load over LAN).

- [ ] **Step 3: Fix any bugs found, then commit fixes**

For each bug found:
- Note the failing chapter / check
- Fix in source HTML / shared.js
- Re-verify
- Commit per-fix:

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add <changed-files>
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "fix(cas-2026): <description>"
```

---

### Task 11: Update sitemap.xml and files.json with the new pages

**Files:**
- Modify: `sitemap.xml`
- Modify: `files.json`

- [ ] **Step 1: Read current `files.json` to understand its schema**

Read the file (use Read tool) and identify the array element schema (title, url, description, tags, etc.).

- [ ] **Step 2: Append the 10 new entries (1 hub + 9 chapters)**

For each new file, add an entry matching the existing schema. Example (adjust keys to match actual schema):

```json
{
  "title": "CAS 2026 訓練課程 (Hub)",
  "url": "cas-2026-hub.html",
  "description": "頸動脈支架訓練課程整合教學模組 — 9 章互動 checklist + Quick Check",
  "tags": ["cas","carotid","stenting","2026","course","tsci"],
  "year": 2026
}
```

For each chapter add an entry with `title` matching `CHAPTERS[i].title`, `url` matching the file name.

- [ ] **Step 3: Update `sitemap.xml`**

Read existing `sitemap.xml`. For each of the 10 new pages, append a `<url>` entry following the existing pattern:

```xml
<url>
  <loc>https://drake1128.github.io/saq-questionnaire/cas-2026-hub.html</loc>
  <lastmod>2026-05-22</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.7</priority>
</url>
```

- [ ] **Step 4: Commit**

```bash
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" add sitemap.xml files.json
git -C "G:/我的雲端硬碟/004 教學資料 at Hsinchu 院內/Teaching materials CV education web at github/saq-questionnaire-main" commit -m "docs(cas-2026): register hub and 9 chapters in sitemap and catalog"
```

---

### Task 12: Push to GitHub for GitHub Pages deploy (Stage 1)

**Files:**
- (None — git operation only)

- [ ] **Step 1: Verify branch state and remote**

```powershell
cd "G:\我的雲端硬碟\004 教學資料 at Hsinchu 院內\Teaching materials CV education web at github\saq-questionnaire-main"
git status
git remote -v
git log --oneline -10
```

Expected: working tree clean, remote `origin` points to `github.com/drake1128/saq-questionnaire`, recent CAS 2026 commits visible.

- [ ] **Step 2: Push to remote**

```powershell
git push origin main
```

(Replace `main` with the actual default branch name if different.)

- [ ] **Step 3: Verify GitHub Pages deploys successfully**

Wait ~1-2 minutes, then visit:

```
https://drake1128.github.io/saq-questionnaire/cas-2026-hub.html
```

Confirm:
- Hub loads
- Click any chapter → chapter HTML loads
- Images load (paths must be relative to repo root)
- All interaction (checkboxes, quiz) works

If 404 or images broken, check that GitHub Pages source is set to the correct branch + root path in repo Settings.

- [ ] **Step 4: Generate a QR code for the hub URL (manual step or via Hub's share button)**

User-facing deliverable: print the QR code on the course program.

---

## Self-Review

The plan is complete. Verifications performed during writing:

- **Spec coverage**:
  - Architecture (§3 of spec) → Tasks 1, 9 (hub) and 8 (chapters)
  - Per-chapter template (§4) → Task 2 (template), 3 (interactivity)
  - Image pipeline (§5) → Tasks 4-7 (extract, sidecar, batch, processor)
  - Hub & deployment (§6) → Tasks 9 (hub), 12 (deploy)
  - Naming / file conventions (§3.4) → Task 8 explicitly uses them
  - Achievements integration (§4.3) → Task 3 calls `Achievements.unlock`
  - localStorage schema (§3.4) → Task 1 defines `cas-2026-progress` key

- **Placeholder scan**: No "TBD", "TODO", "fill in later" or vague "add error handling" steps. Code blocks are concrete and runnable.

- **Type consistency**:
  - `CAS2026.setCardChecked / isCardChecked / chapterProgress / overallProgress / exportRecord` defined in Task 1 are referenced in Tasks 3, 9 — names match.
  - Chapter file names use the same `cas-2026-NN-<slug>.html` convention from Task 2 through Task 12 and match `CHAPTERS` in Task 1.
  - Image path pattern `images-cas-2026/NN-<slug>/<year>-<slug>-seq<NNN>.png` from Task 7 matches the `<img src>` example in Task 8.
  - `chapter_sources.json` keys (`01-ultrasound` etc.) match sidecar / image folder names everywhere.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-05-22-cas-2026-training-module.md`. Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration on the long content-population phase.

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch with checkpoints. Better for the Phase A infrastructure tasks where every step depends on the previous.

A hybrid approach is also natural here: **inline for Phases A-B-C (you and I do them together in this session), subagent-driven for Phase D Task 8** (the 9 chapter-content tasks are highly parallel and each warrants its own focused agent).

**Which approach?**
