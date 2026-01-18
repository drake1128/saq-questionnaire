/**
 * Achievement Tracking System
 * 心血管照護教學資源中心 - 成就追蹤系統
 */

(function(window) {
    'use strict';

    const STORAGE_KEY = 'cv-education-user-data';
    const VERSION = '1.0.0';

    const AchievementTracker = {
        userData: null,
        initialized: false,

        // Initialize tracker
        init: function() {
            if (this.initialized) return;

            this.loadUserData();
            this.migrateOldData();
            this.trackPageVisit();
            this.updateStreak();
            this.checkTimeBasedAchievements();
            this.checkAllAchievements();
            this.updateUI();
            this.initialized = true;

            // Check for welcome achievement
            if (!this.userData.achievements['welcome']) {
                this.unlockAchievement('welcome');
            }
        },

        // Create default user data structure
        createDefaultData: function() {
            return {
                version: VERSION,
                lastUpdated: new Date().toISOString(),
                profile: {
                    totalPoints: 0,
                    level: 1,
                    joinDate: new Date().toISOString()
                },
                achievements: {},
                progress: {
                    quizzes: {},
                    pagesVisited: {},
                    categories: {},
                    streaks: {
                        currentStreak: 0,
                        longestStreak: 0,
                        lastVisitDate: null
                    },
                    stats: {
                        totalVisits: 0,
                        shareCount: 0
                    }
                }
            };
        },

        // Load user data from localStorage
        loadUserData: function() {
            try {
                const data = localStorage.getItem(STORAGE_KEY);
                this.userData = data ? JSON.parse(data) : this.createDefaultData();

                // Ensure all required properties exist
                if (!this.userData.progress) {
                    this.userData.progress = this.createDefaultData().progress;
                }
                if (!this.userData.progress.categories) {
                    this.userData.progress.categories = {};
                }
                if (!this.userData.progress.stats) {
                    this.userData.progress.stats = { totalVisits: 0, shareCount: 0 };
                }
            } catch (e) {
                console.error('Error loading achievement data:', e);
                this.userData = this.createDefaultData();
            }
        },

        // Save user data to localStorage
        saveUserData: function() {
            try {
                this.userData.lastUpdated = new Date().toISOString();
                localStorage.setItem(STORAGE_KEY, JSON.stringify(this.userData));
            } catch (e) {
                console.error('Error saving achievement data:', e);
            }
        },

        // Migrate old localStorage data (existing quiz scores)
        migrateOldData: function() {
            const oldKeys = [
                'exam-echo-as-score',
                'exam-vascular-abi-score'
            ];

            oldKeys.forEach(key => {
                const score = localStorage.getItem(key);
                if (score && !this.userData.progress.quizzes[key]) {
                    this.userData.progress.quizzes[key] = {
                        score: parseInt(score, 10),
                        completedAt: new Date().toISOString(),
                        attempts: 1
                    };
                }
            });

            this.saveUserData();
        },

        // Track page visit
        trackPageVisit: function() {
            const page = window.location.pathname.split('/').pop() || 'index.html';

            // Skip tracking for index.html visits for page count (but track for stats)
            const isIndexPage = page === 'index.html' || page === '';

            if (!this.userData.progress.pagesVisited[page]) {
                this.userData.progress.pagesVisited[page] = {
                    firstVisit: new Date().toISOString(),
                    visits: 0
                };
            }

            this.userData.progress.pagesVisited[page].visits++;
            this.userData.progress.stats.totalVisits++;

            // Update category progress
            if (!isIndexPage) {
                this.updateCategoryProgress(page);
            }

            this.saveUserData();
        },

        // Update category progress
        updateCategoryProgress: function(page) {
            if (!window.ACHIEVEMENT_CONFIG) return;

            const categoryId = ACHIEVEMENT_CONFIG.pageCategories[page];
            if (!categoryId) return;

            if (!this.userData.progress.categories[categoryId]) {
                this.userData.progress.categories[categoryId] = {
                    visited: [],
                    completed: false
                };
            }

            const cat = this.userData.progress.categories[categoryId];
            if (!cat.visited.includes(page)) {
                cat.visited.push(page);
            }

            // Check if category is complete
            const total = ACHIEVEMENT_CONFIG.categoryTotals[categoryId] || 0;
            if (cat.visited.length >= total) {
                cat.completed = true;
            }

            this.saveUserData();
        },

        // Update streak
        updateStreak: function() {
            const today = new Date().toISOString().split('T')[0];
            const streaks = this.userData.progress.streaks;

            if (!streaks.lastVisitDate) {
                streaks.currentStreak = 1;
                streaks.lastVisitDate = today;
            } else if (streaks.lastVisitDate === today) {
                // Already visited today, no change
                return;
            } else {
                const lastDate = new Date(streaks.lastVisitDate);
                const todayDate = new Date(today);
                const diffDays = Math.floor((todayDate - lastDate) / (1000 * 60 * 60 * 24));

                if (diffDays === 1) {
                    // Consecutive day
                    streaks.currentStreak++;
                } else {
                    // Streak broken
                    streaks.currentStreak = 1;
                }

                streaks.lastVisitDate = today;
            }

            // Update longest streak
            if (streaks.currentStreak > streaks.longestStreak) {
                streaks.longestStreak = streaks.currentStreak;
            }

            this.saveUserData();
        },

        // Check time-based achievements
        checkTimeBasedAchievements: function() {
            const hour = new Date().getHours();

            // Early bird: 6-8 AM
            if (hour >= 6 && hour < 8) {
                this.unlockAchievement('early-bird');
            }

            // Night owl: 10 PM - midnight
            if (hour >= 22) {
                this.unlockAchievement('night-owl');
            }
        },

        // Track quiz completion
        trackQuizComplete: function(quizId, score) {
            const existing = this.userData.progress.quizzes[quizId];
            const improved = existing && score > existing.score;

            this.userData.progress.quizzes[quizId] = {
                score: score,
                completedAt: new Date().toISOString(),
                attempts: (existing?.attempts || 0) + 1,
                bestScore: Math.max(score, existing?.bestScore || 0)
            };

            this.saveUserData();
            this.checkQuizAchievements(quizId, score, improved);
        },

        // Check quiz-related achievements
        checkQuizAchievements: function(quizId, score, improved) {
            const quizCount = Object.keys(this.userData.progress.quizzes).length;

            // First quiz
            if (quizCount >= 1) {
                this.unlockAchievement('quiz-first');
            }

            // Quiz scholar (3 quizzes)
            if (quizCount >= 3) {
                this.unlockAchievement('quiz-scholar');
            }

            // Perfect score
            if (score >= 100) {
                this.unlockAchievement('quiz-ace');
            }

            // Improved score
            if (improved) {
                this.unlockAchievement('quiz-persistent');
            }
        },

        // Track share action
        trackShare: function() {
            this.userData.progress.stats.shareCount++;
            this.saveUserData();
            this.unlockAchievement('share-friend');
        },

        // Check all achievements
        checkAllAchievements: function() {
            if (!window.ACHIEVEMENT_CONFIG) return;

            const pageCount = Object.keys(this.userData.progress.pagesVisited).filter(
                p => p !== 'index.html' && p !== ''
            ).length;
            const totalVisits = this.userData.progress.stats.totalVisits;
            const currentStreak = this.userData.progress.streaks.currentStreak;

            // Exploration achievements
            if (pageCount >= 1) this.unlockAchievement('explorer-first');
            if (pageCount >= 10) this.unlockAchievement('explorer-curious');
            if (pageCount >= 25) this.unlockAchievement('explorer-dedicated');
            if (pageCount >= 38) this.unlockAchievement('completionist');

            // Category completion achievements
            const categories = this.userData.progress.categories;
            if (categories.cath?.completed) this.unlockAchievement('cath-expert');
            if (categories.ward?.completed) this.unlockAchievement('ward-expert');
            if (categories.intervention?.completed) this.unlockAchievement('intervention-expert');
            if (categories.medication?.completed) this.unlockAchievement('medication-master');
            if (categories.patient?.completed) this.unlockAchievement('patient-educator');

            // Streak achievements
            if (currentStreak >= 3) this.unlockAchievement('streak-3');
            if (currentStreak >= 7) this.unlockAchievement('streak-7');
            if (currentStreak >= 30) this.unlockAchievement('streak-30');

            // Veteran achievement
            if (totalVisits >= 50) this.unlockAchievement('veteran');
        },

        // Unlock an achievement
        unlockAchievement: function(achievementId) {
            if (this.userData.achievements[achievementId]) return; // Already unlocked
            if (!window.ACHIEVEMENT_CONFIG) return;

            const achievement = ACHIEVEMENT_CONFIG.achievements[achievementId];
            if (!achievement) return;

            this.userData.achievements[achievementId] = {
                unlockedAt: new Date().toISOString(),
                notified: false
            };

            this.userData.profile.totalPoints += achievement.points;
            this.updateLevel();
            this.saveUserData();
            this.showNotification(achievement);
            this.updateUI();
        },

        // Update user level based on points
        updateLevel: function() {
            if (!window.ACHIEVEMENT_CONFIG) return;

            const points = this.userData.profile.totalPoints;
            const levels = ACHIEVEMENT_CONFIG.levels;

            for (let i = levels.length - 1; i >= 0; i--) {
                if (points >= levels[i].minPoints) {
                    this.userData.profile.level = levels[i].level;
                    break;
                }
            }
        },

        // Show toast notification
        showNotification: function(achievement) {
            // Mark as notified
            if (this.userData.achievements[achievement.id]) {
                this.userData.achievements[achievement.id].notified = true;
                this.saveUserData();
            }

            // Remove existing toast if any
            const existingToast = document.querySelector('.achievement-toast');
            if (existingToast) {
                existingToast.remove();
            }

            // Create toast element
            const toast = document.createElement('div');
            toast.className = 'achievement-toast';
            toast.innerHTML = `
                <div class="toast-icon">🎉</div>
                <div class="toast-content">
                    <div class="toast-title">成就解鎖！</div>
                    <div class="toast-achievement">
                        <span class="toast-badge">${achievement.icon}</span>
                        <span>${achievement.titleZh}</span>
                    </div>
                    <div class="toast-points">+${achievement.points} 點</div>
                </div>
                <button class="toast-close" onclick="this.parentElement.remove()">&times;</button>
            `;

            document.body.appendChild(toast);

            // Auto-remove after 5 seconds
            setTimeout(() => {
                if (toast.parentElement) {
                    toast.classList.add('toast-fade-out');
                    setTimeout(() => toast.remove(), 500);
                }
            }, 5000);
        },

        // Update UI elements
        updateUI: function() {
            const pointsDisplay = document.querySelector('.profile-points');
            if (pointsDisplay) {
                pointsDisplay.textContent = this.userData.profile.totalPoints;
            }
        },

        // Get current progress data
        getProgress: function() {
            return this.userData;
        },

        // Get unlocked achievements count
        getUnlockedCount: function() {
            return Object.keys(this.userData.achievements).length;
        },

        // Get total achievements count
        getTotalAchievementsCount: function() {
            if (!window.ACHIEVEMENT_CONFIG) return 0;
            return Object.keys(ACHIEVEMENT_CONFIG.achievements).length;
        },

        // Get level info
        getLevelInfo: function() {
            if (!window.ACHIEVEMENT_CONFIG) return null;

            const points = this.userData.profile.totalPoints;
            const levels = ACHIEVEMENT_CONFIG.levels;
            let currentLevel = levels[0];
            let nextLevel = levels[1];

            for (let i = 0; i < levels.length; i++) {
                if (points >= levels[i].minPoints) {
                    currentLevel = levels[i];
                    nextLevel = levels[i + 1] || null;
                }
            }

            return {
                current: currentLevel,
                next: nextLevel,
                progress: nextLevel ?
                    ((points - currentLevel.minPoints) / (nextLevel.minPoints - currentLevel.minPoints)) * 100 :
                    100
            };
        },

        // Reset all progress (for testing)
        resetProgress: function() {
            if (confirm('確定要重置所有成就進度嗎？此操作無法復原。')) {
                localStorage.removeItem(STORAGE_KEY);
                this.userData = this.createDefaultData();
                this.saveUserData();
                this.updateUI();
                window.location.reload();
            }
        }
    };

    // Modal functions
    window.openAchievementsModal = function() {
        const modal = document.getElementById('achievementsModal');
        if (modal) {
            modal.classList.add('active');
            renderAchievementsModal();
        }
    };

    window.closeAchievementsModal = function(event) {
        if (!event || event.target === event.currentTarget) {
            const modal = document.getElementById('achievementsModal');
            if (modal) {
                modal.classList.remove('active');
            }
        }
    };

    window.filterAchievements = function(category) {
        const buttons = document.querySelectorAll('.achievements-tabs .tab');
        buttons.forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');

        const cards = document.querySelectorAll('.achievement-card');
        cards.forEach(card => {
            if (category === 'all' || card.dataset.category === category) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    };

    function renderAchievementsModal() {
        if (!window.ACHIEVEMENT_CONFIG || !AchievementTracker.userData) return;

        const userData = AchievementTracker.userData;
        const levelInfo = AchievementTracker.getLevelInfo();
        const streak = userData.progress.streaks.currentStreak;
        const unlockedCount = AchievementTracker.getUnlockedCount();
        const totalCount = AchievementTracker.getTotalAchievementsCount();

        // Update profile stats
        const statPoints = document.querySelector('.profile-stat-points');
        const statLevel = document.querySelector('.profile-stat-level');
        const statStreak = document.querySelector('.profile-stat-streak');

        if (statPoints) statPoints.textContent = userData.profile.totalPoints;
        if (statLevel) statLevel.textContent = levelInfo?.current?.title || 'Level ' + userData.profile.level;
        if (statStreak) statStreak.textContent = streak + '天';

        // Update level progress
        const levelFill = document.querySelector('.level-fill');
        const levelText = document.querySelector('.level-text');

        if (levelFill && levelInfo) {
            levelFill.style.width = levelInfo.progress + '%';
        }
        if (levelText && levelInfo?.next) {
            const pointsNeeded = levelInfo.next.minPoints - userData.profile.totalPoints;
            levelText.textContent = `距離 ${levelInfo.next.title} 還需 ${pointsNeeded} 點`;
        } else if (levelText) {
            levelText.textContent = '已達最高等級！';
        }

        // Render achievement cards
        const grid = document.querySelector('.achievements-grid');
        if (!grid) return;

        grid.innerHTML = '';

        const achievements = ACHIEVEMENT_CONFIG.achievements;
        const unlockedAchievements = userData.achievements;

        // Sort: unlocked first, then by tier
        const tierOrder = { platinum: 0, gold: 1, silver: 2, bronze: 3 };
        const sortedIds = Object.keys(achievements).sort((a, b) => {
            const aUnlocked = unlockedAchievements[a] ? 1 : 0;
            const bUnlocked = unlockedAchievements[b] ? 1 : 0;
            if (aUnlocked !== bUnlocked) return bUnlocked - aUnlocked;
            return tierOrder[achievements[a].tier] - tierOrder[achievements[b].tier];
        });

        sortedIds.forEach(id => {
            const achievement = achievements[id];
            const unlocked = unlockedAchievements[id];
            const unlockedDate = unlocked ? new Date(unlocked.unlockedAt).toLocaleDateString('zh-TW') : '';

            const card = document.createElement('div');
            card.className = `achievement-card ${unlocked ? 'unlocked' : 'locked'} ${achievement.tier}`;
            card.dataset.category = achievement.category;

            card.innerHTML = `
                <div class="achievement-icon">${unlocked ? achievement.icon : '🔒'}</div>
                <div class="achievement-info">
                    <div class="achievement-title">${achievement.titleZh}</div>
                    <div class="achievement-desc">${achievement.descZh}</div>
                    ${unlocked ? `<div class="achievement-date">${unlockedDate}</div>` : ''}
                </div>
                <div class="achievement-meta">
                    <span class="achievement-points ${unlocked ? '' : 'locked'}">${unlocked ? '+' : ''}${achievement.points}</span>
                </div>
            `;

            grid.appendChild(card);
        });

        // Update stats section
        const pagesCount = Object.keys(userData.progress.pagesVisited).filter(
            p => p !== 'index.html' && p !== ''
        ).length;
        const quizCount = Object.keys(userData.progress.quizzes).length;

        const statPages = document.querySelector('.stat-pages');
        const statQuizzes = document.querySelector('.stat-quizzes');
        const statAchievements = document.querySelector('.stat-achievements');

        if (statPages) statPages.textContent = pagesCount;
        if (statQuizzes) statQuizzes.textContent = quizCount;
        if (statAchievements) statAchievements.textContent = `${unlockedCount}/${totalCount}`;
    }

    // Auto-initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            AchievementTracker.init();
        });
    } else {
        AchievementTracker.init();
    }

    // Close modal with Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            const modal = document.getElementById('achievementsModal');
            if (modal && modal.classList.contains('active')) {
                closeAchievementsModal();
            }
        }
    });

    // Expose globally
    window.AchievementTracker = AchievementTracker;

})(window);
