# Disegni dei passi per tools/steps_strip.py. Coordinate dentro il riquadro 700x560
# (disegno tra x 60-640, y 90-500; in alto a sinistra c'e' il numero). Niente persone
# riconoscibili, niente prodotti riconoscibili, niente parole.
import math

WHITE = "#ffffff"


def _testa(p, cx=350, cy=300, r=130):
    # testa vista di spalle: spalle, collo, testa, capelli come calotta con ciocche
    p.A([cx - 230, cy + r + 20, cx + 230, cy + r + 260], 200, 340, w=8)
    p.R([cx - 40, cy + r - 30, cx + 40, cy + r + 50], fill=WHITE)
    p.L([(cx - 40, cy + r - 20), (cx - 40, cy + r + 45)], w=7)
    p.L([(cx + 40, cy + r - 20), (cx + 40, cy + r + 45)], w=7)
    p.C(cx, cy, r, fill=WHITE, outline=p.a, w=7)
    pts = [(cx + (r + 6) * math.cos(math.radians(a)), cy + (r + 6) * math.sin(math.radians(a))) for a in range(160, 381, 5)]
    p.poly(pts + [(cx + r * 0.95, cy + 30), (cx - r * 0.95, cy + 30)], fill=p.t, outline=p.a, w=7)
    for k in range(-3, 4):
        x = cx + k * 30
        p.L([(x, cy - r + 18 + abs(k) * 8), (x + k * 6, cy + 25)], w=4)

def bagnare(p):
    # capelli bagnati: testa e gocce d'acqua dall'alto
    _testa(p)
    for (x, y) in [(250, 120), (330, 100), (410, 115), (480, 140), (200, 150)]:
        p.poly([(x, y - 22), (x - 14, y + 4), (x + 14, y + 4)], fill=p.a)
        p.C(x, y + 8, 14, fill=p.a)


def massaggio(p):
    # massaggio della cute: testa e frecce circolari
    _testa(p)
    for (cx, cy) in [(200, 230), (500, 230)]:
        p.A([cx - 55, cy - 55, cx + 55, cy + 55], 200, 520, w=8)
        t = math.radians(160)
        x, y = cx + 55 * math.cos(t), cy + 55 * math.sin(t)
        p.poly([(x - 16, y - 18), (x + 18, y - 6), (x - 6, y + 20)], fill=p.a)


def posa(p):
    # tempo di posa: orologio con spicchio evidenziato
    cx, cy, r = 350, 310, 170
    p.C(cx, cy, r, fill=WHITE, outline=p.a, w=8)
    pts = [(cx, cy)] + [(cx + r * 0.88 * math.cos(math.radians(a)), cy + r * 0.88 * math.sin(math.radians(a))) for a in range(-90, -24, 3)]
    p.poly(pts, fill=p.t)
    for k in range(12):
        t = math.radians(k * 30)
        p.L([(cx + (r - 28) * math.cos(t), cy + (r - 28) * math.sin(t)), (cx + (r - 10) * math.cos(t), cy + (r - 10) * math.sin(t))], w=6)
    p.L([(cx, cy), (cx, cy - 120)], w=8)
    p.L([(cx, cy), (cx + 75, cy - 40)], w=8)
    p.C(cx, cy, 12, fill=p.a)
    p.R([cx - 30, cy - r - 46, cx + 30, cy - r - 14], rad=8, fill=p.a)


def risciacquo(p):
    # risciacquo: soffione della doccia e getto d'acqua
    p.R([180, 110, 420, 150], rad=20, fill=p.a)
    p.R([380, 90, 420, 150], rad=12, fill=p.a)
    p.L([(400, 90), (520, 90), (520, 140)], w=10)
    for x in range(200, 410, 30):
        p.L([(x, 175), (x - 30, 460)], w=5)
    for (x, y) in [(220, 490), (300, 500), (380, 490)]:
        p.C(x, y, 10, fill=p.a)


def asciugamano(p):
    # tamponare con l'asciugamano: asciugamano piegato con righe
    p.R([140, 200, 560, 440], rad=30, fill=WHITE, outline=p.a, w=8)
    p.R([140, 200, 560, 260], rad=30, fill=p.a)
    p.R([140, 230, 560, 260], fill=p.a)
    for y in [320, 370]:
        p.L([(180, y), (520, y)], w=5)
    for (x, y) in [(470, 140), (520, 170), (430, 160)]:
        p.C(x, y, 9, fill=p.a)


def sezioni(p):
    # applicazione sezione per sezione: cute divisa da righe e goccioline sulle righe
    _testa(p)
    for x in [300, 350, 400]:
        for y in [215, 255, 295]:
            p.C(x, y, 10, fill=p.a)
    p.R([500, 100, 550, 210], rad=14, fill=WHITE, outline=p.a, w=6)
    p.poly([(510, 210), (540, 210), (525, 252)], fill=p.a)


def pettine(p):
    # distribuire con il pettine
    p.R([150, 180, 550, 250], rad=20, fill=WHITE, outline=p.a, w=8)
    for x in range(170, 540, 26):
        p.L([(x, 250), (x, 340)], w=6)
    for k in range(4):
        y = 390 + k * 26
        p.L([(170, y), (530, y + 10)], w=4)


def lunghezze(p):
    # applicare su lunghezze e punte: ciocca lunga con le punte evidenziate a puntini
    p.R([300, 90, 400, 500], rad=50, fill=WHITE, outline=p.a, w=7)
    for x in [325, 350, 375]:
        p.L([(x, 110), (x, 300)], w=3)
    p.L([(300, 300), (400, 300)], w=6)
    for row, y in enumerate(range(325, 485, 26)):
        for x in range(318 + (row % 2) * 13, 390, 26):
            p.C(x, y, 7, fill=p.a)
    p.L([(470, 300), (470, 480)], w=8)
    p.poly([(448, 470), (492, 470), (470, 505)], fill=p.a)

def calendario(p):
    # frequenza: calendario con giorni segnati
    p.R([170, 140, 530, 480], rad=24, fill=WHITE, outline=p.a, w=8)
    p.R([170, 140, 530, 210], rad=24, fill=p.a)
    p.R([170, 185, 530, 210], fill=p.a)
    for r in range(3):
        for c in range(5):
            cx, cy = 220 + c * 65, 260 + r * 75
            if (r * 5 + c) % 2 == 0:
                p.C(cx, cy, 20, fill=p.a)
            else:
                p.C(cx, cy, 8, fill=p.a)


STEPS = {f.__name__: f for f in [bagnare, massaggio, posa, risciacquo, asciugamano, sezioni, pettine, lunghezze, calendario]}
