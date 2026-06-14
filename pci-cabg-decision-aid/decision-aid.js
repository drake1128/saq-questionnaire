/* 醫病共享決策 — 步驟頁互動：可勾選、自動儲存（localStorage）、列印、清除。
   純前端、離線可用。本工具「不計分、不給建議」，只協助病人釐清與記錄自己的想法。 */
(function () {
  var root = document.querySelector('article.page') || document.body;
  var key = 'sdm-pci-cabg::' + location.pathname.split('/').pop();
  var inputs = Array.prototype.slice.call(
    root.querySelectorAll('input[type=radio], input[type=checkbox]')
  );
  if (!inputs.length) return;

  // 為沒有 name 的輸入建立穩定識別（依出現順序）
  inputs.forEach(function (el, i) { if (!el.dataset.k) el.dataset.k = el.name ? el.name + '#' + el.value : 'i' + i; });

  var saved = document.querySelector('.da-saved');
  function flash(msg) { if (saved) { saved.textContent = msg; } }

  function persist() {
    var state = {};
    inputs.forEach(function (el) { if (el.checked) state[el.dataset.k] = 1; });
    try { localStorage.setItem(key, JSON.stringify(state)); } catch (e) {}
    flash('已自動儲存於本機 ✓');
  }

  function restore() {
    var state;
    try { state = JSON.parse(localStorage.getItem(key) || '{}'); } catch (e) { state = {}; }
    var any = false;
    inputs.forEach(function (el) { if (state[el.dataset.k]) { el.checked = true; any = true; } });
    if (any) flash('已載入上次填寫內容 ✓');
  }

  root.addEventListener('change', function (e) {
    if (e.target && (e.target.type === 'radio' || e.target.type === 'checkbox')) persist();
  });

  document.addEventListener('click', function (e) {
    var t = e.target.closest ? e.target.closest('.js-print, .js-reset') : null;
    if (!t) return;
    if (t.classList.contains('js-print')) { window.print(); }
    if (t.classList.contains('js-reset')) {
      if (!confirm('確定要清除本頁所有勾選嗎？')) return;
      inputs.forEach(function (el) { el.checked = false; });
      try { localStorage.removeItem(key); } catch (e2) {}
      flash('已清除');
    }
  });

  restore();
})();
