# Website Improvement Plan
## 心血管照護教學資源中心 (Cardiovascular Care Education Hub)

**Generated:** January 2026
**Last Updated:** January 18, 2026
**Website:** https://drake1128.github.io/saq-questionnaire

---

## Master To-Do List (Priority Order)

### Phase 1: Critical - Accessibility & SEO (Week 1-2)

| # | Task | Priority | Time Est. | Status |
|---|------|----------|-----------|--------|
| 1 | Add `aria-label` to all icon buttons | Critical | 2 hrs | ☑ DONE |
| 2 | Add `alt` text to all images and SVGs | Critical | 1 hr | ☑ DONE (aria-hidden on 16 files) |
| 3 | Add skip-to-content link at top of each page | Critical | 30 min | ☑ DONE |
| 4 | Remove `user-scalable=no` restriction | Critical | 30 min | ☑ DONE |
| 5 | Fix heading hierarchy (h1 > h2 > h3) | Critical | 1 hr | ☑ DONE (7 categories → h2) |
| 6 | Add unique `<meta name="description">` to each page | High | 2 hrs | ☑ DONE (index.html) |
| 7 | Add Open Graph tags for social sharing | High | 1 hr | ☑ DONE |
| 8 | Create `sitemap.xml` | High | 30 min | ☑ DONE (40+ URLs) |
| 9 | Create `robots.txt` | High | 15 min | ☑ DONE |
| 10 | Add structured data (Schema.org) | High | 1 hr | ☑ DONE |

### Phase 2: High Priority - Design System (Week 3-4)

| # | Task | Priority | Time Est. | Status |
|---|------|----------|-----------|--------|
| 11 | Create `design-system.css` with shared variables | High | 3 hrs | ☑ DONE (in index.html :root) |
| 12 | Standardize color palette (3-4 core themes) | High | 2 hrs | ☑ DONE |
| 13 | Define consistent spacing scale | High | 1 hr | ☐ |
| 14 | Create reusable button classes | High | 1 hr | ☐ |
| 15 | Standardize card and shadow styles | High | 1 hr | ☑ DONE |
| 16 | Implement keyboard navigation (Tab, Enter, Escape) | High | 2 hrs | ☐ |
| 17 | Add visible focus indicators (`:focus-visible`) | High | 1 hr | ☑ DONE (already in index.html) |

### Phase 3: Medium Priority - Performance & Features (Week 5-8)

| # | Task | Priority | Time Est. | Status |
|---|------|----------|-----------|--------|
| 18 | Add `loading="lazy"` to images below fold | Medium | 1 hr | ☐ |
| 19 | Preload critical fonts and scripts | Medium | 30 min | ☑ DONE (preconnect added) |
| 20 | Implement Dark Mode toggle | Medium | 3 hrs | ☐ |
| 21 | Add print stylesheet | Medium | 2 hrs | ☐ |
| 22 | Create advanced search filters | Medium | 4 hrs | ☑ DONE (category filters) |
| 23 | Add related resources linking | Medium | 3 hrs | ☐ |
| 24 | Build feedback mechanism | Medium | 3 hrs | ☐ |

### Phase 4: Low Priority - Content Enhancements (Ongoing)

| # | Task | Priority | Time Est. | Status |
|---|------|----------|-----------|--------|
| 25 | Add estimated completion time for each resource | Low | 2 hrs | ☐ |
| 26 | Add difficulty level indicators | Low | 2 hrs | ☐ |
| 27 | Add learning outcomes for each module | Low | 3 hrs | ☐ |
| 28 | Add last updated date to each page | Low | 1 hr | ☐ |
| 29 | Create Favorites/Bookmarks feature | Low | 4 hrs | ☐ |
| 30 | Build Learning Progress tracker | Low | 6 hrs | ☐ |

### Testing Tasks

| # | Task | Priority | Status |
|---|------|----------|--------|
| T1 | Test with keyboard only (no mouse) | High | ☐ |
| T2 | Test with screen reader (VoiceOver/NVDA) | High | ☐ |
| T3 | Check color contrast (WCAG 2.1 AA) | High | ☐ |
| T4 | Validate HTML with W3C validator | Medium | ☐ |
| T5 | Run Lighthouse audit | Medium | ☐ |
| T6 | Test on iOS Safari | Medium | ☐ |
| T7 | Test on Android Chrome | Medium | ☐ |
| T8 | Test on slow 3G connection | Low | ☐ |

### Files to Create

| File | Purpose | Status |
|------|---------|--------|
| `design-system.css` | Shared CSS variables and components | ☑ (integrated in index.html) |
| `sitemap.xml` | Search engine indexing | ☑ DONE |
| `robots.txt` | Search engine crawling rules | ☑ DONE |
| `og-image.svg` | Social media preview image | ☑ DONE |

---

## Progress Summary

| Category | Tasks | Completed | Progress |
|----------|-------|-----------|----------|
| Accessibility (1-5) | 5 | 5 | 100% ✅ |
| SEO (6-10) | 5 | 5 | 100% ✅ |
| Design System (11-17) | 7 | 4 | 57% |
| Performance (18-19) | 2 | 1 | 50% |
| Features (20-24) | 5 | 1 | 20% |
| Content (25-30) | 6 | 0 | 0% |
| Testing (T1-T8) | 8 | 0 | 0% |
| **Total** | **38** | **16** | **42%** |

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
