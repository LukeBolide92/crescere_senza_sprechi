# PI — Istruzioni iniziali per Crescere Senza Sprechi

## Scopo
Prototipo locale statico per il portale genitoriale "Crescere Senza Sprechi". Solo 2 template attivi: `theme/templates/index.html` + `theme/templates/advice.html`.

## Stato attuale (ultima verifica)
- `advice.html` carica contenuto da `theme/templates/static/js/weeks-data.js` (`WEEKS` + `WEEKS_DEFAULT` + `babyInfo`).
- Menu drawer: settimane gravidanza (4-40) + mesi bambino (41-52); link a `advice.html?settimana=`.
- `index.html`: redirect "Vai ai consigli" a `advice.html?settimana=`.
- Non committare finché l'utente non lo richiede esplicitamente.
- Push origine bloccato (auth GitHub mancante).

## Struttura chiave
- `theme/templates/index.html`
- `theme/templates/advice.html`
- `theme/templates/static/js/weeks-data.js` (unica fonte dati; anche copia in `theme/static/` rimossa)
- `README.md` (comando preview + nota "non committare")
- `pelicanconf.py` / `publishconf.py`

## Preview locale (comando corretto)
```bash
python -m http.server 8000 --directory theme/templates
# prova: http://localhost:8000/advice.html?settimana=21  o  ?settimana=7
```

## Vincoli
- Non rompere il design mobile (`overflow-y-none`, `overscroll-behavior`, `pb-safe`).
- Non cancellare o modificare `_nav.html` / altri template parziali (già rimossi; solo 2 template restano).
- Non committare **nessun** file del progetto finché l'utente non richieda esplicitamente.
- Se l'utente chiede di spostare/copiare dati: mantenere coerenza tra `theme/static/` e `theme/templates/static/` (ma ora è un solo file in templates).

## Cosa fare se si rompe il caricamento dati
1. Verificare che `static/js/weeks-data.js` sia raggiungibile (200) dal server locale.
2. Verificare che nella console del browser non ci sia `SyntaxError` in `advice.html` (spesso manca `})();` o chiusura `<script>`).
3. Verificare che `advice.html` abbia gli ID (`advice-title`, `box1-title`, etc.) per il popolamento.
