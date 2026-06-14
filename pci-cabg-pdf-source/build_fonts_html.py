# 依本網站實際用到的字元，將 Noto 字型子集化（大幅縮小檔案、保持離線可用）。
# 來源為完整字符集字型（心衰竭手冊專案 fonts/），輸出到本資料夾 fonts/（子集）。
# 若日後修改 HTML/JS/CSS 文字、出現缺字，重新執行： python build_fonts.py
import glob, re, subprocess, sys, os

# 完整字型來源（含 2 萬餘字符）
SRC_DIR = r"C:/Users/drake/Downloads/心衰竭衛教手冊-Tufte/fonts"
DST_DIR = "fonts"   # 子集輸出（網站使用）

chars = set()
for pat in ("*.html", "*.js", "*.css"):
    for f in glob.glob(pat):
        t = open(f, encoding="utf-8").read()
        t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S)
        t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S)
        t = re.sub(r'<[^>]+>', ' ', t)
        t = re.sub(r'&[a-zA-Z]+;|&#\d+;', ' ', t)
        chars |= set(t)

extra = ("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
         ".,:;!?()[]{}/+-*=%·—–…　、。，！？；：「」『』（）【】《》〈〉～／＋－×≤≥→←↑↓"
         "①②③④⑤⑥❤⊕≡✔★◆◇■□●○※🖨📄  \n\t")
chars |= set(extra)
text = "".join(sorted(c for c in chars if c.strip() or c in "  "))
open("_subset_chars.txt", "w", encoding="utf-8").write(text)
print("unique chars:", len(chars))

fonts = ["NotoSerifTC-Regular.ttf", "NotoSerifTC-Bold.ttf",
         "NotoSansTC-Regular.ttf", "NotoSansTC-Medium.ttf", "NotoSansTC-Bold.ttf"]
os.makedirs(DST_DIR, exist_ok=True)
for fn in fonts:
    src = os.path.join(SRC_DIR, fn)
    out = os.path.join(DST_DIR, fn)
    cmd = [sys.executable, "-m", "fontTools.subset", src,
           "--text-file=_subset_chars.txt", "--output-file=" + out,
           "--layout-features=*", "--glyph-names", "--no-hinting",
           "--desubroutinize", "--name-IDs=*", "--recalc-bounds"]
    subprocess.run(cmd, check=True)
    print("subset", fn, round(os.path.getsize(out) / 1024, 1), "KB")
os.remove("_subset_chars.txt")
print("DONE")
