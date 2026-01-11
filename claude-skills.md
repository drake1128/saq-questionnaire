---
name: cv-education-webapp
description: Create mobile-optimized, interactive HTML/React educational web applications for cardiovascular medicine training. Use when Drake (謝慕揚醫師) requests development of (1) nursing teaching apps for cardiac catheterization, wound care, or post-procedure protocols, (2) medication learning tools with calculators or dosing algorithms, (3) clinical procedure checklists or handoff teaching modules, (4) patient education materials, (5) diagnostic interpretation guides (ECG, Echo, troponin), (6) interventional cardiology learning resources (PTMC, LAAO, TEER, carotid stenting), or (7) emergency protocol apps (CPR, cardiogenic shock). Triggers on requests containing keywords like "教學app", "學習網頁", "護理教學", "自學工具", "臨床checklist", "mobile app", or references to NTUH Hsinchu cardiovascular center training materials.
---

# Cardiovascular Education Web Application Development

Create standalone, mobile-optimized HTML applications using React with CDN for medical education at NTUH Hsinchu Cardiovascular Center.

## PDF-to-App Workflow

**When a new PDF file is detected in the project folder:**

1. **Detect**: Scan for PDF files that may be new or haven't been converted yet
2. **Ask**: Prompt the user with:
   > "I found a new PDF: `[filename.pdf]`. Would you like me to:
   > 1. Read and analyze its content
   > 2. Convert it into an interactive web application
   > 3. Skip for now"
3. **Process**: If user confirms, read the PDF content and extract:
   - Main topics and sections
   - Key learning points
   - Any tables, formulas, or algorithms
   - Quiz-worthy content
4. **Create**: Build a web application following this skill's templates
5. **Update**: Add the new app to `index.html` (see Post-Creation Actions)

## Technical Stack

### Required CDN Libraries

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>[應用程式標題]</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.5/babel.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
```

Alternative with Tailwind (for simpler styling):
```html
<script src="https://cdn.tailwindcss.com"></script>
```

### CSS Variables Theme

```css
:root {
    --primary: #1e3a5f;
    --primary-light: #2d5a87;
    --accent: #e74c3c;
    --accent-light: #ff6b5b;
    --success: #27ae60;
    --warning: #f39c12;
    --bg-cream: #faf8f5;
    --bg-card: #ffffff;
    --text-dark: #2c3e50;
    --text-muted: #7f8c8d;
    --border: #ecf0f1;
    --shadow: 0 4px 20px rgba(0,0,0,0.08);
}

/* For cath lab / ICU dark theme */
:root.dark-theme {
    --bg-cream: #1a1a2e;
    --bg-card: #16213e;
    --text-dark: #eaeaea;
    --text-muted: #a0a0a0;
    --border: #2d3748;
}
```

## Application Structure

### React Component Pattern

```jsx
const { useState, useEffect, useRef } = React;

// Icon components as inline SVG
const Icons = {
    Heart: () => (
        <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24">
            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5..."/>
        </svg>
    ),
    // Add more icons as needed
};

