/* 心衰竭衛教手冊 — 站台互動：回到頁首按鈕 + 長章頁章內小目錄。純前端、離線可用。 */
(function () {
  // ---- 回到頁首浮動按鈕 ----
  var btn = document.createElement('button');
  btn.className = 'to-top';
  btn.type = 'button';
  btn.setAttribute('aria-label', '回到頁首');
  btn.textContent = '↑';
  btn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
  document.body.appendChild(btn);
  function onScroll() { btn.classList.toggle('show', window.scrollY > 480); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ---- 章內小目錄（≥3 個 h3 的章節才產生）----
  var art = document.querySelector('article.page');
  if (!art) return;
  var h3s = art.querySelectorAll('h3');
  if (h3s.length < 3) return;
  var h2 = art.querySelector('h2');
  if (!h2) return;

  var nav = document.createElement('nav');
  nav.className = 'chap-toc';
  var ul = document.createElement('ul');
  Array.prototype.forEach.call(h3s, function (h, i) {
    if (!h.id) h.id = 'sec-' + (i + 1);
    var li = document.createElement('li');
    var a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent;
    li.appendChild(a);
    ul.appendChild(li);
  });
  var title = document.createElement('span');
  title.className = 'ct-title';
  title.textContent = '本章導覽';
  nav.appendChild(title);
  nav.appendChild(ul);
  h2.parentNode.insertBefore(nav, h2.nextSibling);
})();
