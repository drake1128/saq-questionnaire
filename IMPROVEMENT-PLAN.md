# Website Improvement Plan
## 心血管照護教學資源中心 (Cardiovascular Care Education Hub)

**Generated:** January 2026
**Website:** https://drake1128.github.io/saq-questionnaire

---

## Executive Summary

Your website is a **well-executed educational platform** with excellent content organization and thoughtful UX. However, there are opportunities to improve **accessibility, SEO, design consistency, and performance** that would make it a world-class medical education resource.

---

## Current Strengths

| Area | Status |
|------|--------|
| Content Organization | Excellent - 44 resources across 7 well-defined categories |
| Mobile Responsiveness | Good - CSS Grid with adaptive layouts |
| Interactive Features | Strong - 31 React-based interactive apps |
| Visual Design | Professional - consistent card-based UI, color coding |
| Search & Filtering | Working - real-time search with tag support |
| Share Functionality | Complete - QR code, Email, LINE sharing |

---

## Improvement Areas

### 1. Accessibility (Critical Priority)

**Current Issues:**
- No ARIA labels or roles on interactive elements
- Missing `alt` text on images and icons
- No keyboard navigation support
- Missing skip-to-content links
- Some pages disable zoom (`user-scalable=no`)

**Recommendations:**
- [ ] Add `aria-label` to all icon buttons
- [ ] Add `alt` text to all images and SVGs
- [ ] Implement keyboard navigation (Tab, Enter, Escape)
- [ ] Add visible focus indicators (`:focus-visible`)
- [ ] Add skip-to-content link at top of each page
- [ ] Remove or soften `user-scalable=no` restriction
- [ ] Ensure proper heading hierarchy (h1 > h2 > h3)
- [ ] Test with screen readers (VoiceOver, NVDA)

**Example Fix:**
```html
<!-- Before -->
<button onclick="openShareModal()">📤</button>

<!-- After -->
<button onclick="openShareModal()" aria-label="分享網站" title="分享網站">📤</button>
```

---

### 2. SEO & Meta Information (High Priority)

**Current Issues:**
- No meta descriptions on any pages
- Missing Open Graph tags for social sharing
- No structured data (Schema.org)
- No sitemap.xml or robots.txt

**Recommendations:**
- [ ] Add unique `<meta name="description">` to each page
- [ ] Add Open Graph tags for better social media previews
- [ ] Create `sitemap.xml` for search engine indexing
- [ ] Create `robots.txt` file
- [ ] Add structured data for educational content

**Example Implementation:**
```html
<head>
    <!-- Basic SEO -->
    <meta name="description" content="心血管照護教學資源中心 - 提供導管室、病房、加護病房照護教學資源">
    <meta name="keywords" content="心血管, 心臟科, 教學, 護理, 導管室, CCU, ICU">

    <!-- Open Graph -->
    <meta property="og:title" content="心血管照護教學資源中心">
    <meta property="og:description" content="專業心血管照護教學資源，含導管室、病房、ICU 教學內容">
    <meta property="og:image" content="https://drake1128.github.io/saq-questionnaire/og-image.png">
    <meta property="og:url" content="https://drake1128.github.io/saq-questionnaire">
    <meta property="og:type" content="website">

    <!-- Structured Data -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "EducationalOrganization",
        "name": "心血管照護教學資源中心",
        "url": "https://drake1128.github.io/saq-questionnaire",
        "description": "心血管照護教學資源平台"
    }
    </script>
</head>
```

---

### 3. Design System Consistency (High Priority)

**Current Issues:**
- Multiple color schemes across apps (8+ different primary colors)
- Inconsistent typography and spacing
- Different button styles and card shadows
- No centralized design system

**Recommendations:**
- [ ] Create `design-system.css` with shared variables
- [ ] Standardize color palette (3-4 core themes)
- [ ] Define consistent spacing scale (8px, 16px, 24px, 32px)
- [ ] Create reusable button classes
- [ ] Standardize card and shadow styles

**Proposed Design Tokens:**
```css
:root {
    /* Primary Colors */
    --color-primary: #e74c3c;
    --color-secondary: #3498db;
    --color-success: #27ae60;
    --color-warning: #f39c12;

    /* Category Colors */
    --color-cath: #e74c3c;
    --color-ward: #3498db;
    --color-icu: #00d4ff;
    --color-intervention: #9b59b6;
    --color-medication: #27ae60;
    --color-patient: #f39c12;

    /* Spacing */
    --space-xs: 4px;
    --space-sm: 8px;
    --space-md: 16px;
    --space-lg: 24px;
    --space-xl: 32px;

    /* Typography */
    --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft JhengHei', sans-serif;
    --font-size-sm: 0.875rem;
    --font-size-md: 1rem;
    --font-size-lg: 1.25rem;
    --font-size-xl: 1.5rem;

    /* Shadows */
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 15px rgba(0,0,0,0.1);
    --shadow-lg: 0 8px 25px rgba(0,0,0,0.15);
}
```

---

### 4. Performance Optimization (Medium Priority)

