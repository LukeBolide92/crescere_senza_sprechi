# Crescere Senza Sprechi — Istruzioni per lo Sviluppatore / Assistente AI di Codice

Questo documento fornisce le specifiche di implementazione, le regole di business e le istruzioni prompt pronte per essere fornite al tuo assistente AI (es. Claude Code, Cursor, Copilot Workspace o terminale locale) per completare la codebase Pelican e distribuire il portale.

---

## 1. Obiettivo del Progetto
Realizzare un portale editoriale statico italiano indipendente (**Crescere Senza Sprechi**, payoff: *"Crescere insieme, spendere meglio"*) rivolto ai genitori dal test positivo al 12° mese.
Lo stack tecnologico deve essere: **Python 3**, **Pelican Static Site Generator**, **Tailwind CSS**, template **Jinja2**, e moduli interattivi in **Vanilla JavaScript** (zero dipendenze frontend pesanti).

---

## 2. Architettura File e Repository

Struttura di directory obbligatoria conforme a Pelican:
```text
crescere-senza-sprechi/
├── content/
│   ├── articles/              # Guide comparative in Markdown con frontmatter YAML
│   ├── phases/                # Pagine di approfondimento per le 6 aree temporali (0-12 mesi)
│   ├── courses/               # Schede della directory corsi territoriali
│   ├── checklists/            # Schede scaricabili e testi sintetici
│   ├── pages/                 # Pagine statiche: chi-siamo.md, metodo-editoriale.md, ecc.
│   └── data/
│       ├── timeline.json      # Tappe cronologiche e consigli d'acquisto
│       ├── products.json      # Catalogo prodotti con data_verifica_prezzo
│       └── courses.json       # Database geolocalizzato corsi e consultori
├── theme/
│   ├── templates/
│   │   ├── base.html          # Shell layout comune con header, banner etico e footer
│   │   ├── index.html         # Homepage editoriale e calcolatore "Il tuo percorso"
│   │   ├── article.html       # Template guida comparativa con tabella e box fonti
│   │   ├── directory.html     # Directory corsi con filtri vanilla JS
│   │   ├── phase.html         # Template pagina di fase evolutiva
│   │   └── page.html          # Pagine informative/legali
│   └── static/
│       ├── css/input.css      # Regole Tailwind con token design system
│       └── js/
│           ├── timeline.js    # Motore di calcolo settimane gravidanza e mesi neonato
│           └── directory.js   # Filtro client-side istantaneo per i corsi
├── scripts/
│   ├── validate_content.py    # Linter obbligatorio pre-build
│   └── generate_sitemap.py    # Generatore sitemap SEO e schema.org
├── pelicanconf.py             # Configurazione principale Pelican
├── publishconf.py             # Configurazione per hosting Cloudflare / GitHub Pages
├── requirements.txt           # pelican, markdown, beautifulsoup4, pyyaml
└── README.md                  # Istruzioni di installazione e build locale
```

---

## 3. Direttive Rigorose per l'AI di Sviluppo

Quando ordini all'AI di generare i file, fai rispettare queste 5 regole auree:

### Regola 1: Vincolo Deontologico sulle Fonti (Nessuna invenzione clinica)
- Tutti i contenuti inerenti la sicurezza (sonno sicuro, seggiolini auto, allattamento, alimentazione complementare) devono citare esplicitamente fonti ufficiali: **Ministero della Salute**, **Istituto Superiore di Sanità (ISS)**, o **Società Italiana di Pediatria (SIP)**.
- Il file `scripts/validate_content.py` deve restituire errore di compilazione (`sys.exit(1)`) se un file Markdown nelle categorie `sonno`, `seggiolini` o `alimentazione` è privo del campo `Fonti:`.

### Regola 2: Trasparenza sui Prezzi e Affiliazioni
- Non inventare mai sconti fittizi o fasce di prezzo non verificate.
- Ogni prezzo monetario deve riportare il metadato `prezzo_verificato_il: DD/MM/YYYY`.
- La disclosure etica (*"I link verso i prodotti possono generare una commissione che non influisce sul prezzo per il lettore..."*) deve essere iniettata in automatico nel template `article.html` e non hardcoded manualmente nei singoli articoli.

### Regola 3: Motore "Il tuo percorso" in Vanilla JavaScript
Nel file `theme/static/js/timeline.js`:
- Il calcolo deve avvenire **interamente nel browser** (nessun tracking o invio dati utente).
- Gestire:
  1. Input `Data Presunta Parto (DPA)`: calcolare le settimane correnti (40 - giorni_mancanti/7) e mostrare solo la fase pertinente.
  2. Input `Data di Nascita`: calcolare i mesi trascorsi (0-12 mesi).
  3. Evidenziare sempre: le 3 guide consigliate, la checklist PDF abbinata, e soprattutto il box **"Spese da rimandare assolutamente"** per evitare acquisti prematuri o inutili.

### Regola 4: Design Token e CSS
- Palette cromatica:
  - Primario / Brand: `#2D5A47` (Verde Foresta Salvia - fiducia, calma, natura)
  - Superficie / Background: `#FBF9F5` (Avorio caldo naturale, anti-affaticamento visivo)
  - Accento / Risparmio: `#D97736` (Terracotta / Ocra caldo per badge risparmio e attenzioni)
  - Testo: `#1E2922` su `#FFFFFF` per garantire contrasto WCAG AAA.
- Font: Serif editoriale accogliente per titoli (`Newsreader` o `Merriweather`), Sans-serif ad alta leggibilità per corpo testo e tabelle (`Plus Jakarta Sans` o `Inter`).

---

## 4. Prompt Master da copiare e incollare all'AI (Cursor / Claude / Copilot)

> *"Genera la struttura completa del repository Pelican 'crescere-senza-sprechi' secondo le specifiche fornite nel documento. Implementa il file `pelicanconf.py`, i template Jinja2 `base.html`, `index.html`, `article.html` e `directory.html`, lo script `scripts/validate_content.py`, e compila gli articoli Markdown di test per la guida passeggini e la directory di Gallarate/Varese con dati reali e fonti Ministero della Salute. Assicurati che lo script di validazione esegua il controllo sulle date di verifica prezzi e la presenza delle fonti istituzionali."*
