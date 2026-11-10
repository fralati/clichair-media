# Generatore copertine cliCHair News (dal 10.11.2026, modello del documento di progetto claude/clichair-news-covers.py).
# Uso:
#   python3 tools/news_cover.py --theme platform --icon chat_cart --out news/AAMMGGhhmm_clichair-news-<slug>.webp
# Temi (scuro / chiaro): tools #1f1f1f/#e8e5df, platform #3b4a8a/#e5e8f4, strategy #8a6a2b/#f3ecdc,
# product #5e3a6e/#ece4ef, community #5f6b2e/#eceedd.
# Sfondo pieno nel colore chiaro, "N E W S" e logo a sinistra, icona a destra, nessun testo da tradurre.
# 1600x1000 WebP, area sicura y 220-780. Logo da assets/logo-clichair.png (mai dal base64).
# Icone: tools/news_icons.py (ICONS). Icona nuova: funzione draw(p) in news_icons.py, oppure --icon-file file.py con draw(p).
import argparse, os, sys, importlib.util
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import news_icons  # noqa: E402

S = 2; W, H = 1600, 1000
INTERSB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
LOGO = os.path.join(HERE, "..", "assets", "logo-clichair.png")
THEMES = {
    "tools": ("#1f1f1f", "#e8e5df"),
    "platform": ("#3b4a8a", "#e5e8f4"),
    "strategy": ("#8a6a2b", "#f3ecdc"),
    "product": ("#5e3a6e", "#ece4ef"),
    "community": ("#5f6b2e", "#eceedd"),
}


class P:
    def __init__(s, d, a, t):
        s.d, s.a, s.t = d, a, t

    def L(s, pts, w=8, c=None):
        s.d.line([(x * S, y * S) for x, y in pts], fill=c or s.a, width=w * S, joint="curve")

    def R(s, b, rad=0, fill=None, outline=None, w=8):
        s.d.rounded_rectangle([v * S for v in b], radius=rad * S, fill=fill, outline=outline, width=w * S)

    def C(s, cx, cy, r, fill=None, outline=None, w=8):
        s.d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], fill=fill, outline=outline, width=w * S)

    def poly(s, pts, fill):
        s.d.polygon([(x * S, y * S) for x, y in pts], fill=fill)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--theme", required=True, choices=sorted(THEMES))
    ap.add_argument("--icon", default=None)
    ap.add_argument("--icon-file", default=None)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.icon_file:
        spec = importlib.util.spec_from_file_location("icon_mod", a.icon_file)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); draw = mod.draw
    else:
        draw = news_icons.ICONS[a.icon]
    dark, light = THEMES[a.theme]
    lg = Image.open(LOGO).convert("RGBA")
    bb = lg.getbbox(); lg = lg.crop(bb) if bb else lg
    h = 52 * S; logo = lg.resize((int(lg.width * h / lg.height), h), Image.LANCZOS)
    img = Image.new("RGB", (W * S, H * S), light); d = ImageDraw.Draw(img); p = P(d, dark, light)
    d.text((110 * S, 230 * S), "N E W S", font=ImageFont.truetype(INTERSB, 30 * S), fill=dark)
    d.line([(110 * S, 285 * S), (210 * S, 285 * S)], fill=dark, width=5 * S)
    img.paste(logo, (110 * S, 760 * S - logo.height), logo)
    draw(p)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    img.resize((W, H), Image.LANCZOS).save(a.out, "WEBP", quality=90)
    print(a.out)


if __name__ == "__main__":
    main()