**Current Issues:**
- React + Babel loaded on every page (heavy)
- Multiple CDN requests per page
- No lazy loading for images
- No resource preloading

**Recommendations:**
- [ ] Consider lighter alternatives (Preact, Alpine.js) for simple interactions
- [ ] Add `loading="lazy"` to images below the fold
- [ ] Preload critical fonts and scripts
- [ ] Combine external CSS/JS where possible
- [ ] Add caching headers

**Example:**
```html
<!-- Preload critical resources -->
<link rel="preload" as="font" href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC" crossorigin>

<!-- Lazy load images -->
<img loading="lazy" src="..." alt="...">
```

---

### 5. New Features (Medium Priority)

| Feature | Description | Benefit |
|---------|-------------|---------|
| Dark Mode Toggle | Add light/dark theme switch | User preference, reduce eye strain |
| Print Stylesheet | Optimize pages for printing | Offline study materials |
| Favorites/Bookmarks | Save frequently used tools | Quick access for repeat users |
| Learning Progress | Track completed resources | Student engagement |
| Search Filters | Filter by category, difficulty, time | Better resource discovery |
| Related Resources | Link similar content | Improved navigation |
| Feedback Form | Collect user suggestions | Continuous improvement |

**Dark Mode Implementation:**
```javascript
// Add toggle button
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

// Check preference on load
if (localStorage.getItem('darkMode') === 'true' ||
    window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.body.classList.add('dark-mode');
}
```

---

### 6. Content Enhancements (Low Priority)

**Recommendations:**
- [ ] Add estimated completion time for each resource
- [ ] Add difficulty level indicators (初階/中階/進階)
- [ ] Add prerequisite information
- [ ] Add learning outcomes for each module
- [ ] Add author/reviewer attribution
- [ ] Add last updated date to each page
- [ ] Add version history for clinical guidelines

**Example Badge System:**
```html
<div class="app-meta">
    <span class="badge difficulty-beginner">初階</span>
    <span class="badge time">15 分鐘</span>
    <span class="badge updated">2026-01 更新</span>
</div>
```

---

## Implementation Roadmap

### Phase 1: Critical (Week 1-2)
**Focus: Accessibility & SEO**
1. Add ARIA labels and alt text
2. Implement keyboard navigation
3. Create meta descriptions for all pages
4. Add Open Graph tags
5. Create sitemap.xml and robots.txt

### Phase 2: High Priority (Week 3-4)
**Focus: Design System & Performance**
1. Create centralized design-system.css
2. Standardize colors and typography
3. Optimize image loading
4. Add resource preloading
5. Create component library

### Phase 3: Medium Priority (Week 5-8)
**Focus: New Features**
1. Implement dark mode toggle
2. Add print stylesheets
3. Create advanced search filters
4. Add related resources linking
5. Build feedback mechanism

### Phase 4: Ongoing
**Focus: Content & Polish**
1. Add content metadata (time, difficulty)
2. Create learning progress tracker
3. Add multilingual support framework
4. Regular accessibility audits

---

## Quick Wins (Can Do Today)

These improvements take minimal effort but have high impact:

1. **Add meta descriptions** - 1 hour
2. **Add alt text to images** - 30 minutes
3. **Create robots.txt** - 15 minutes
4. **Add skip-to-content link** - 15 minutes
5. **Fix heading hierarchy** - 1 hour
6. **Add favicon if missing** - 15 minutes

---

## Files to Create

| File | Purpose |
|------|---------|
| `design-system.css` | Shared CSS variables and components |
| `sitemap.xml` | Search engine indexing |
| `robots.txt` | Search engine crawling rules |
| `og-image.png` | Social media preview image |
| `ACCESSIBILITY.md` | Accessibility guidelines |
| `CONTRIBUTING.md` | Contribution guidelines |

---

## Testing Checklist

### Accessibility Testing
- [ ] Test with keyboard only (no mouse)
- [ ] Test with screen reader (VoiceOver/NVDA)
- [ ] Check color contrast (WCAG 2.1 AA)
- [ ] Validate HTML with W3C validator

### Mobile Testing
- [ ] Test on iOS Safari
- [ ] Test on Android Chrome
- [ ] Test on various screen sizes (320px - 1440px)
- [ ] Test touch targets (minimum 44x44px)

### Performance Testing
- [ ] Run Lighthouse audit
- [ ] Check Core Web Vitals (LCP, FID, CLS)
- [ ] Test on slow 3G connection

---

## Summary

| Category | Current | Target | Priority |
|----------|---------|--------|----------|
| Accessibility | 30% | 90%+ | Critical |
| SEO | 20% | 80%+ | High |
| Design Consistency | 60% | 90%+ | High |
| Performance | 70% | 85%+ | Medium |
| Features | 70% | 85%+ | Medium |

Your website has an excellent foundation. Implementing these improvements will make it a truly world-class cardiovascular education resource that serves all users effectively.

---

*This improvement plan was generated based on a comprehensive analysis of the codebase. For questions or clarifications, please review with the development team.*
