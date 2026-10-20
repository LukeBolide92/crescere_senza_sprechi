#!/usr/bin/env python3
# Configurazione Pelican - Crescere Senza Sprechi

AUTHOR = 'Crescere Senza Sprechi'
SITENAME = 'Crescere Senza Sprechi'
SITEURL = 'https://crescere-senza-sprechi.it'
PATH = 'content'
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'it'

THEME = 'theme'

# URL slug
ARTICLE_URL = 'guide/{slug}.html'
ARTICLE_SAVE_AS = 'guide/{slug}.html'
ARTICLE_LANG_URL = 'guide/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'guide/{slug}-{lang}.html'
CATEGORY_URL = 'area/{slug}.html'
CATEGORY_SAVE_AS = 'area/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'guide/'
ARCHIVES_SAVE_AS = 'guide/index.html'

# Plugin markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.meta': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Indice articoli con paginazione
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
}
PAGINATION_PATTERNS = [
    (1, '{name}{extension}', '{name}{extension}'),
    (2, '{name}{number}{extension}', '{name}{number}{extension}'),
]
DEFAULT_PAGINATION = 12

# Varie
RELATIVE_URLS = False
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
DEFAULT_METADATA = {
    'lang': 'it',
    'author': AUTHOR,
    'description': 'Crescere insieme, spendere meglio. Guide indipendenti per genitori, dal test positivo al 12° mese.',
}
SUMMARY_MAX_LENGTH = 45
