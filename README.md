# clichair-media

Immagini pubbliche del blog cliCHair (copertine delle Stories) e strumenti per generarle.
Shopify prende le immagini da qui con `fileCreate` (originalSource = URL raw di GitHub).

- `assets/logo-clichair.png`: logo nero trasparente "cliCHair / BEYOND BEAUTY" (928x246 utili). Non modificare.
- `assets/logo-clichair-bianco.png`: stessa versione in bianco.
- `tools/stories_cover.py`: generatore della copertina Stories (1600x1000 WebP, modello unico).
- `tools/icons.py`: icone a linee pronte (flacone, goccia, cute, ricciolo, ciocche, forbici, tabella, sole, fiocco, rasoio, calendario, ciotola: ciotola con pennello e ciocche bianche coperte, per i servizi colore in salone).
- `tools/steps_strip.py` + `tools/step_icons.py`: illustrazione "passo per passo" (riquadri numerati, nessuna parola) da mettere dopo la routine nella storia.
- `tools/news_cover.py` + `tools/news_icons.py`: generatore della copertina News (1600x1000 WebP, temi tools/platform/strategy/product/community, "N E W S", logo, icona a destra, nessun testo da tradurre). Esempio: `python3 tools/news_cover.py --theme platform --icon chat_cart --out news/AAMMGGhhmm_clichair-news-<slug>.webp`. Icone pronte: quick, calc, klarna, planb, collective, niche, pureverve, creators, login, kits, retail, chat_cart, colour_fade (ciocca che sfuma + gocce).
- `news/`: copertine del blog News, nome `AAMMGGhhmm_clichair-news-<slug>.webp`.
- `stories/`: copertine e illustrazioni generate, nome `AAMMGGhhmm_clichair-stories-<nome>.webp`.

Esempio:

    python3 tools/stories_cover.py --name "Nome" --city "Citta" --category saloni --icon tabella \
        --out stories/2611111820_clichair-stories-nome.webp

URL da passare a Shopify: `https://raw.githubusercontent.com/fralati/clichair-media/main/stories/<file>.webp`
