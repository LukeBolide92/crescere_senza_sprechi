# Crescere Senza Sprechi

Portale editoriale italiano per genitori, dal test positivo al primo compleanno.
Progetto realizzato con **Pelican** (generatore di siti statici), **Python 3**, **Markdown**, **Jinja2**, **HTML5/CSS**, **JavaScript vanilla**.

Payoff: *Crescere insieme, spendere meglio.*

---

## Requisiti

- Python 3.10+
- Virtualenv consigliato

---

## Installazione

```bash
# 1. Crea e attiva il virtualenv
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# 2. Installa le dipendenze
pip install -r requirements.txt
```

Il file `requirements.txt` contiene già:
`pelican`, `markdown`, `jinja2`, `pyyaml`, `beautifulsoup4`, `lxml`.

---

## Comandi principali

| Azione | Comando |
|--------|---------|
| **Build sviluppo** (URI locale, senza SITEURL) | `pelican content/` |
| **Build produzione** (URL canonico da `publishconf.py`) | `pelican content/ -s publishconf.py` |
| **Anteprima in browser su localhost** | `cd output && python -m http.server 8000` poi apri `http://localhost:8000` |
| **Validazione contenuti** | `python scripts/validate_content.py` |

### URI localhost
Per generare il sito con un URL locale (utile per testare link assoluti e Open Graph):

```bash
pelican content/ -S http://localhost:8000
```

Poi servili con:

```bash
cd output && python -m http.server 8000
```

Il sito sarà visibile a `http://localhost:8000`.

---

## Struttura del progetto

```
crescere_senza_sprechi/
├── .venv/                  # Virtualenv Python (non in git)
├── output/                 # Sito generato (non in git)
├── content/
│   ├── pages/              # Pagine statiche (chi siamo, contatti, privacy...)
│   ├── articles/           # Articoli e guide (Markdown)
│   ├── products/           # Schede prodotto (Markdown)
│   ├── courses/            # Corsi preparto e servizi (Markdown)
│   ├── checklists/         # Checklist (Markdown)
│   └── data/               # Dati strutturati YAML (prodotti, corsi, professionisti...)
├── theme/
│   ├── templates/          # Template Jinja2
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
├── scripts/                # Script di validazione e utilità
├── tests/                  # Test del progetto
├── docs/                   # Documentazione aggiuntiva
├── pelicanconf.py          # Configurazione sviluppo (SITEURL vuoto)
├── publishconf.py          # Configurazione produzione (SITEURL reale)
├── requirements.txt        # Dipendenze Python
├── .gitignore
└── README.md
```

---

## Aggiungere contenuti

1. Crea un file `.md` in `content/articles/` o `content/pages/`.
2. Intestazione YAML richiesta:

```markdown
Title: Titolo della guida
Slug: nome-slug-univoco
Date: 2024-01-15 09:00
Category: guide
Tags: gravidanza, risparmio
Summary: Breve descrizione per i meta tag e le card.
Author: Redazione Crescere Senza Sprechi
Status: draft|published
```

3. Scrivi il contenuto in Markdown.
4. Non usare prezzi, recensioni o URL inventati. Usa segnaposto editoriali espliciti se i dati non sono verificati.

---

## Validazione

Prima di pubblicare, esegui lo script di validazione:

```bash
python scripts/validate_content.py
```

Lo script controlla:
- Campi obbligatori mancanti
- Slug duplicati
- URL malformati
- Prezzi senza data di verifica
- Segnaposto editoriali critici
- Schede corsi non verificate

Distingue avvisi da errori che bloccano la pubblicazione.

## Come rigenerare il sito

Dopo aver modificato contenuti o template, ricostruisci con:

```bash
# 1. Attiva il virtualenv
source .venv/Scripts/activate  # Windows
# oppure source .venv/bin/activate  # macOS/Linux

# 2. Rimuovi il vecchio output e rigenera
rm -rf output/*
.venv/Scripts/python -m pelican content/

# 3. (Opzionale) Serve in locale
cd output && python -m http.server 8000
```

Nota: il build può mostrare un piccolo avviso Jinja su alcune pagine specifiche (correggibile con una modifica al template `article.html`). L'homepage (`output/index.html`), le guide (`output/guide/`), la pagina percorso (`output/percorso.html`) e il feed RSS (`output/rss.xml`) si generano correttamente.

---

## Deploy

Il sito è statico e può essere pubblicato su **GitHub Pages** o **Cloudflare Pages**.

1. Esegui il build di produzione:
   ```bash
   pelican content/ -s publishconf.py
   ```
2. Carica il contenuto di `output/` sull'hosting scelto.
3. Configura l'URL canonico nel `publishconf.py`.

Non richiede server sempre acceso, database né API.

---

## Note legali

Le pagine privacy e cookie sono predisposte ma **non dichiarano conformità automatica**. Prima della pubblicazione, completa le informazioni legali in base ai servizi effettivamente attivati (affiliazioni, analytics, cookie, newsletter).

---

## Licenza

Progetto editoriale indipendente. I contenuti sono proprietà di *Crescere Senza Sprechi*.
