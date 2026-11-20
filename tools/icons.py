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


def ciotola(p):
    # servizio colore: ciotola con crema e pennello, ciocche bianche coperte dal colore
    # ciocche: parte alta bianca, parte bassa colorata
    for k, x in enumerate([985, 1075]):
        top = 250 + k * 30
        p.R([x, top, x + 64, 520], rad=32, fill=WHITE, outline=p.a, w=6)
        p.R([x + 3, top + 120, x + 61, 517], rad=29, fill=p.a)
        p.L([(x + 32, top + 20), (x + 32, top + 100)], w=3)
    # ciotola: corpo a mezza ellisse
    cx, cy, rx, ry = 1210, 600, 200, 150
    body = [(cx + rx * math.cos(math.radians(a)), cy + ry * math.sin(math.radians(a))) for a in range(0, 181, 4)]
    p.poly(body, fill=WHITE, outline=p.a, w=8)
    # bordo e crema
    p.R([cx - rx, cy - 34, cx + rx, cy + 34], rad=34, fill=p.t, outline=p.a, w=8)
    # base
    p.R([cx - 70, cy + ry - 6, cx + 70, cy + ry + 22], rad=10, fill=p.a)
    # pennello: setole nella crema e manico inclinato
    p.poly([(1250, 600), (1300, 600), (1318, 545), (1268, 545)], fill=p.a)
    p.L([(1293, 548), (1430, 270)], w=16)
    p.C(1430, 270, 12, fill=p.a)


def berretto(p):
    # inverno: berretto di lana con pompon e treccia lunga che scende, fiocchi di neve
    cx = 1160
    # calotta del berretto (mezza ellisse)
    dome = [(cx + 210 * math.cos(math.radians(a)), 470 + 230 * math.sin(math.radians(a))) for a in range(180, 361, 4)]
    p.poly(dome, fill=WHITE, outline=p.a, w=8)
    # coste della maglia
    for k in range(-3, 4):
        x = cx + k * 52
        top = 470 - 230 * math.sqrt(max(0, 1 - (k * 52 / 210) ** 2)) + 18
        p.L([(x, top), (x, 450)], w=4)
    # risvolto a costine
    p.R([cx - 225, 440, cx + 225, 520], rad=22, fill=p.a)
    for x in range(cx - 195, cx + 200, 30):
        p.L([(x, 452), (x, 508)], w=4, c=p.t)
    # pompon
    p.C(cx, 232, 46, fill=p.t, outline=p.a, w=8)
    # treccia: maglie a foglia inclinate alternativamente, come una treccia vista di fronte
    x0, y = cx + 120, 548
    def leaf(xc, yc, ang):
        pts = []
        for a in range(0, 360, 8):
            t = math.radians(a)
            ex, ey = 26 * math.cos(t), 40 * math.sin(t)
            r = math.radians(ang)
            pts.append((xc + ex * math.cos(r) - ey * math.sin(r), yc + ex * math.sin(r) + ey * math.cos(r)))
        return pts
    for i in range(5):
        yc = y + i * 46
        p.poly(leaf(x0 - 16, yc, -35), fill=p.t, outline=p.a, w=6)
        p.poly(leaf(x0 + 16, yc + 23, 35), fill=p.t, outline=p.a, w=6)
    y = y + 5 * 46 + 10
    p.R([x0 - 26, y - 6, x0 + 26, y + 12], rad=8, fill=p.a)
    for dx in (-18, 0, 18):
        p.L([(x0 + dx * 0.6, y + 12), (x0 + dx, y + 60)], w=5)
    # fiocchi di neve
    for (fx, fy, r) in [(960, 300, 38), (1400, 330, 30), (990, 700, 28)]:
        for k in range(3):
            t = math.radians(k * 60)
            p.L([(fx - r * math.cos(t), fy - r * math.sin(t)), (fx + r * math.cos(t), fy + r * math.sin(t))], w=5)


def balayage(p):
    # balayage: paletta con ciocche scure schiarite verso le punte e pennello piatto che dipinge
    p.R([960, 250, 1330, 740], rad=60, fill=WHITE, outline=p.a, w=8)
    # manico della paletta, stretto e con foro
    p.R([1115, 735, 1175, 830], rad=24, fill=WHITE, outline=p.a, w=8)
    p.C(1145, 800, 10, outline=p.a, w=5)
    # ciocche: parte alta scura, punte schiarite con sfumatura a V
    for k, x in enumerate([1000, 1075, 1150, 1225]):
        top = 280 + (k % 2) * 25
        p.R([x, top, x + 62, 710], rad=31, fill=p.t, outline=p.a, w=6)
        mid = 470 + (k % 2) * 30
        p.R([x + 3, top + 3, x + 59, mid], rad=28, fill=p.a)
        for j in range(3):
            y0 = mid + j * 26
            p.L([(x + 12 + j * 6, y0), (x + 31, y0 + 22), (x + 50 - j * 6, y0)], w=4)
    # pennello piatto: testa con setole che appoggia sull'ultima ciocca, manico verso l'alto a destra
    ang = math.radians(-58)
    cx, cy = 1290, 600
    def rot(dx, dy):
        return (cx + dx * math.cos(ang) - dy * math.sin(ang), cy + dx * math.sin(ang) + dy * math.cos(ang))
    # setole (rettangolo ruotato) e ghiera
    p.poly([rot(-10, -45), rot(60, -45), rot(60, 45), rot(-10, 45)], fill=p.t, outline=p.a, w=7)
    for d in (-25, 0, 25):
        p.L([rot(-8, d), rot(40, d)], w=4)
    p.poly([rot(60, -38), rot(110, -30), rot(110, 30), rot(60, 38)], fill=p.a)
    p.L([rot(110, 0), rot(330, 0)], w=16)
    p.C(*rot(330, 0), 11, fill=p.a)
    # luce sulle punte
    for (sx, sy, r) in [(1420, 700, 24), (1420, 300, 20)]:
        if r:
            p.L([(sx - r, sy), (sx + r, sy)], w=5)
            p.L([(sx, sy - r), (sx, sy + r)], w=5)


ICONS = {f.__name__: f for f in [flacone, goccia, cute, ricciolo, ciocche, forbici, tabella, sole, fiocco, rasoio, calendario, ciotola, berretto, balayage]}