// Main App Component
const App = () => {
    const [currentSection, setCurrentSection] = useState('home');
    const [progress, setProgress] = useState({});

    // Load progress from localStorage
    useEffect(() => {
        const saved = localStorage.getItem('app-progress');
        if (saved) setProgress(JSON.parse(saved));
    }, []);

    // Save progress
    useEffect(() => {
        localStorage.setItem('app-progress', JSON.stringify(progress));
    }, [progress]);

    return (
        <div className="app-container">
            {/* Navigation and Content */}
        </div>
    );
};

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
```

## Content Modules

### 1. Educational Section Template

```jsx
const EducationalSection = ({ title, content, keyPoints }) => (
    <div className="section-card">
        <h2>{title}</h2>
        <div className="content">{content}</div>
        <div className="key-points">
            {keyPoints.map((point, i) => (
                <div key={i} className="point">
                    <Icons.Check />
                    <span>{point}</span>
                </div>
            ))}
        </div>
    </div>
);
```

### 2. Interactive Checklist Template

```jsx
const Checklist = ({ items, sectionId, onComplete }) => {
    const [checked, setChecked] = useState({});

    const handleCheck = (id) => {
        const newChecked = { ...checked, [id]: !checked[id] };
        setChecked(newChecked);

        const allChecked = items.every(item => newChecked[item.id]);
        if (allChecked) onComplete(sectionId);
    };

    return (
        <div className="checklist">
            {items.map(item => (
                <div
                    key={item.id}
                    className={`checklist-item ${checked[item.id] ? 'completed' : ''}`}
                    onClick={() => handleCheck(item.id)}
                >
                    <div className="checkbox">
                        {checked[item.id] && <Icons.Check />}
                    </div>
                    <span>{item.text}</span>
                </div>
            ))}
        </div>
    );
};
```

### 3. Quiz Module Template

```jsx
const Quiz = ({ questions }) => {
    const [currentQ, setCurrentQ] = useState(0);
    const [selected, setSelected] = useState(null);
    const [showResult, setShowResult] = useState(false);
    const [score, setScore] = useState(0);

    const handleAnswer = (optionIndex) => {
        setSelected(optionIndex);
        setShowResult(true);
        if (optionIndex === questions[currentQ].correct) {
            setScore(s => s + 1);
        }
    };

    const nextQuestion = () => {
        if (currentQ < questions.length - 1) {
            setCurrentQ(c => c + 1);
            setSelected(null);
            setShowResult(false);
        }
    };

    const q = questions[currentQ];

    return (
        <div className="quiz-container">
            <div className="progress-bar">
                <div style={{width: `${(currentQ + 1) / questions.length * 100}%`}} />
            </div>
            <h3>第 {currentQ + 1} 題 / 共 {questions.length} 題</h3>
            <p className="question">{q.question}</p>
            <div className="options">
                {q.options.map((opt, i) => (
                    <button
                        key={i}
                        className={`option ${selected === i ? (i === q.correct ? 'correct' : 'wrong') : ''}`}
                        onClick={() => !showResult && handleAnswer(i)}
                        disabled={showResult}
                    >
                        {opt}
                    </button>
                ))}
            </div>
            {showResult && (
                <div className="explanation">
                    <p>{selected === q.correct ? '✅ 正確！' : '❌ 錯誤'}</p>
                    <p>{q.explanation}</p>
                    <button onClick={nextQuestion}>
                        {currentQ < questions.length - 1 ? '下一題' : '查看結果'}
                    </button>
                </div>
            )}
        </div>
    );
};
```

### 4. Clinical Calculator Template

```jsx
const Calculator = ({ name, formula, inputs, calculate }) => {
    const [values, setValues] = useState({});
    const [result, setResult] = useState(null);

    const handleCalculate = () => {
        const res = calculate(values);
        setResult(res);
    };

    return (
        <div className="calculator">
            <h3>{name}</h3>
            {inputs.map(input => (
                <div key={input.id} className="input-group">
                    <label>{input.label}</label>
                    {input.type === 'select' ? (
                        <select
                            value={values[input.id] || ''}
                            onChange={e => setValues({...values, [input.id]: e.target.value})}
                        >
                            {input.options.map(opt => (
                                <option key={opt.value} value={opt.value}>{opt.label}</option>
                            ))}
                        </select>
                    ) : (
                        <input
                            type={input.type}
                            value={values[input.id] || ''}
                            onChange={e => setValues({...values, [input.id]: e.target.value})}
                            placeholder={input.placeholder}
                        />
                    )}
                </div>
            ))}
            <button onClick={handleCalculate}>計算</button>
            {result && (
                <div className="result">
                    <h4>結果</h4>
                    <p className="value">{result.value}</p>
                    <p className="interpretation">{result.interpretation}</p>
                </div>
            )}
        </div>
    );
};
```

### 5. SVG Anatomical Diagram Template

```jsx
const AnatomyDiagram = ({ highlightArea }) => (
    <svg viewBox="0 0 200 200" className="anatomy-svg">
        {/* Base anatomy */}
        <ellipse cx="100" cy="100" rx="80" ry="60" fill="#fad0c4" stroke="#d4a5a5" strokeWidth="2"/>

        {/* Highlighted structure */}
        <circle
            cx="100" cy="100" r="20"
            fill={highlightArea === 'target' ? '#e74c3c' : '#ccc'}
            opacity="0.7"
        />

        {/* Labels */}
        <text x="100" y="150" textAnchor="middle" fontSize="12">結構名稱</text>
    </svg>
);
```

## Language Rules

1. **Main UI**: Traditional Chinese (繁體中文)
2. **Preserve English** for:
   - Drug names (medications)
   - Medical terminology
   - Procedure names
   - Lab tests
   - Anatomical terms in parentheses

Example: `"股動脈 (Femoral Artery)"`, `"Heparin 5000 units"`

## Taiwan-Specific Adaptations

### Hospital Medication Codes
When referencing medications, include Taiwan hospital codes if known:
- Warfarin: 院內代碼
- Heparin: 院內代碼

### Reference Values
Use Taiwan-specific normal ranges when different from international standards.

### National Health Insurance
Note NHI coverage criteria when relevant for medications or procedures.

## Mobile Optimization Requirements

```css
/* Touch-friendly buttons */
.button, .checklist-item {
    min-height: 48px;
    padding: 12px 16px;
}

/* Prevent zoom on input focus */
input, select, textarea {
    font-size: 16px;
}

/* Safe area for notched phones */
.app-container {
    padding-bottom: env(safe-area-inset-bottom);
}

