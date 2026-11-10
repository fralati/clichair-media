# Illustrazione "passo per passo" per le Stories (dal 10.11.2026).
# Griglia di riquadri numerati, stesso stile a linee delle copertine, nessuna parola dentro
# (vale per le 4 lingue: le spiegazioni stanno nel testo e nell'alt).
# Uso:
#   python3 tools/steps_strip.py --category cute --steps bagnare,massaggio,posa,asciugamano \
#       --out stories/AAMMGGhhmm_clichair-stories-<nome>-routine.webp
# Passi pronti: vedi STEPS in tools/step_icons.py. Per un passo nuovo: --steps-file file.py con
# funzioni draw_<nome>(p) e un dizionario STEPS = {"nome": draw_nome}.
# Ogni riquadro e' 700x560; il disegno sta tra x 60-640 e y 90-500 del riquadro.
import argparse, os, sys, math, importlib.util
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import step_icons  # noqa: E402
from stories_cover import CATEGORIES, INTERSB  # noqa: E402

S = 2
PW, PH, GAP, M = 700, 560, 40, 40


class P:
    def __init__(s, d, a, t, ox, oy):
        s.d, s.a, s.t, s.ox, s.oy = d, a, t, ox, oy

    def _p(s, x, y):
        return ((s.ox + x) * S, (s.oy + y) * S)

    def L(s, pts, w=7, c=None):
        s.d.line([s._p(x, y) for x, y in pts], fill=c or s.a, width=w * S, joint="curve")

    def R(s, b, rad=0, fill=None, outline=None, w=7):
        x0, y0 = s._p(b[0], b[1]); x1, y1 = s._p(b[2], b[3])
        s.d.rounded_rectangle([x0, y0, x1, y1], radius=rad * S, fill=fill, outline=outline, width=w * S)

    def C(s, cx, cy, r, fill=None, outline=None, w=7):
        x, y = s._p(cx, cy)
        s.d.ellipse([x - r * S, y - r * S, x + r * S, y + r * S], fill=fill, outline=outline, width=w * S)

    def A(s, b, st, en, w=7, c=None):
        x0, y0 = s._p(b[0], b[1]); x1, y1 = s._p(b[2], b[3])
        s.d.arc([x0, y0, x1, y1], st, en, fill=c or s.a, width=w * S)

    def poly(s, pts, fill=None, outline=None, w=7):
        s.d.polygon([s._p(x, y) for x, y in pts], fill=fill, outline=outline, width=w * S if outline else 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", required=True, choices=sorted(CATEGORIES))
    ap.add_argument("--steps", required=True, help="nomi separati da virgola, 2-6")
    ap.add_argument("--steps-file")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    lib = dict(step_icons.STEPS)
    if a.steps_file:
        spec = importlib.util.spec_from_file_location("custom_steps", a.steps_file)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        lib.update(m.STEPS)
    names = [n.strip() for n in a.steps.split(",") if n.strip()]
    for n in names:
        if n not in lib:
            sys.exit("Passo sconosciuto: %s. Disponibili: %s" % (n, ", ".join(sorted(lib))))
    dark, light = CATEGORIES[a.category]
    cols = 2 if len(names) in (2, 4) else 3 if len(names) in (3, 5, 6) else 2
    rows = math.ceil(len(names) / cols)
    W = M * 2 + cols * PW + (cols - 1) * GAP
    H = M * 2 + rows * PH + (rows - 1) * GAP
    img = Image.new("RGB", (W * S, H * S), "#f5f4f2"); d = ImageDraw.Draw(img)
    font = ImageFont.truetype(INTERSB, 34 * S)
    for i, n in enumerate(names):
        ox = M + (i % cols) * (PW + GAP); oy = M + (i // cols) * (PH + GAP)
        d.rounded_rectangle([ox * S, oy * S, (ox + PW) * S, (oy + PH) * S], radius=36 * S, fill=light)
        lib[n](P(d, dark, light, ox, oy))
        cx, cy = ox + 58, oy + 58
        d.ellipse([(cx - 30) * S, (cy - 30) * S, (cx + 30) * S, (cy + 30) * S], fill=dark)
        num = str(i + 1)
        tw = d.textlength(num, font=font)
        d.text((cx * S - tw / 2, (cy - 21) * S), num, font=font, fill="#ffffff")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    img.resize((W, H), Image.LANCZOS).save(a.out, "WEBP", quality=88)
    print("ok", a.out, W, H)


if __name__ == "__main__":
    main()
