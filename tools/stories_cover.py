# Generatore copertine cliCHair Stories (modello unico, dal 10.11.2026).
# Uso:
#   python3 tools/stories_cover.py --name "Nome" --city "Citta" --category saloni \
#       --icon flacone [--icon-file mia_icona.py] --out stories/AAMMGGhhmm_clichair-stories-nome.webp
# Categorie: saloni, colore, lunghezze, cute, ricci, uomo
# Icone pronte: vedi tools/icons.py (ICONS). Per un'icona nuova scrivere un file .py
# con una funzione draw(p) che usa i metodi di P (L linea, R rettangolo, C cerchio, A arco, poly).
# Coordinate nella tela 1600x1000; il riquadro dell'icona va da x 840-1520, y 80-920.
# Area sicura (ritaglio del tema circa 2.3:1): contenuto importante tra y 190 e 810.
import argparse, os, sys, importlib.util
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import icons  # noqa: E402

S = 2; W, H = 1600, 1000
LORA = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
INTER = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
INTERSB = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
LOGO = os.path.join(HERE, "..", "assets", "logo-clichair.png")

CATEGORIES = {
    "saloni":    ("#2f5d48", "#e3ece6"),
    "colore":    ("#7a2e3a", "#f1e4e6"),
    "lunghezze": ("#2a5e80", "#e1ebf1"),
    "cute":      ("#3f7a73", "#e2efed"),
    "ricci":     ("#a8543f", "#f4e7e2"),
    "uomo":      ("#3e4a5c", "#e6e8eb"),
}


class P:
    def __init__(s, d, a, t):
        s.d, s.a, s.t = d, a, t

    def L(s, pts, w=7, c=None):
        s.d.line([(x * S, y * S) for x, y in pts], fill=c or s.a, width=w * S, joint="curve")

    def R(s, b, rad=0, fill=None, outline=None, w=7):
        s.d.rounded_rectangle([v * S for v in b], radius=rad * S, fill=fill, outline=outline, width=w * S)

    def C(s, cx, cy, r, fill=None, outline=None, w=7):
        s.d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], fill=fill, outline=outline, width=w * S)

    def A(s, b, st, en, w=7, c=None):
        s.d.arc([v * S for v in b], st, en, fill=c or s.a, width=w * S)

    def poly(s, pts, fill=None, outline=None, w=7):
        s.d.polygon([(x * S, y * S) for x, y in pts], fill=fill, outline=outline, width=w * S if outline else 0)


def load_icon(name, icon_file):
    if icon_file:
        spec = importlib.util.spec_from_file_location("custom_icon", icon_file)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        return m.draw
    if name not in icons.ICONS:
        sys.exit("Icona sconosciuta: %s. Disponibili: %s" % (name, ", ".join(sorted(icons.ICONS))))
    return icons.ICONS[name]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--city", required=True)
    ap.add_argument("--category", required=True, choices=sorted(CATEGORIES))
    ap.add_argument("--icon", default="flacone")
    ap.add_argument("--icon-file")
    ap.add_argument("--out", required=True)
    ap.add_argument("--logo", default=LOGO)
    a = ap.parse_args()

    dark, light = CATEGORIES[a.category]
    lg = Image.open(a.logo).convert("RGBA")
    alpha = lg.getchannel("A")
    lg = lg.crop(alpha.point(lambda v: 255 if v > 20 else 0).getbbox())
    h = 52 * S
    logo = lg.resize((int(lg.width * h / lg.height), h), Image.LANCZOS)

    img = Image.new("RGB", (W * S, H * S), "#f5f4f2"); d = ImageDraw.Draw(img)
    d.rounded_rectangle([840 * S, 80 * S, 1520 * S, 920 * S], radius=48 * S, fill=light)
    layer = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    load_icon(a.icon, a.icon_file)(P(ImageDraw.Draw(layer), dark, light))
    SC = 0.78; CX, CY = 1180, 500
    small = layer.resize((int(W * S * SC), int(H * S * SC)), Image.LANCZOS)
    img.paste(small, (int(CX * S - CX * S * SC), int(CY * S - CY * S * SC)), small)

    d.text((110 * S, 250 * S), "S T O R I E S", font=ImageFont.truetype(INTERSB, 26 * S), fill=dark)
    d.line([(110 * S, 300 * S), (200 * S, 300 * S)], fill=dark, width=4 * S)
    size = 132
    while size > 80:
        f = ImageFont.truetype(LORA, size * S)
        if d.textlength(a.name, font=f) <= 700 * S:
            break
        size -= 4
    d.text((104 * S, 330 * S), a.name, font=f, fill="#1f1f1f")
    d.text((112 * S, 530 * S), a.city, font=ImageFont.truetype(INTER, 38 * S), fill="#6b6660")
    img.paste(logo, (110 * S, 760 * S - logo.height), logo)

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    img.resize((W, H), Image.LANCZOS).save(a.out, "WEBP", quality=90)
    print("ok", a.out)


if __name__ == "__main__":
    main()
