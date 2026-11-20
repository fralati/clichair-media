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


def ciotola(p):
    # miscelare colore e ossidante: ciotola con crema, pennello e misurino
    cx, cy, rx, ry = 320, 320, 190, 140
    body = [(cx + rx * math.cos(math.radians(a)), cy + ry * math.sin(math.radians(a))) for a in range(0, 181, 4)]
    p.poly(body, fill=WHITE, outline=p.a, w=8)
    p.R([cx - rx, cy - 32, cx + rx, cy + 32], rad=32, fill=p.t, outline=p.a, w=8)
    p.R([cx - 65, cy + ry - 6, cx + 65, cy + ry + 20], rad=10, fill=p.a)
    p.poly([(360, 320), (408, 320), (424, 268), (376, 268)], fill=p.a)
    p.L([(400, 271), (520, 110)], w=14)
    # misurino graduato a destra
    p.R([540, 230, 620, 440], rad=14, fill=WHITE, outline=p.a, w=7)
    p.R([544, 340, 616, 436], rad=10, fill=p.t)
    for y in [270, 310, 350, 390]:
        p.L([(540, y), (570, y)], w=5)


def spray(p):
    # nebulizzare senza risciacquo: flacone spray generico e nuvola di goccioline su una ciocca
    p.R([110, 230, 250, 490], rad=26, fill=WHITE, outline=p.a, w=7)
    p.R([140, 175, 220, 230], rad=8, fill=p.a)
    p.R([150, 130, 250, 175], rad=10, fill=p.a)
    p.R([230, 140, 290, 160], rad=6, fill=p.a)
    for y in [320, 360]:
        p.L([(140, y), (220, y)], w=5)
    # nuvola di goccioline a ventaglio
    for k, (dx, dy) in enumerate([(330, 120), (370, 150), (350, 180), (400, 125), (410, 175), (440, 150), (380, 205)]):
        p.C(dx, dy, 9 if k % 2 else 12, fill=p.a)
    # ciocca lunga a destra
    p.R([480, 100, 580, 500], rad=50, fill=WHITE, outline=p.a, w=7)
    for x in [505, 530, 555]:
        p.L([(x, 125), (x + 4, 475)], w=3)
    # freccia: dall'alto verso le punte
    p.L([(620, 180), (620, 440)], w=7)
    p.poly([(600, 430), (640, 430), (620, 465)], fill=p.a)


def _pennello(p, cx, cy, deg, L=230):
    ang = math.radians(deg)
    def rot(dx, dy):
        return (cx + dx * math.cos(ang) - dy * math.sin(ang), cy + dx * math.sin(ang) + dy * math.cos(ang))
    p.poly([rot(-8, -34), rot(46, -34), rot(46, 34), rot(-8, 34)], fill=p.t, outline=p.a, w=6)
    for d in (-18, 0, 18):
        p.L([rot(-6, d), rot(30, d)], w=3)
    p.poly([rot(46, -28), rot(84, -22), rot(84, 22), rot(46, 28)], fill=p.a)
    p.L([rot(84, 0), rot(L, 0)], w=12)
    p.C(*rot(L, 0), 9, fill=p.a)


def balayage(p):
    # balayage a mano libera: paletta con ciocche, punte schiarite, pennello piatto
    p.R([150, 110, 450, 480], rad=46, fill=WHITE, outline=p.a, w=7)
    for k, x in enumerate([185, 250, 315, 380]):
        top = 135 + (k % 2) * 20
        p.R([x, top, x + 50, 455], rad=25, fill=p.t, outline=p.a, w=5)
        mid = 285 + (k % 2) * 25
        p.R([x + 3, top + 3, x + 47, mid], rad=22, fill=p.a)
        for j in range(2):
            y0 = mid + j * 22
            p.L([(x + 10 + j * 5, y0), (x + 25, y0 + 18), (x + 40 - j * 5, y0)], w=3)
    _pennello(p, 440, 380, -58)


def tono(p):
    # tonalizzare a occhio: ciocca chiara con punte calde, pennello che parte dalla zona piu' gialla, occhio
    p.R([200, 100, 300, 500], rad=50, fill=WHITE, outline=p.a, w=7)
    for row, y in enumerate(range(330, 485, 24)):
        for x in range(218 + (row % 2) * 12, 290, 24):
            p.C(x, y, 6, fill=p.a)
    for x in [225, 250, 275]:
        p.L([(x, 120), (x, 310)], w=3)
    _pennello(p, 310, 380, -40, L=200)
    # occhio: controllo visivo
    cx, cy = 520, 200
    up = [(cx + 90 * math.cos(math.radians(a)), cy - 45 * math.sin(math.radians(a))) for a in range(0, 181, 6)]
    dn = [(cx - 90 * math.cos(math.radians(a)), cy + 45 * math.sin(math.radians(a))) for a in range(0, 181, 6)]
    p.poly(up + dn, fill=WHITE, outline=p.a, w=7)
    p.C(cx, cy, 26, fill=p.a)
    p.C(cx + 8, cy - 8, 7, fill=WHITE)


STEPS = {f.__name__: f for f in [bagnare, massaggio, posa, risciacquo, asciugamano, sezioni, pettine, lunghezze, calendario, ciotola, spray, balayage, tono]}
