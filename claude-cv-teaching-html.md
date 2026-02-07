---
name: cv-education-webapp
description: Create mobile-optimized, interactive HTML/React educational web applications for cardiovascular medicine training. Use when Drake requests development of (1) nursing teaching apps for cardiac catheterization, wound care, or post-procedure protocols, (2) medication learning tools with calculators or dosing algorithms, (3) clinical procedure checklists or handoff teaching modules, (4) patient education materials, (5) diagnostic interpretation guides (ECG, Echo, troponin), (6) interventional cardiology learning resources (PTMC, LAAO, TEER, carotid stenting), or (7) emergency protocol apps (CPR, cardiogenic shock). Triggers on keywords: "teaching", "learning", "checklist", "mobile app", or cardiovascular center training materials.
---

# Cardiovascular Education Web Application Development Guide

> **Institution:** NTUH Hsinchu Branch - Cardiovascular Center
> **Project:** 心血管照護教學資源中心 (Cardiovascular Care Education Hub)
> **Repository:** `drake1128/saq-questionnaire`
> **Last Updated:** 2026-01

This comprehensive guide documents the workflow, HTML style rules, share functionality, and development conventions for creating CV teaching web applications.

---

## Table of Contents

1. [Technical Stack](#1-technical-stack)
2. [HTML Template Boilerplate](#2-html-template-boilerplate)
3. [CSS Design System](#3-css-design-system)
4. [Dark Theme Patterns](#4-dark-theme-patterns)
5. [Component Templates](#5-component-templates)
6. [Share Button Implementation](#6-share-button-implementation)
7. [React Component Patterns](#7-react-component-patterns)
8. [Reference Requirements](#8-reference-requirements)
9. [Mobile Responsiveness](#9-mobile-responsiveness)
10. [Language Rules](#10-language-rules)
11. [Application Categories](#11-application-categories)
12. [Post-Creation Actions](#12-post-creation-actions)
13. [File Naming Convention](#13-file-naming-convention)
14. [Quality Checklist](#14-quality-checklist)
15. [Git Workflow](#15-git-workflow)

---

## 1. Technical Stack

### Required CDN Libraries

All applications use React 18 with Babel for in-browser JSX transformation:

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>[Application Title]</title>

    <!-- React 18 + Babel -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.5/babel.min.js"></script>

    <!-- Google Fonts (Traditional Chinese) -->
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
```

### Optional: Tailwind CSS

For simpler styling needs:
```html
<script src="https://cdn.tailwindcss.com"></script>
```

---

## 2. HTML Template Boilerplate

### Complete Single-File Application Structure

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
    <style>
        /* CSS Variables and Styles Here */
    </style>
</head>
<body>
    <!-- Share Button (see Section 6) -->
    <div class="share-button">...</div>

    <!-- React Root -->
    <div id="root"></div>

    <!-- React Application -->
    <script type="text/babel">
        const { useState, useEffect, useRef } = React;

        const App = () => {
            // Application logic
            return (
                <div className="app-container">
                    {/* Content */}
                </div>
            );
        };

        ReactDOM.render(<App />, document.getElementById('root'));
    </script>

    <!-- Share Button JavaScript (see Section 6) -->
    <script>
        // Share functions
    </script>
</body>
</html>
```

---

## 3. CSS Design System

### 3.1 CSS Custom Properties (Design Tokens)

Copy this complete design token set into your `<style>` block:

```css
:root {
    /* =============================================
       PRIMARY COLORS
       ============================================= */
    --color-primary: #e74c3c;
    --color-primary-dark: #c0392b;
    --color-primary-light: #f5b7b1;

    --color-secondary: #3498db;
    --color-secondary-dark: #2980b9;
    --color-secondary-light: #aed6f1;

    /* =============================================
       SEMANTIC COLORS
       ============================================= */
    --color-success: #27ae60;
    --color-success-dark: #1e8449;
    --color-success-light: #a9dfbf;

    --color-warning: #f39c12;
    --color-warning-dark: #d68910;
    --color-warning-light: #f9e79f;

    --color-danger: #e74c3c;
    --color-danger-dark: #c0392b;
    --color-danger-light: #f5b7b1;

    --color-info: #3498db;
    --color-info-dark: #2980b9;
    --color-info-light: #aed6f1;

    /* =============================================
       CATEGORY COLORS (by function)
       ============================================= */
    --color-cath: #e74c3c;          /* Cath Lab - Red */
    --color-ward: #3498db;          /* Ward - Blue */
    --color-icu: #00d4ff;           /* ICU/CCU - Cyan */
    --color-intervention: #9b59b6;  /* Intervention - Purple */
    --color-medication: #27ae60;    /* Medication - Green */
    --color-patient: #f39c12;       /* Patient Education - Orange */
    --color-learning: #1abc9c;      /* Learning Resources - Teal */

    /* =============================================
       ACHIEVEMENT TIER COLORS
       ============================================= */
    --tier-bronze: #cd7f32;
    --tier-silver: #a8a8a8;
    --tier-gold: #ffd700;
    --tier-platinum: #e5e4e2;

    /* =============================================
       NEUTRAL COLORS (Grayscale)
       ============================================= */
    --color-dark: #2c3e50;
    --color-gray-900: #1a252f;
    --color-gray-800: #2c3e50;
    --color-gray-700: #34495e;
    --color-gray-600: #5d6d7e;
    --color-gray-500: #7f8c8d;
    --color-gray-400: #95a5a6;
    --color-gray-300: #bdc3c7;
    --color-gray-200: #d5dbdb;
    --color-gray-100: #ecf0f1;
    --color-gray-50: #f8f9f9;
    --color-white: #ffffff;

    /* =============================================
       TEXT COLORS
       ============================================= */
    --text-primary: #2c3e50;
    --text-secondary: #5d6d7e;
    --text-muted: #7f8c8d;
    --text-light: #95a5a6;
    --text-inverse: #ffffff;

    /* =============================================
       SPACING SCALE (8px base)
       ============================================= */
    --space-0: 0;
    --space-1: 4px;
    --space-2: 8px;
    --space-3: 12px;
    --space-4: 16px;
    --space-5: 20px;
    --space-6: 24px;
    --space-7: 28px;
    --space-8: 32px;
    --space-10: 40px;
    --space-12: 48px;
    --space-16: 64px;
    --space-20: 80px;

    /* =============================================
       TYPOGRAPHY
       ============================================= */
    --font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Microsoft JhengHei', 'Noto Sans TC', sans-serif;
    --font-family-mono: 'JetBrains Mono', 'SF Mono', 'Consolas', monospace;

    --font-size-xs: 0.75rem;    /* 12px */
    --font-size-sm: 0.875rem;   /* 14px */
    --font-size-base: 1rem;     /* 16px */
    --font-size-lg: 1.125rem;   /* 18px */
    --font-size-xl: 1.25rem;    /* 20px */
    --font-size-2xl: 1.5rem;    /* 24px */
    --font-size-3xl: 1.875rem;  /* 30px */
    --font-size-4xl: 2.25rem;   /* 36px */

    --font-weight-normal: 400;
    --font-weight-medium: 500;
    --font-weight-semibold: 600;
    --font-weight-bold: 700;

    --line-height-tight: 1.25;
    --line-height-normal: 1.5;
    --line-height-relaxed: 1.75;

    /* =============================================
       BORDER RADIUS
       ============================================= */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;
    --radius-xl: 16px;
    --radius-2xl: 24px;
    --radius-full: 9999px;

    /* =============================================
       SHADOWS
       ============================================= */
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
    --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);
    --shadow-card: 0 4px 15px rgba(0, 0, 0, 0.1);
    --shadow-card-hover: 0 8px 25px rgba(0, 0, 0, 0.15);

    /* =============================================
       TRANSITIONS
       ============================================= */
    --transition-fast: 150ms ease;
    --transition-normal: 200ms ease;
    --transition-slow: 300ms ease;

    /* =============================================
       Z-INDEX SCALE
       ============================================= */
    --z-dropdown: 100;
    --z-sticky: 200;
    --z-fixed: 300;
    --z-modal-backdrop: 400;
    --z-modal: 500;
    --z-popover: 600;
    --z-tooltip: 700;
}
```

### 3.2 Base Styles

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

html {
    font-size: 16px;
    -webkit-text-size-adjust: 100%;
}

body {
    font-family: var(--font-family-base);
    font-size: var(--font-size-base);
    line-height: var(--line-height-normal);
    color: var(--text-primary);
    background-color: var(--bg-primary);
    -webkit-tap-highlight-color: transparent;
}
```

---

## 4. Dark Theme Patterns

Most teaching apps use dark themes for better readability. Here are the standard patterns:

### 4.1 Dark Background (PAOD/Cath Lab Style)

```css
body {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    min-height: 100vh;
    color: #e8e8e8;
}
```

### 4.2 Alternative Dark Theme (AF/Ward Style)

```css
:root {
    --bg-primary: #0a0f1a;
    --bg-secondary: #111827;
    --accent-teal: #14b8a6;
}

body {
    background: var(--bg-primary);
    background-image: radial-gradient(ellipse at 20% 0%, rgba(20, 184, 166, 0.08) 0%, transparent 50%);
}
```

### 4.3 Blue-Cyan Theme (ACS/HF Style)

```css
:root {
    --bg-primary: #0a0f1a;
    --accent-blue: #3b82f6;
    --accent-cyan: #06b6d4;
    --gradient-primary: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);
}
```

---

## 5. Component Templates

### 5.1 Sticky Header

```css
.header {
    background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
    color: white;
    padding: 20px 15px;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 4px 20px rgba(233, 69, 96, 0.4);
}

.header h1 {
    font-size: 1.4em;
    margin-bottom: 5px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.header p {
    font-size: 0.85em;
    opacity: 0.95;
}

.header-badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    padding: 3px 10px;
    border-radius: 15px;
    font-size: 0.7em;
    margin-top: 5px;
}
```

### 5.2 Horizontal Scrollable Navigation Tabs

```css
.nav-tabs {
    display: flex;
    overflow-x: auto;
    background: rgba(22, 33, 62, 0.95);
    padding: 10px;
    gap: 8px;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    border-bottom: 2px solid #e94560;
}

.nav-tabs::-webkit-scrollbar {
    display: none;
}

.nav-tab {
    flex-shrink: 0;
    padding: 10px 16px;
    border-radius: 25px;
    border: none;
    background: rgba(233, 69, 96, 0.2);
    color: #e8e8e8;
    cursor: pointer;
    font-size: 0.85em;
    transition: all 0.3s ease;
    white-space: nowrap;
}

.nav-tab.active {
    background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
    color: white;
    box-shadow: 0 4px 15px rgba(233, 69, 96, 0.4);
}
```

### 5.3 Card Component (Glass Effect)

```css
.card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 15px;
    border: 1px solid rgba(233, 69, 96, 0.2);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(233, 69, 96, 0.2);
}

.card-title {
    color: #ff6b6b;
    font-size: 1.1em;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(233, 69, 96, 0.3);
}

.card-icon {
    font-size: 1.3em;
}
```

### 5.4 Info/Warning/Danger/Success Boxes

```css
/* Warning Box */
.warning-box {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.15) 0%, rgba(255, 152, 0, 0.15) 100%);
    border: 1px solid #ffc107;
    border-radius: 12px;
    padding: 15px;
    margin: 12px 0;
}

.warning-title {
    color: #ffc107;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}

/* Danger Box */
.danger-box {
    background: linear-gradient(135deg, rgba(244, 67, 54, 0.15) 0%, rgba(233, 30, 99, 0.15) 100%);
    border: 1px solid #f44336;
    border-radius: 12px;
    padding: 15px;
    margin: 12px 0;
}

.danger-title {
    color: #f44336;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}

/* Success Box */
.success-box {
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.15) 0%, rgba(102, 187, 106, 0.15) 100%);
    border: 1px solid #4caf50;
    border-radius: 12px;
    padding: 15px;
    margin: 12px 0;
}

.success-title {
    color: #4caf50;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}

/* Info Box */
.info-box {
    background: linear-gradient(135deg, rgba(33, 150, 243, 0.15) 0%, rgba(3, 169, 244, 0.15) 100%);
    border: 1px solid #2196f3;
    border-radius: 12px;
    padding: 15px;
    margin: 12px 0;
}

.info-box-title {
    color: #2196f3;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}
```

### 5.5 Checklist Items with Toggle

```css
.checklist-item {
    display: flex;
    align-items: flex-start;
    padding: 12px;
    margin: 8px 0;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.checklist-item:hover {
    background: rgba(233, 69, 96, 0.1);
}

.checkbox {
    width: 24px;
    height: 24px;
    border: 2px solid #e94560;
    border-radius: 6px;
    margin-right: 12px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
}

.checkbox.checked {
    background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
}

.checklist-text {
    flex: 1;
    font-size: 0.9em;
    line-height: 1.5;
}
```

### 5.6 Data Table

```css
.data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85em;
}

.data-table th {
    background: rgba(233, 69, 96, 0.3);
    padding: 12px 10px;
    color: #ff8a8a;
    font-weight: bold;
    text-align: left;
}

.data-table td {
    padding: 10px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.data-table tr:hover {
    background: rgba(233, 69, 96, 0.1);
}

/* Responsive table wrapper */
.table-responsive {
    overflow-x: auto;
    margin: 15px 0;
    -webkit-overflow-scrolling: touch;
}
```

---

## 6. Share Button Implementation

### 6.1 Share Button CSS

Add this CSS inside your `<style>` block:

```css
/* Share Button - Fixed Position */
.share-button {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
}

.share-toggle {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: linear-gradient(135deg, #3B82F6 0%, #60A5FA 100%);
    border: none;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}

.share-toggle:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5);
}

.share-menu {
    position: absolute;
    top: 60px;
    right: 0;
    background: white;
    border-radius: 16px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    padding: 20px;
    min-width: 280px;
    display: none;
    animation: fadeInShare 0.3s ease;
}

.share-menu.active {
    display: block;
}

@keyframes fadeInShare {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

.share-menu h4 {
    color: #1e293b;
    margin: 0 0 15px 0;
    font-size: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}

.qr-container {
    background: #f8fafc;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    margin-bottom: 15px;
}

.qr-container img {
    max-width: 150px;
    height: auto;
    border-radius: 8px;
}

.qr-container p {
    font-size: 0.75rem;
    color: #64748b;
    margin: 8px 0 0 0;
}

.share-buttons {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.share-btn {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-size: 0.95rem;
    font-weight: 500;
    transition: all 0.2s ease;
    text-decoration: none;
    color: white;
}

.share-btn.line { background: #00B900; }
.share-btn.email { background: #EA4335; }
.share-btn.copy { background: #3B82F6; }

.share-btn:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.share-btn svg {
    width: 20px;
    height: 20px;
    fill: currentColor;
}

.share-close {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #64748b;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
}

.share-close:hover {
    color: #1e293b;
}
```

### 6.2 Share Button HTML

Place this immediately after `<body>`:

```html
<!-- Share Button -->
<div class="share-button">
    <button class="share-toggle" onclick="toggleShareMenu()" title="Share this page">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
            <path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92s2.92-1.31 2.92-2.92-1.31-2.92-2.92-2.92z"/>
        </svg>
    </button>
    <div class="share-menu" id="shareMenu">
        <button class="share-close" onclick="toggleShareMenu()">&times;</button>
        <h4>Share this page</h4>
        <div class="qr-container">
            <img id="qrCode" src="" alt="QR Code">
            <p>Scan QR Code to open page</p>
        </div>
        <div class="share-buttons">
            <a class="share-btn line" href="#" id="lineShare" target="_blank">
                <svg viewBox="0 0 24 24"><path d="M19.365 9.863c.349 0 .63.285.63.631 0 .345-.281.63-.63.63H17.61v1.125h1.755c.349 0 .63.283.63.63 0 .344-.281.629-.63.629h-2.386c-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.627-.63h2.386c.349 0 .63.285.63.63 0 .349-.281.63-.63.63H17.61v1.125h1.755zm-3.855 3.016c0 .27-.174.51-.432.596-.064.021-.133.031-.199.031-.211 0-.391-.09-.51-.25l-2.443-3.317v2.94c0 .344-.279.629-.631.629-.346 0-.626-.285-.626-.629V8.108c0-.27.173-.51.43-.595.06-.023.136-.033.194-.033.195 0 .375.104.495.254l2.462 3.33V8.108c0-.345.282-.63.63-.63.345 0 .63.285.63.63v4.771zm-5.741 0c0 .344-.282.629-.631.629-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.627-.63.349 0 .631.285.631.63v4.771zm-2.466.629H4.917c-.345 0-.63-.285-.63-.629V8.108c0-.345.285-.63.63-.63.349 0 .63.285.63.63v4.141h1.756c.348 0 .629.283.629.63 0 .344-.281.629-.629.629M24 10.314C24 4.943 18.615.572 12 .572S0 4.943 0 10.314c0 4.811 4.27 8.842 10.035 9.608.391.082.923.258 1.058.59.12.301.079.766.038 1.08l-.164 1.02c-.045.301-.24 1.186 1.049.645 1.291-.539 6.916-4.078 9.436-6.975C23.176 14.393 24 12.458 24 10.314"/></svg>
                LINE Share
            </a>
            <a class="share-btn email" href="#" id="emailShare">
                <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                Email Share
            </a>
            <button class="share-btn copy" onclick="copyPageUrl()">
                <svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
                Copy Link
            </button>
        </div>
    </div>
</div>
```

### 6.3 Share Button JavaScript

Place this before `</body>`:

```html
<script>
    function initShareButtons() {
        const pageUrl = window.location.href;
        const pageTitle = document.title;
        const encodedUrl = encodeURIComponent(pageUrl);

        // QR Code generation using api.qrserver.com
        const qrCodeImg = document.getElementById('qrCode');
        if (qrCodeImg) {
            qrCodeImg.src = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${encodedUrl}`;
        }

        // LINE share
        const lineShare = document.getElementById('lineShare');
        if (lineShare) {
            lineShare.href = `https://social-plugins.line.me/lineit/share?url=${encodedUrl}`;
        }

        // Email share
        const emailShare = document.getElementById('emailShare');
        if (emailShare) {
            const emailSubject = encodeURIComponent(`Share: ${pageTitle}`);
            const emailBody = encodeURIComponent(`I want to share this page with you:\n\n${pageTitle}\n\n${pageUrl}`);
            emailShare.href = `mailto:?subject=${emailSubject}&body=${emailBody}`;
        }
    }

    function toggleShareMenu() {
        const menu = document.getElementById('shareMenu');
        if (menu) menu.classList.toggle('active');
    }

    function copyPageUrl() {
        const pageUrl = window.location.href;
        navigator.clipboard.writeText(pageUrl)
            .then(() => {
                alert('Link copied to clipboard!');
            })
            .catch(() => {
                // Fallback for older browsers
                const textArea = document.createElement('textarea');
                textArea.value = pageUrl;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                alert('Link copied to clipboard!');
            });
    }

    // Close menu on outside click
    document.addEventListener('click', function(event) {
        const shareButton = document.querySelector('.share-button');
        const shareMenu = document.getElementById('shareMenu');
        if (shareButton && shareMenu &&
            !shareButton.contains(event.target) &&
            shareMenu.classList.contains('active')) {
            shareMenu.classList.remove('active');
        }
    });

    // Initialize on page load
    document.addEventListener('DOMContentLoaded', initShareButtons);
</script>
```

---

## 7. React Component Patterns

### 7.1 Main App Structure

```jsx
const { useState, useEffect, useRef } = React;

const App = () => {
    const [currentTab, setCurrentTab] = useState('overview');
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

    const renderContent = () => {
        switch(currentTab) {
            case 'overview': return <OverviewTab />;
            case 'details': return <DetailsTab />;
            case 'quiz': return <QuizTab />;
            default: return <OverviewTab />;
        }
    };

    return (
        <div className="app-container">
            <Header currentTab={currentTab} setCurrentTab={setCurrentTab} />
            <main>{renderContent()}</main>
            <Footer />
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));
```

### 7.2 Quiz Module Template

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
            <h3>Question {currentQ + 1} / {questions.length}</h3>
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
                    <p>{selected === q.correct ? 'Correct!' : 'Incorrect'}</p>
                    <p>{q.explanation}</p>
                    <button onClick={nextQuestion}>
                        {currentQ < questions.length - 1 ? 'Next' : 'View Results'}
                    </button>
                </div>
            )}
        </div>
    );
};
```

### 7.3 Interactive Checklist Template

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
                    <div className={`checkbox ${checked[item.id] ? 'checked' : ''}`}>
                        {checked[item.id] && '✓'}
                    </div>
                    <span className="checklist-text">{item.text}</span>
                </div>
            ))}
        </div>
    );
};
```

---

## 8. Reference Requirements

**IMPORTANT: Every educational app MUST include proper references with hyperlinks.**

### 8.1 Reference Format on Title Page

Add a clickable reference section below the main description:

```jsx
<div className="reference-section">
    <a href="[CORRECT_URL]" target="_blank" rel="noopener noreferrer">
        <p className="reference-text">
            Reference: [Authors]. <em>[Title].</em>
        </p>
        <p className="reference-journal">
            [Journal Year; Volume: Pages]
        </p>
    </a>
</div>
```

### 8.2 Hyperlink Verification Checklist

- [ ] **Always verify the hyperlink is correct** before committing
- [ ] Test the link opens to the correct paper/resource
- [ ] Prefer official publisher links (e.g., Springer, Elsevier, PubMed)
- [ ] Use DOI links (`https://doi.org/...`) or direct publisher URLs
- [ ] **Never guess DOI numbers** - verify from the actual paper or search

### 8.3 Example Reference Format

```
Reference: Saura O, Combes A, Hekimian G. My echo checklist in venoarterial ECMO patients.
Intensive Care Med 2024; 50: 2158-2161
```
Link: `https://link.springer.com/article/10.1007/s00134-024-07659-2`

---

## 9. Mobile Responsiveness

### 9.1 Viewport Meta Tag

Always include:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
```

### 9.2 Responsive Breakpoints

```css
/* Extra small phones */
@media (max-width: 360px) {
    .header h1 { font-size: 1.2em; }
    .nav-tabs { padding: 8px; gap: 4px; }
}

/* Small phones */
@media (max-width: 480px) {
    .app-container { padding: 10px; }
    .data-table { font-size: 0.75em; }
    .assessment-grid { grid-template-columns: 1fr; }
}

/* Tablets */
@media (max-width: 640px) {
    .grid-layout { grid-template-columns: 1fr; }
}

/* Desktop */
@media (min-width: 768px) {
    .grid-layout { grid-template-columns: repeat(2, 1fr); }
}
```

### 9.3 Touch-Friendly Elements

```css
/* Minimum touch target size */
.button, .nav-tab, .checklist-item {
    min-height: 48px;
    padding: 12px 16px;
}

/* Prevent zoom on input focus (iOS) */
input, select, textarea {
    font-size: 16px;
}

/* Safe area for notched phones */
.app-container {
    padding-bottom: env(safe-area-inset-bottom);
}

/* Smooth scrolling on iOS */
.scrollable {
    -webkit-overflow-scrolling: touch;
}
```

---

## 10. Language Rules

### 10.1 Main UI Language
- Use **Traditional Chinese (繁體中文)** for all user interface text

### 10.2 Preserve English For
- Drug names (medications)
- Medical terminology
- Procedure names
- Lab tests
- Anatomical terms in parentheses

### 10.3 Bilingual Format Example
```
"股動脈 (Femoral Artery)"
"Heparin 5000 units"
"心房顫動 (Atrial Fibrillation, AF)"
```

---

## 11. Application Categories

Map new applications to these categories:

| Category | Class | Color | Description |
|----------|-------|-------|-------------|
| 導管室教學 | `cath` | Red (#e74c3c) | Cath lab procedures, protocols, hemostasis |
| 病房照護 | `ward` | Blue (#3498db) | Ward care, post-procedure, monitoring |
| 加護病房 | `icu` | Cyan (#00d4ff) | ICU/CCU, critical care |
| 介入治療 | `intervention` | Purple (#9b59b6) | PTMC, LAAO, TEER, carotid |
| 藥物學習 | `medication` | Green (#27ae60) | Drug protocols, calculators |
| 病人衛教 | `patient` | Orange (#f39c12) | Patient-facing content |
| 學習資源 | `learning` | Teal (#1abc9c) | Lectures, guidelines, cases |

---

## 12. Post-Creation Actions

### 12.1 Update index.html

After creating a new app, add a card in the appropriate section of `index.html`:

```html
<a href="[new-app-filename].html" class="app-card [category]" data-tags="[space-separated tags]">
    <div class="app-icon">[emoji]</div>
    <div class="app-title">[Chinese Title]</div>
    <div class="app-desc">[Brief Description]</div>
    <div class="app-tags">
        <span class="tag staff">Staff</span>
        <span class="tag new">New</span>
        <span class="tag">[additional tag]</span>
    </div>
</a>
```

### 12.2 Tag Classes Reference

| Class | Color | Usage |
|-------|-------|-------|
| `tag.staff` | Blue | For medical staff |
| `tag.patient` | Orange | For patient education |
| `tag.new` | Green | Recently added |
| `tag.updated` | Pink | Recently updated |
| `tag.icu` | Cyan | ICU/Critical care |

### 12.3 Update Category Count

Update the `<span class="category-count">` element in the corresponding section header.

---

## 13. File Naming Convention

### Format
```
[topic]-[type]-app.html
```

### Examples
- `cath-wound-care-app.html`
- `warfarin-dosing-calculator.html`
- `af-ward-teaching-app.html`
- `tee-interpretation-guide.html`
- `paod-care-app.html`
- `cardiogenic-shock-teaching.html`

---

## 14. Quality Checklist

Before finalizing any application:

- [ ] Mobile viewport meta tag included
- [ ] Touch targets ≥ 48px
- [ ] localStorage progress persistence working
- [ ] All interactive elements have visual feedback
- [ ] Quiz has immediate feedback with explanations
- [ ] Medical content reviewed for Taiwan-specific accuracy
- [ ] Drug names remain in English
- [ ] Bilingual terminology format: 中文 (English)
- [ ] Dark theme works properly (if applicable)
- [ ] No external dependencies requiring installation
- [ ] **Reference with hyperlink** added to title page
- [ ] **Hyperlinks verified** - all URLs are correct and working
- [ ] Share button functional (QR, LINE, Email, Copy)

---

## 15. Git Workflow

### Repository
- **GitHub:** `https://github.com/drake1128/saq-questionnaire`
- **Branch:** `main`

### After Every Change

```bash
# Stage files
git add [files]

# Commit with descriptive message
git commit -m "Add [component] - [description]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

# Push to GitHub
git push origin main
```

### Commit Message Format
```
[Action] [Component/File] - [Brief description]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### Examples
- `Add VA-ECMO Echo Checklist teaching app`
- `Fix reference hyperlink to correct Springer URL`
- `Update index.html with new app link`
- `Add share functionality to 49 HTML pages`

---

## Quick Reference Card

### Essential CDN URLs
```
React 18:     https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js
ReactDOM 18:  https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js
Babel:        https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.5/babel.min.js
Noto Sans TC: https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700&display=swap
```

### QR Code API
```
https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={encodedUrl}
```

### LINE Share URL
```
https://social-plugins.line.me/lineit/share?url={encodedUrl}
```

---

*Document created: 2026-01*
*Project: NTUH Hsinchu Cardiovascular Care Education Hub*
