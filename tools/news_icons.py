# Icone delle copertine cliCHair News (dal 10.11.2026).
# Ogni icona e' una funzione draw(p) con i metodi di P (L linea, R rettangolo, C cerchio, poly, d = ImageDraw).
# Coordinate nella tela 1600x1000, icona centrata attorno a x 1050, area sicura y 220-780.
# Nessun prodotto riconoscibile, nessuna persona, nessun testo.
import math

WHITE = "#ffffff"
GREY = "#9a958d"


def quick(p):  # foglio d'ordine con righe + fulmine
    p.R([760, 230, 1160, 770], rad=24, fill=WHITE, outline=p.a)
    for i, y in enumerate(range(320, 720, 80)):
        p.R([800, y - 18, 836, y + 18], rad=6, fill=p.a if i % 2 == 0 else p.t)
        p.L([(860, y), (1060, y)], w=6, c=GREY); p.L([(1090, y), (1120, y)], w=6)
    p.poly([(1240, 260), (1150, 480), (1225, 480), (1170, 700), (1330, 430), (1250, 430), (1320, 260)], p.a)


def calc(p):  # calcolatrice + tubetto
    p.R([780, 230, 1120, 770], rad=30, fill=WHITE, outline=p.a)
    p.R([820, 270, 1080, 380], rad=12, fill=p.t)
    for r in range(4):
        for c in range(3):
            x = 830 + c * 85; y = 420 + r * 85
            p.R([x, y, x + 60, y + 60], rad=12, fill=p.a if (r == 3 and c == 2) else p.t)
    p.R([1200, 300, 1300, 640], rad=22, fill=WHITE, outline=p.a); p.R([1225, 250, 1275, 302], rad=8, fill=p.a)
    p.poly([(1200, 630), (1300, 630), (1292, 680), (1208, 680)], p.a)


def klarna(p):  # carta + 3 rate
    p.R([760, 280, 1160, 540], rad=26, fill=WHITE, outline=p.a); p.R([760, 340, 1160, 390], fill=p.a)
    p.R([800, 450, 900, 480], rad=6, fill=p.t)
    for i in range(3):
        x = 860 + i * 140; p.C(x, 680, 48, fill=p.a if i == 0 else WHITE, outline=p.a, w=7)
    p.L([(908, 680), (952, 680)], w=6); p.L([(1048, 680), (1092, 680)], w=6)
    p.C(1290, 330, 70, fill=WHITE, outline=p.a, w=7); p.L([(1290, 330), (1290, 285)], w=7); p.L([(1290, 330), (1325, 350)], w=7)


def planb(p):  # bivio
    p.L([(1040, 780), (1040, 560)], w=12)
    p.L([(1040, 560), (860, 330)], w=12); p.L([(1040, 560), (1220, 330)], w=12, c="#c8b58c")
    p.L([(860, 330), (860, 400)], w=12); p.L([(860, 330), (930, 330)], w=12)
    p.L([(1220, 330), (1150, 330)], w=12, c="#c8b58c"); p.L([(1220, 330), (1220, 400)], w=12, c="#c8b58c")
    p.C(1040, 560, 26, fill=p.a)


def collective(p):  # due negozi collegati
    for x0 in (760, 1180):
        p.R([x0, 380, x0 + 220, 620], rad=18, fill=WHITE, outline=p.a)
        p.poly([(x0 - 20, 380), (x0 + 240, 380), (x0 + 210, 300), (x0 + 10, 300)], p.a)
        p.R([x0 + 80, 520, x0 + 140, 620], rad=6, fill=p.t)
    p.L([(990, 500), (1170, 500)], w=10); p.L([(1140, 470), (1170, 500), (1140, 530)], w=10); p.L([(1020, 470), (990, 500), (1020, 530)], w=10)


def niche(p):  # bilancia
    p.L([(1060, 260), (1060, 760)], w=10); p.R([960, 750, 1160, 780], rad=8, fill=p.a)
    p.L([(800, 340), (1320, 300)], w=10)
    p.L([(800, 340), (760, 500)], w=5); p.L([(800, 340), (840, 500)], w=5); p.d.chord([740 * 2, 450 * 2, 860 * 2, 550 * 2], 0, 180, fill=p.a)
    p.L([(1320, 300), (1280, 460)], w=5); p.L([(1320, 300), (1360, 460)], w=5); p.d.chord([1260 * 2, 410 * 2, 1380 * 2, 510 * 2], 0, 180, fill=p.a)
    p.poly([(800, 410), (822, 440), (800, 470), (778, 440)], "#d9c08a")
    p.R([1280, 370, 1360, 452], rad=6, fill="#c8b58c")


