# clichair-media

Immagini pubbliche del blog cliCHair (copertine delle Stories) e strumenti per generarle.
Shopify prende le immagini da qui con `fileCreate` (originalSource = URL raw di GitHub).

- `assets/logo-clichair.png`: logo nero trasparente "cliCHair / BEYOND BEAUTY" (928x246 utili). Non modificare.
- `assets/logo-clichair-bianco.png`: stessa versione in bianco.
- `tools/stories_cover.py`: generatore della copertina Stories (1600x1000 WebP, modello unico).
- `tools/icons.py`: icone a linee pronte (flacone, goccia, cute, ricciolo, ciocche, forbici, tabella, sole, fiocco, rasoio, calendario).
- `stories/`: copertine generate, nome `AAMMGGhhmm_clichair-stories-<nome>.webp`.

Esempio:

    python3 tools/stories_cover.py --name "Nome" --city "Citta" --category saloni --icon tabella \
        --out stories/2611111820_clichair-stories-nome.webp

URL da passare a Shopify: `https://raw.githubusercontent.com/fralati/clichair-media/main/stories/<file>.webp`
