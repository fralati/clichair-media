# Icone a linee per le copertine Stories. Ogni funzione riceve p (classe P di stories_cover.py):
# p.a = colore scuro della categoria, p.t = colore chiaro. Niente prodotti riconoscibili, niente persone.
import math

WHITE = "#ffffff"


def flacone(p):
    # flacone generico con goccia
    p.R([1040, 330, 1300, 800], rad=40, fill=WHITE, outline=p.a, w=8)
    p.R([1110, 250, 1230, 330], rad=12, fill=p.a)
    p.R([1135, 200, 1205, 250], rad=8, outline=p.a, w=7)
    p.L([(1080, 470), (1260, 470)], w=6)
    p.L([(1080, 520), (1220, 520)], w=6)
    p.L([(1080, 570), (1240, 570)], w=6)
    p.poly([(1380, 300), (1350, 360), (1410, 360)], fill=p.a)
    p.C(1380, 375, 31, fill=p.a)


def goccia(p):
    # siero / olio: grande goccia con riflesso e piccole gocce
    pts = []
    for i in range(0, 361, 6):
        t = math.radians(i)
        x = 1180 + 170 * math.sin(t)
        y = 560 - 170 * math.cos(t)
        if y < 560 - 80:
            pass
        pts.append((x, y))
    p.C(1180, 590, 170, fill=WHITE, outline=p.a, w=8)
    p.poly([(1180, 250), (1036, 500), (1324, 500)], fill=WHITE)
    p.L([(1180, 250), (1040, 495)], w=8)
    p.L([(1180, 250), (1320, 495)], w=8)
    p.A([1080, 480, 1180, 680], 180, 250, w=10)
    p.C(1400, 330, 26, fill=p.a)
    p.C(1440, 410, 16, fill=p.a)


def cute(p):
    # cute vista in sezione: linea della pelle, follicoli e fusti
    p.R([960, 560, 1400, 760], rad=30, fill=WHITE, outline=p.a, w=8)
    for x in [1020, 1110, 1200, 1290, 1370]:
        p.C(x, 650, 18, outline=p.a, w=6)
        p.L([(x, 632), (x + 20, 400), (x + 60, 300)], w=7)
    p.L([(960, 600), (1400, 600)], w=5, c=p.a)


def ricciolo(p):
    # ricci: tre ciocche a molla affiancate
    for k, x0 in enumerate([1020, 1180, 1340]):
        top = 230 + (k % 2) * 40
        pts = []
        for i in range(0, 1081, 5):
            t = math.radians(i)
            pts.append((x0 + 55 * math.cos(t), top + i * 0.45 + 22 * math.sin(t)))
        p.L(pts, w=8)

def ciocche(p):
    # ventaglio di ciocche colore in toni della categoria
    tones = [p.a, "#8a6b70", "#b8a0a4", "#d9c7ca", WHITE]
    for i, tone in enumerate(tones):
        x = 950 + i * 95
        p.R([x, 260, x + 70, 720], rad=35, fill=tone, outline=p.a, w=6)
    p.R([930, 700, 1430, 780], rad=20, fill=p.a)


def forbici(p):
    # strumenti del salone: forbici e pettine
    p.C(1030, 640, 60, outline=p.a, w=9)
    p.C(1030, 780, 60, outline=p.a, w=9)
    p.L([(1080, 610), (1400, 260)], w=10)
    p.L([(1080, 810), (1400, 260)], w=10)
    p.C(1240, 500, 12, fill=p.a)
    p.R([1260, 600, 1450, 660], rad=12, outline=p.a, w=7)
    for x in range(1275, 1445, 22):
        p.L([(x, 660), (x, 720)], w=6)


def tabella(p):
    # numeri del salone: foglio con tabella e grafico
    p.R([960, 220, 1400, 800], rad=26, fill=WHITE, outline=p.a, w=8)
    p.R([960, 220, 1400, 300], rad=26, fill=p.a)
    p.R([960, 270, 1400, 300], fill=p.a)
    for y in [380, 460, 540]:
        p.L([(1000, y), (1360, y)], w=4, c="#9aa9a0")
    for i, hgt in enumerate([60, 110, 90, 160]):
        x = 1020 + i * 85
        p.R([x, 740 - hgt, x + 50, 740], rad=8, fill=p.a)


def sole(p):
    # sole e onde: estate, piscina, mare
    p.C(1180, 400, 110, fill=WHITE, outline=p.a, w=8)
    for k in range(12):
        t = math.radians(k * 30)
        p.L([(1180 + 150 * math.cos(t), 400 + 150 * math.sin(t)), (1180 + 200 * math.cos(t), 400 + 200 * math.sin(t))], w=8)
    for y in [680, 750]:
        pts = [(x, y + 18 * math.sin((x - 960) / 45)) for x in range(960, 1401, 10)]
        p.L(pts, w=8)


def fiocco(p):
    # inverno: fiocco di neve
    cx, cy = 1180, 500
    for k in range(6):
        t = math.radians(k * 60)
        ex, ey = cx + 260 * math.cos(t), cy + 260 * math.sin(t)
        p.L([(cx, cy), (ex, ey)], w=9)
        for f in [0.55, 0.8]:
            bx, by = cx + 260 * f * math.cos(t), cy + 260 * f * math.sin(t)
            for s in (-1, 1):
                a2 = t + s * math.radians(40)
                p.L([(bx, by), (bx + 60 * math.cos(a2), by + 60 * math.sin(a2))], w=7)
    p.C(cx, cy, 30, fill=p.a)


def rasoio(p):
    # uomo: pettine da barbiere e forbici chiuse
    p.R([960, 260, 1060, 780], rad=18, fill=WHITE, outline=p.a, w=8)
    for y in range(290, 760, 34):
        p.L([(1060, y), (1130, y)], w=7)
    p.C(1290, 300, 52, outline=p.a, w=9)
    p.C(1400, 300, 52, outline=p.a, w=9)
    p.L([(1310, 350), (1350, 790)], w=10)
    p.L([(1380, 350), (1350, 790)], w=10)
    p.C(1345, 470, 11, fill=p.a)

def calendario(p):
    # riordino, abbonamento, tempo tra un appuntamento e l'altro
    p.R([960, 260, 1400, 760], rad=28, fill=WHITE, outline=p.a, w=8)
    p.R([960, 260, 1400, 350], rad=28, fill=p.a)
    p.R([960, 320, 1400, 350], fill=p.a)
    for x in [1060, 1300]:
        p.R([x - 10, 220, x + 10, 290], rad=8, fill=p.a)
    for r in range(3):
        for c in range(5):
            cx, cy = 1020 + c * 80, 420 + r * 100
            if (r, c) == (1, 3):
                p.C(cx, cy, 30, fill=p.a)
            else:
                p.C(cx, cy, 10, fill=p.a)


ICONS = {f.__name__: f for f in [flacone, goccia, cute, ricciolo, ciocche, forbici, tabella, sole, fiocco, rasoio, calendario]}