/* Swipe gestures */
.section {
    touch-action: pan-x pan-y;
}
```

## Application Categories

Map new applications to existing categories:

1. **Cath Lab Teaching (導管室教學)**: Procedures, protocols, hemostasis
2. **Ward & ICU Care (病房與加護照護)**: Post-procedure care, monitoring, complications
3. **Interventional Treatment (介入治療)**: PTMC, LAAO, TEER, carotid
4. **Medication Learning (藥物學習)**: Drug protocols, calculators, interactions
5. **Patient Education (病人衛教)**: Patient-facing content, discharge instructions
6. **Learning Resources (學習資源)**: Lectures, guidelines, case studies

## Quality Checklist

Before finalizing:

- [ ] Mobile viewport meta tag included
- [ ] Touch targets ≥48px
- [ ] localStorage progress persistence working
- [ ] All interactive elements have visual feedback
- [ ] Quiz has immediate feedback with explanations
- [ ] Medical content reviewed for Taiwan-specific accuracy
- [ ] Drug names remain in English
- [ ] Bilingual terminology format: 中文 (English)
- [ ] Dark theme option for cath lab/ICU use
- [ ] No external dependencies requiring installation
- [ ] **Reference with hyperlink** added to title page (see Reference Requirements below)
- [ ] **Hyperlinks verified** - manually check all URLs are correct and working

## Reference Requirements

**IMPORTANT: Every educational app MUST include proper references with hyperlinks.**

### On Title Page (HomePage)
Add a clickable reference section below the main description:

```jsx
<div className="mt-4 pt-4 border-t border-white/10">
  <a href="[CORRECT_URL]" target="_blank" rel="noopener noreferrer" className="block hover:bg-white/5 rounded-lg p-2 -m-2 transition-colors">
    <p className="text-gray-400 text-sm">📚 Reference: [Authors]. <span className="italic">[Title].</span></p>
    <p className="text-cyan-400/70 text-sm hover:text-cyan-300">[Journal Year; Volume: Pages] <span className="text-xs">↗</span></p>
  </a>
</div>
```

### Hyperlink Verification Checklist
- [ ] **Always verify the hyperlink is correct** before committing
- [ ] Test the link opens to the correct paper/resource
- [ ] Prefer official publisher links (e.g., Springer, Elsevier, PubMed)
- [ ] Use DOI links (https://doi.org/...) or direct publisher URLs
- [ ] **Never guess DOI numbers** - verify from the actual paper or search

### Example Reference Format
```
📚 Reference: Saura O, Combes A, Hekimian G. My echo checklist in venoarterial ECMO patients.
Intensive Care Med 2024; 50: 2158-2161 ↗
```
Link: `https://link.springer.com/article/10.1007/s00134-024-07659-2`

## File Naming Convention

`[topic]-[type]-app.html`

Examples:
- `cath-wound-care-app.html`
- `warfarin-dosing-calculator.html`
- `tee-interpretation-guide.html`

## Post-Creation Actions

**IMPORTANT: After creating any new web application, you MUST update `index.html` to include a link to the new app.**

### Update index.html Checklist

1. **Identify the correct category** for the new app:
   - 導管室教學 Cath Lab (`class="app-card cath"`)
   - 病房與加護病房照護 Ward & ICU Care (`class="app-card ward"` or `class="app-card icu"`)
   - 介入性治療教學 Intervention (`class="app-card intervention"`)
   - 藥物學習 Medication (`class="app-card medication"`)
   - 病人與家屬衛教 Patient Education (`class="app-card patient"`)
   - 學習資源 Learning Resources (`class="app-card learning"`)
   - 行政流程 Administrative (`class="app-card learning"`)

2. **Add a new app card** in the appropriate `<div class="app-grid">` section:

```html
<a href="[new-app-filename].html" class="app-card [category]" data-tags="[space-separated tags]">
    <div class="app-icon">[emoji]</div>
    <div class="app-title">[中文標題]</div>
    <div class="app-desc">[簡短描述]</div>
    <div class="app-tags">
        <span class="tag staff">醫護人員</span>  <!-- or <span class="tag patient">病人衛教</span> -->
        <span class="tag new">新增</span>
        <span class="tag">[additional tag]</span>
    </div>
</a>
```

3. **Update the category count** in the corresponding `<span class="category-count">` element.

4. **Update the total apps count** in the stats bar if needed (currently auto-calculated by JS).

### Tag Classes Reference
- `tag.staff` - 醫護人員 (blue)
- `tag.patient` - 病人衛教 (orange)
- `tag.new` - 新增 (green)
- `tag.updated` - 更新 (pink)
- `tag.icu` - ICU (cyan)

## GitHub Push Requirements

**IMPORTANT: Always push changes to GitHub after creating or updating any file.**

### Repository
- GitHub: `https://github.com/drake1128/saq-questionnaire`
- Branch: `main`

### After Every Change
1. Stage the changed files: `git add [files]`
2. Commit with descriptive message: `git commit -m "Description"`
3. Push to GitHub: `git push origin master:main`

### Commit Message Format
```
[Action] [Component/File] - [Brief description]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

Examples:
- `Add VA-ECMO Echo Checklist teaching app`
- `Fix reference hyperlink to correct Springer URL`
- `Update index.html with new app link`

## Output

Save completed applications to the project root directory alongside index.html.
