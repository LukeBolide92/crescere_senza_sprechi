#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Configuration file for Pelican static site generator
# Crescere Senza Sprechi

import os
import yaml

# ---------------------------------------------------------------------------
# Percorsi
# ---------------------------------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(PROJECT_ROOT, "content")
DATA_DIR = os.path.join(CONTENT_DIR, "data")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

PATH = CONTENT_DIR
OUTPUT_PATH = OUTPUT_DIR
THEME = "theme"

# Cartelle statiche tema
STATIC_PATHS = ["theme/static"]

# ---------------------------------------------------------------------------
# Impostazioni di base
# ---------------------------------------------------------------------------
SITENAME = "Crescere Senza Sprechi"
SITESUBTITLE = "Crescere insieme, spendere meglio."
SITEDESCRIPTION = (
    "Ti aiutiamo a capire cosa serve davvero, cosa preparare e come fare "
    "scelte consapevoli, evitando spese inutili e perdite di tempo."
)
SITEURL = "http://localhost:8000"
CANONICAL_URL = "http://localhost:8000"
BASE_URL = "http://localhost:8000"

TIMEZONE = "Europe/Rome"
DEFAULT_LANG = "it"
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%A %d %B %Y"
LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False

# ---------------------------------------------------------------------------
# URL e permalink
# ---------------------------------------------------------------------------
ARTICLE_URL = "guide/{slug}/"
ARTICLE_SAVE_AS = "guide/{slug}.html"
ARTICLE_LANG_URL = "guide/{slug}/"
ARTICLE_LANG_SAVE_AS = "guide/{slug}.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}.html"
PAGE_LANG_URL = "{slug}/"
PAGE_LANG_SAVE_AS = "{slug}.html"

CATEGORY_URL = "categoria/{slug}/"
CATEGORY_SAVE_AS = "categoria/{slug}.html"

TAG_URL = "tema/{slug}/"
TAG_SAVE_AS = "tema/{slug}.html"

AUTHOR_URL = "autore/{slug}/"
AUTHOR_SAVE_AS = "autore/{slug}.html"

INDEX_SAVE_AS = "index.html"
INDEX_URL = ""
PAGINATION_URL = "pagina/{num}/"
PAGINATION_SAVE_AS = "pagina/{num}.html"

# Pagine da generare con i template diretti
DIRECT_TEMPLATES = ["index", "page", "404"]
TEMPLATE_PAGES = {
    # Mappatura template-name.html -> output-name.html in radice
    "404.html": "404.html",
    "index.html": "index.html",
}

# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.codehilite": {},
        "markdown.extensions.toc": {"permalink": True, "slugify": lambda x: x.lower().replace(" ", "-")},
        "markdown.extensions.smarty": {},
    },
    "output_format": "html5",
}

# ---------------------------------------------------------------------------
# Feed RSS
# ---------------------------------------------------------------------------
FEED_RSS = "rss.xml"
FEED_ALL_RSS = None
FEED_DOMAIN = "localhost"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

# ---------------------------------------------------------------------------
# Plugin / segnali per caricare i dati strutturati
# ---------------------------------------------------------------------------
PRODUCTS = []
COURSES = []
PROFESSIONALS = []
CATEGORIES = []
PHASES = []
AFFILIATES = {}


def _load_yaml(name):
    path = os.path.join(DATA_DIR, name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data if data is not None else []
    return []


def _load_custom_data():
    """Carica i file YAML dei dati strutturati in variabili globali."""
    global PRODUCTS, COURSES, PROFESSIONALS, CATEGORIES, PHASES, AFFILIATES
    PRODUCTS = _load_yaml("products.yaml")
    COURSES = _load_yaml("courses.yaml")
    PROFESSIONALS = _load_yaml("professionals.yaml")
    CATEGORIES = _load_yaml("categories.yaml")
    PHASES = _load_yaml("phases.yaml")
    AFFILIATES = _load_yaml("affiliates.yaml")


# Carica i dati all'importazione del file di configurazione
# _load_custom_data()  # TEMP: disabilitato per debug


# ---------------------------------------------------------------------------
# SEO base
# ---------------------------------------------------------------------------
SEO_ENABLED = True
SITEMAP_INCLUDE_FILELESS = True
SITEVAR_SECTIONS = ["articoli", "guide", "pagine", "prodotti", "corsi"]

# Paginazione
DEFAULT_PAGINATION = 6
PAGINATE = True
