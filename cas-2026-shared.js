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
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (e) {
      console.warn('CAS2026: could not save progress', e);
    }
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
      const entry = p[ch.id] || {};
      const c = entry.cards || {};
      done += Object.values(c).filter(Boolean).length;
      total += entry.totalCards || 0;
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
