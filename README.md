# Crescere Senza Sprechi

Payoff: *Crescere insieme, spendere meglio*.

## Installazione
pip install -r requirements.txt

## Build locale
python scripts/validate_content.py
python -m pelican content -o output -t theme -s pelicanconf.py

## Struttura
- content/: articoli, fasi, pagine, dati JSON
- theme/templates/: template Jinja2 (index, article, phase, explore)
- theme/static/: css e js vanilla (timeline.js, directory.js)
- scripts/: validate_content.py, generate_sitemap.py

---
## Preview locale
```bash
python -m http.server 8000 --directory theme/templates
```
Apri `http://localhost:8000/advice.html?settimana=4` per testare il caricamento dai dati (`theme/templates/static/js/weeks-data.js`).
