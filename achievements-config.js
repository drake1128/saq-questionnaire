/**
 * Achievement System Configuration
 * 心血管照護教學資源中心 - 成就系統設定
 */

const ACHIEVEMENT_CONFIG = {
    version: "1.0.0",

    // Level thresholds
    levels: [
        { level: 1, minPoints: 0, title: "新手學員" },
        { level: 2, minPoints: 100, title: "初階學員" },
        { level: 3, minPoints: 250, title: "進階學員" },
        { level: 4, minPoints: 500, title: "資深學員" },
        { level: 5, minPoints: 1000, title: "專家級" },
        { level: 6, minPoints: 2000, title: "大師級" }
    ],

    // Category mapping for pages
    pageCategories: {
        // Cath Lab
        "cath-handoff-teaching-app.html": "cath",
        "cath-nursing-exam-100.html": "cath",
        "cin-prevention-app.html": "cath",
        "pci-complications-emergency.html": "cath",
        // Ward & ICU
        "va-ecmo-echo-checklist.html": "ward",
        "icu-pocus.html": "ward",
        "cardiogenic-shock-teaching.html": "ward",
        "heart-failure-ward-app.html": "ward",
        "af-ward-teaching-app.html": "ward",
        "paod-care-app.html": "ward",
        "cv-vaccination-guide.html": "ward",
        "ph-diagnostic-checklist.html": "ward",
        "fabry-disease-checklist.html": "ward",
        "emb-teaching-app.html": "ward",
        "ilvd-revascularization-app.html": "ward",
        // Intervention
        "ptmc-teaching-app.html": "intervention",
        "carotid-stenting-app.html": "intervention",
        "laao-tee-evaluation-app.html": "intervention",
        "teer-tee-checklist-app.html": "intervention",
        // Medication
        "warfarin-dosing-app.html": "medication",
        "thrombolytic-calculator-app.html": "medication",
        "cardiac-surgery-medication-app.html": "medication",
        "acs-hf-medication-learning.html": "medication",
        // Patient Education
        "cto-pci-patient-education.html": "patient",
        "hypertension-education-app.html": "patient",
        "seattle-saq.html": "patient",
        "kccq.html": "patient",
        "ldl-education-app.html": "patient",
        "echo-education-app.html": "patient",
        // Learning
        "exam.html": "learning",
        "pci-complications-case-teaching.html": "learning",
        "thoracic-ultrasound-teaching.html": "learning",
        "hemodynamic-shock-teaching-app.html": "learning",
        "troponin-lecture.html": "learning",
        "tsoc-echo-learning-2025.html": "learning",
        // Administrative
        "cv_center_checklist.html": "admin",
        "ccu-orientation-manual.html": "admin",
        "cardiology-ward-orientation-2025.html": "admin"
    },

    // Category totals for completion tracking
    categoryTotals: {
        cath: 4,
        ward: 11,
        intervention: 4,
        medication: 4,
        patient: 6,
        learning: 6,
        admin: 3
    },

    // Achievement definitions
    achievements: {
        // ===== Quiz Achievements (測驗成就) =====
        "quiz-first": {
            id: "quiz-first",
            category: "quiz",
            icon: "🎯",
            titleZh: "初試啼聲",
            titleEn: "First Quiz",
            descZh: "完成第一個測驗",
            descEn: "Complete your first quiz",
            points: 10,
            tier: "bronze",
            criteria: { type: "quiz_count", count: 1 }
        },
        "quiz-ace": {
            id: "quiz-ace",
            category: "quiz",
            icon: "🏆",
            titleZh: "滿分達人",
            titleEn: "Perfect Score",
            descZh: "在任一測驗中獲得滿分",
            descEn: "Get 100% on any quiz",
            points: 50,
            tier: "gold",
            criteria: { type: "quiz_perfect", score: 100 }
        },
        "quiz-scholar": {
            id: "quiz-scholar",
            category: "quiz",
            icon: "📚",
            titleZh: "學海無涯",
            titleEn: "Quiz Scholar",
            descZh: "完成 3 個不同的測驗",
            descEn: "Complete 3 different quizzes",
            points: 30,
            tier: "silver",
            criteria: { type: "quiz_count", count: 3 }
        },
        "quiz-persistent": {
            id: "quiz-persistent",
            category: "quiz",
            icon: "💪",
            titleZh: "屢敗屢戰",
            titleEn: "Persistent Learner",
            descZh: "重考並提升分數",
            descEn: "Retake a quiz and improve your score",
            points: 20,
            tier: "silver",
            criteria: { type: "quiz_improved" }
        },

        // ===== Exploration Achievements (探索成就) =====
        "explorer-first": {
            id: "explorer-first",
            category: "exploration",
            icon: "👣",
            titleZh: "初來乍到",
            titleEn: "First Steps",
            descZh: "訪問第一個教學頁面",
            descEn: "Visit your first learning page",
            points: 5,
            tier: "bronze",
            criteria: { type: "pages_visited", count: 1 }
        },
        "explorer-curious": {
            id: "explorer-curious",
            category: "exploration",
            icon: "🔍",
            titleZh: "求知若渴",
            titleEn: "Curious Mind",
            descZh: "訪問 10 個不同頁面",
            descEn: "Visit 10 different pages",
            points: 25,
            tier: "silver",
            criteria: { type: "pages_visited", count: 10 }
        },
        "explorer-dedicated": {
            id: "explorer-dedicated",
            category: "exploration",
            icon: "📖",
            titleZh: "勤學不倦",
            titleEn: "Dedicated Learner",
            descZh: "訪問 25 個不同頁面",
            descEn: "Visit 25 different pages",
            points: 50,
            tier: "gold",
            criteria: { type: "pages_visited", count: 25 }
        },
        "cath-expert": {
            id: "cath-expert",
            category: "exploration",
            icon: "🏥",
            titleZh: "導管室專家",
            titleEn: "Cath Lab Expert",
            descZh: "完成所有導管室教學內容",
            descEn: "Complete all Cath Lab content",
            points: 40,
            tier: "gold",
            criteria: { type: "category_complete", categoryId: "cath" }
        },
        "ward-expert": {
            id: "ward-expert",
            category: "exploration",
            icon: "🛏️",
            titleZh: "病房達人",
            titleEn: "Ward Expert",
            descZh: "完成所有病房與ICU內容",
            descEn: "Complete all Ward & ICU content",
            points: 60,
            tier: "gold",
            criteria: { type: "category_complete", categoryId: "ward" }
        },
        "intervention-expert": {
            id: "intervention-expert",
            category: "exploration",
            icon: "🔬",
            titleZh: "介入治療專家",
            titleEn: "Intervention Expert",
            descZh: "完成所有介入治療內容",
            descEn: "Complete all Intervention content",
            points: 40,
            tier: "gold",
            criteria: { type: "category_complete", categoryId: "intervention" }
        },
        "medication-master": {
            id: "medication-master",
            category: "exploration",
            icon: "💊",
            titleZh: "藥物學家",
            titleEn: "Medication Master",
            descZh: "完成所有藥物學習內容",
            descEn: "Complete all Medication content",
            points: 40,
            tier: "gold",
            criteria: { type: "category_complete", categoryId: "medication" }
        },
        "patient-educator": {
            id: "patient-educator",
            category: "exploration",
            icon: "👥",
            titleZh: "衛教先鋒",
            titleEn: "Patient Educator",
            descZh: "完成所有病人衛教內容",
            descEn: "Complete all Patient Education content",
            points: 40,
            tier: "gold",
            criteria: { type: "category_complete", categoryId: "patient" }
        },
        "completionist": {
            id: "completionist",
            category: "exploration",
            icon: "🌟",
            titleZh: "全能王者",
            titleEn: "Completionist",
            descZh: "訪問所有教學頁面",
            descEn: "Visit all learning pages",
            points: 100,
            tier: "platinum",
            criteria: { type: "pages_visited", count: 38 }
        },

        // ===== Milestone Achievements (里程碑成就) =====
        "streak-3": {
            id: "streak-3",
            category: "milestone",
            icon: "🔥",
            titleZh: "連續學習",
            titleEn: "Learning Streak",
            descZh: "連續 3 天訪問網站",
            descEn: "Visit the site 3 days in a row",
            points: 15,
            tier: "bronze",
            criteria: { type: "streak", days: 3 }
        },
        "streak-7": {
            id: "streak-7",
            category: "milestone",
            icon: "🔥",
            titleZh: "週末不休息",
            titleEn: "Week Warrior",
            descZh: "連續 7 天訪問網站",
            descEn: "Visit the site 7 days in a row",
            points: 35,
            tier: "silver",
            criteria: { type: "streak", days: 7 }
        },
        "streak-30": {
            id: "streak-30",
            category: "milestone",
            icon: "🔥",
            titleZh: "月度學霸",
            titleEn: "Monthly Champion",
            descZh: "連續 30 天訪問網站",
            descEn: "Visit the site 30 days in a row",
            points: 100,
            tier: "platinum",
            criteria: { type: "streak", days: 30 }
        },
        "early-bird": {
            id: "early-bird",
            category: "milestone",
            icon: "🌅",
            titleZh: "早起的鳥兒",
            titleEn: "Early Bird",
            descZh: "在早上 6-8 點訪問網站",
            descEn: "Visit the site between 6-8 AM",
            points: 10,
            tier: "bronze",
            criteria: { type: "time_visit", startHour: 6, endHour: 8 }
        },
        "night-owl": {
            id: "night-owl",
            category: "milestone",
            icon: "🦉",
            titleZh: "夜貓子",
            titleEn: "Night Owl",
            descZh: "在晚上 10 點後訪問網站",
            descEn: "Visit the site after 10 PM",
            points: 10,
            tier: "bronze",
            criteria: { type: "time_visit", startHour: 22, endHour: 24 }
        },
        "veteran": {
            id: "veteran",
            category: "milestone",
            icon: "🏅",
            titleZh: "資深學員",
            titleEn: "Veteran",
            descZh: "累計訪問超過 50 次",
            descEn: "Accumulate 50+ total visits",
            points: 50,
            tier: "gold",
            criteria: { type: "total_visits", count: 50 }
        },

        // ===== Special Achievements (特殊成就) =====
        "share-friend": {
            id: "share-friend",
            category: "special",
            icon: "🤝",
            titleZh: "知識傳播者",
            titleEn: "Knowledge Sharer",
            descZh: "分享網站給朋友",
            descEn: "Share the website with friends",
            points: 15,
            tier: "bronze",
            criteria: { type: "share_action" }
        },
        "welcome": {
            id: "welcome",
            category: "special",
            icon: "👋",
            titleZh: "歡迎加入",
            titleEn: "Welcome",
            descZh: "開始使用成就系統",
            descEn: "Start using the achievement system",
            points: 5,
            tier: "bronze",
            criteria: { type: "first_visit" }
        }
    }
};

// Make available globally
if (typeof window !== 'undefined') {
    window.ACHIEVEMENT_CONFIG = ACHIEVEMENT_CONFIG;
}