def pureverve(p):  # molecola
    def hexa(cx, cy, r, fill):
        pts = [(cx + r * math.cos(math.radians(60 * k + 30)), cy + r * math.sin(math.radians(60 * k + 30))) for k in range(6)]
        p.poly(pts, fill); p.L(pts + [pts[0]], w=8)
    hexa(960, 420, 110, WHITE); hexa(1150, 530, 110, "#d9c6df"); hexa(960, 640, 110, WHITE)
    for (x, y) in [(1300, 330), (1330, 700)]: p.C(x, y, 30, fill=p.a)
    p.L([(1245, 470), (1290, 350)], w=7); p.L([(1245, 590), (1315, 680)], w=7)


def creators(p):  # stella + rete
    pts = [(1050 + (150 if k % 2 == 0 else 65) * math.cos(math.radians(-90 + 36 * k)),
            470 + (150 if k % 2 == 0 else 65) * math.sin(math.radians(-90 + 36 * k))) for k in range(10)]
    p.poly(pts, WHITE); p.L(pts + [pts[0]], w=8)
    for (x, y) in [(800, 700), (1050, 740), (1300, 700)]:
        p.C(x, y, 34, fill=p.a); p.L([(x, y - 34), (1050, 620)], w=5)


def login(p):  # chiave + lucchetto
    p.R([1060, 440, 1300, 700], rad=24, fill=WHITE, outline=p.a)
    p.d.arc([1110 * 2, 300 * 2, 1250 * 2, 520 * 2], 180, 360, fill=p.a, width=10 * 2)
    p.L([(1110, 410), (1110, 440)], w=10); p.L([(1250, 410), (1250, 440)], w=10)
    p.C(1180, 555, 26, fill=p.a); p.R([1170, 560, 1190, 630], rad=6, fill=p.a)
    p.C(860, 430, 70, fill=WHITE, outline=p.a, w=10); p.L([(900, 490), (990, 640)], w=12); p.L([(950, 575), (990, 550)], w=10); p.L([(975, 615), (1010, 595)], w=10)


def kits(p):  # scatola kit + monete
    p.R([760, 380, 1120, 720], rad=20, fill=WHITE, outline=p.a); p.R([760, 380, 1120, 460], rad=20, fill=p.a)
    p.R([900, 330, 980, 390], rad=10, fill=WHITE, outline=p.a)
    for i, y in enumerate([690, 640, 590, 540]):
        p.R([1180, y, 1340, y + 40], rad=20, fill="#cfc9bf" if i % 2 else WHITE, outline=p.a, w=7)


def retail(p):  # scaffale con flaconi + barre
    p.R([740, 620, 1180, 640], rad=6, fill=p.a)
    for x, h in [(780, 170), (880, 210), (980, 150), (1080, 190)]:
        p.R([x, 620 - h, x + 70, 620], rad=14, fill=WHITE, outline=p.a, w=7); p.R([x + 20, 620 - h - 30, x + 50, 620 - h + 2], rad=5, fill=p.a)
    for i, h in enumerate([90, 150, 220]):
        p.R([1230 + i * 55, 620 - h, 1265 + i * 55, 620], rad=6, fill=p.a if i == 2 else "#cfc9bf")
    p.L([(1220, 400), (1300, 350), (1380, 300)], w=7)


def chat_cart(p):  # fumetto della chat con spunta + carrello pronto (10.11.2026)
    # fumetto
    p.R([740, 240, 1150, 560], rad=40, fill=WHITE, outline=p.a)
    p.poly([(820, 552), (900, 552), (810, 640)], p.a)
    p.poly([(832, 548), (884, 548), (826, 606)], WHITE)
    # spunta nel cerchio
    p.C(850, 400, 58, fill=p.a)
    p.L([(822, 402), (845, 426), (882, 378)], w=11, c=WHITE)
    # righe di testo astratte
    p.L([(940, 360), (1100, 360)], w=12, c=GREY)
    p.L([(940, 420), (1060, 420)], w=12, c=GREY)
    p.L([(940, 480), (1090, 480)], w=12, c="#c9cde0")
    # carrello
    p.L([(1080, 570), (1150, 570), (1200, 725), (1390, 725)], w=11)
    p.poly([(1160, 600), (1420, 600), (1385, 695), (1192, 695)], WHITE)
    p.L([(1160, 600), (1420, 600), (1385, 695), (1192, 695), (1160, 600)], w=9)
    for x in (1240, 1300, 1355):
        p.R([x - 16, 620, x + 16, 678], rad=6, fill=p.a)
    p.C(1230, 755, 22, fill=p.a); p.C(1360, 755, 22, fill=p.a)
    # freccia di ripetizione sopra il carrello
    p.d.arc([1210 * 2, 410 * 2, 1370 * 2, 570 * 2], 200, 340, fill=p.a, width=10 * 2)
    p.poly([(1366, 440), (1395, 490), (1336, 492)], p.a)


ICONS = {
    "quick": quick, "calc": calc, "klarna": klarna, "planb": planb, "collective": collective,
    "niche": niche, "pureverve": pureverve, "creators": creators, "login": login, "kits": kits,
    "retail": retail, "chat_cart": chat_cart,
}
