# -*- coding: utf-8 -*-
"""Allinea weeks-data.js allo schema completo usato dal renderer."""
import re, io, json

P = 'theme/static/js/weeks-data.js'
s = io.open(P, encoding='utf-8').read()

# 1) normalizza chiavi duplicate "4: 4:" ecc.
s = re.sub(r'(\d+):\s+\d+:', r'\1:', s)

# 2) rimuove campi img/imgAlt duplicati se presenti piu volte per chiave
EXTRA = {
 4:  ("S1-S8", "Nessun codice previsto in questa fase: la prima visita e' in consultorio.",
      "Non serve ancora comprare attrezzatura: solo gravidanza, latte e abbigliamento base.",
      "Checklist delle spese reali", "Solo l'essenziale: gravidanza, latte, abbigliamento base."),
 8:  ("S8-S12", "Esecuzione prevista tra S8 e S12 secondo il piano regionale.",
      "Il trasporto e' la scelta che fara' piu' differenza: aspettare qualche settimana fa risparmiare.",
      "Il Test del Bagagliaio", "Prova il passeggino nel portabagagli: misura gli ingombri reali."),
 12: ("S12-S13", "Verifica il referto con il consultorio.",
      "Il passeggino non e' una scelta da fare d'impulso in negozio.",
      "Il Test del Bagagliaio Reale", "Prova il passeggino nel portabagagli: l'80% delle famiglie cambia dopo 5 mesi."),
 16: ("—", "Curva di peso valutata con il consultorio.",
      "Abbigliamento e cura personale: meglio comprare poco, la crescita cambia taglia.",
      "La taglia che dura", "Due o tre taglie comode e usabili, non un guardaroba della gravidanza."),
 21: ("M21", "Nessun ticket dovuto se prescritto tra 19+0 e 20+6.",
      "Il telaio del passeggino: meglio una prova pratica che un acquisto da 900 euro.",
      "Il Test del Bagagliaio Reale", "Prova il passeggino di un amico nel portabagagli: l'80% delle famiglie cambia dopo 5 mesi."),
 28: ("—", "Iscrizione presso il consultorio ASL del territorio.",
      "Il punto del parto: confronta le opzioni del tuo territorio prima di decidere.",
      "Carta dei servizi", "Consulta ASL e ospedali di riferimento: distanze, reparti, analgesia."),
 32: ("—", "Servono documento, tessera sanitaria e referti recenti.",
      "L'auto per il rientro: se hai gia' un'auto evita gli accessori dedicati.",
      "Posto auto e trasporto", "Verifica percorso verso la maternita' e parcheggio: e' la vera incognita."),
 36: ("—", "Piano regionale dei controlli nella gravidanza fisiologica.",
      "Culla e seggiolino auto: due acquisti che meritano la massima attenzione.",
      "Sicurezza in auto e in casa", "Consulta un servizio di consulenza pediatrica: la sicurezza costa meno di un rimorso."),
 40: ("—", "Entro 10 giorni dalla nascita: presa in carico del pediatra.",
      "Il pediatra di base: confronta gli studi del tuo territorio prima di scegliere.",
      "Come scegliere il pediatra", "Guarda distanza, disponibilita' e continuita'."),
}

def js(v):
    return json.dumps(v, ensure_ascii=False)

for w, (code, codeNote, b3text, b3box, b3inner) in EXTRA.items():
    pat = re.compile(r'(\n  %d:\s*\{)' % w)
    m = pat.search(s)
    if not m:
        continue
    # inserisce campi mancanti subito dopo la chiave
    add = " badge:'SSN', codeTitle:'Codice Esenzione Ricetta: %s', codeNote:'%s'" % (code, codeNote)
    s = s[:m.end()] + add + s[m.end():]

# 3) aggiunge b2.points, b3, checklist a ogni chiave settimana
def patch_week(s, w):
    # inserisce b3/checklist/b2.points prima della chiusura della entry
    pat = re.compile(r'(\n  %d:\s*\{.*?dl:"[^"]*")(\},?)' % w, re.S)
    m = pat.search(s)
    if not m:
        return s, False
    extra = ""
    if '"b3"' not in m.group(1):
        extra += ", b3:{title:'Cosa valutare con calma', text:'%s', boxTitle:'%s', boxText:'%s'}" % (
            EXTRA[w][2].replace("'", "\\'"), EXTRA[w][3].replace("'", "\\'"), EXTRA[w][4].replace("'", "\\'"))
    if '"checklist"' not in m.group(1):
        extra += ", checklist:{title:'I 3 Compiti Essenziali di Questa Settimana', items:TASKS_%d}" % w
    if '"points"' not in m.group(1):
        extra += ", points:POINTS_%d" % w
    if not extra:
        return s, False
    s = s[:m.end(1)] + extra + s[m.end(1):]
    return s, True

# raccoglie tasks per week dal file
def extract_tasks(s, w):
    pat = re.compile(r'\n  %d:\s*\{.*?tasks:\[(.*?)\], dl:' % w, re.S)
    m = pat.search(s)
    if not m:
        return None
    items = re.findall(r'\{t:"((?:[^"\\]|\\.)*)", d:"((?:[^"\\]|\\.)*)"\}', m.group(1))
    if not items:
        return None
    return "[" + ",".join('{t:"%s",d:"%s"}' % (t, d) for t, d in items) + "]"

TASKS = {}
for w in EXTRA:
    t = extract_tasks(s, w)
    if t:
        TASKS[w] = t

POINTS = {
 4:  '[{strong:"Nessuna spesa ora",text:"Tutto questo si puo\' comprare con calma dopo il 1o trimestre."},{strong:"Risparmio",text:"Nessun acquisto d\'impulso: e\' la regola d\'oro del 1o trimestre."}]',
 8:  '[{strong:"Prima di comprare",text:"Gli integratori non servono se l\'alimentazione e\' varia."},{strong:"Attenzione",text:"Alcuni esami privati sono opzionali: chiedi al consultorio."}]',
 12: '[{strong:"Nessuna fretta",text:"Il trio completo si sceglie dopo aver visto il bimbo."},{strong:"Risparmio",text:"150-400 euro rimandati di qualche mese."}]',
 16: '[{strong:"Prova prima",text:"Un cuscino del divano puo\' bastare."},{strong:"Risparmio",text:"40-70 euro non spesi in un accessorio usa-e-getta."}]',
 21: '[{strong:"Nessun uso prima dei 6 mesi",text:"Il bimbo non ha il tono posturale per stare seduto: tenerlo in salotto per 8 mesi ruba spazio vitale."},{strong:"Risparmio immediato",text:"Trattieni in tasca 150-250 euro per le spese indispensabili di fine trimestre."}]',
 28: '[{strong:"Solo l\'essenziale",text:"10 pezzi bastano per il soggiorno in ospedale."},{strong:"Il resto dopo",text:"Il resto si compra a casa, con calma."}]',
 32: '[{strong:"Dieci pezzi",text:"Solo l\'essenziale per i primi 10-14 giorni."},{strong:"Zero doppioni",text:"Tutto il resto puo\' aspettare la nascita."}]',
 36: '[{strong:"Dopo il parto",text:"Tutto il resto si compra dopo la nascita, con calma."},{strong:"Risparmio",text:"Centinaia di euro rimandate senza rinunce."}]',
 40: '[{strong:"Novanta euro",text:"Il kit notte essenziale per la prima settimana."},{strong:"Il resto dopo",text:"Aspetta di conoscere i ritmi del bimbo."}]',
}

for w in list(EXTRA):
    s = patch_week(s, w)

# 4) inserisce le costanti TASKS_x / POINTS_x prima di window.WEEKS
consts = "\n".join(
    "window.TASKS_%d = %s;" % (w, TASKS[w]) for w in sorted(TASKS)) + "\n" + \
"\n".join("window.POINTS_%d = %s;" % (w, POINTS[w]) for w in sorted(POINTS)) + "\n"
s = s.replace("window.WEEKS = {", consts + "window.WEEKS = {", 1)

# 5) dentro le entry, sostituisce i placeholder TASKS_x / POINTS_x con riferimenti
for w in EXTRA:
    s = s.replace("items:TASKS_%d" % w, "items:window.TASKS_%d" % w)
    s = s.replace("points:POINTS_%d" % w, "points:window.POINTS_%d" % w)

# 6) b1 deve avere .badge/.codeTitle/.codeNote dentro l'oggetto b1, non al livello entry
def move_into_b1(s, w):
    pat = re.compile(r'(\n  %d:\s*\{)( badge:\'SSN\', codeTitle:\'([^\']*)\', codeNote:\'([^\']*)\')(.*?b1:\{)' % w, re.S)
    m = pat.search(s)
    if not m:
        return s
    repl = m.group(1) + m.group(5) + " badge:'SSN', codeTitle:'" + m.group(2) + "', codeNote:'" + m.group(3) + "'"
    # ricostruisce: dopo b1:{ inseriamo i campi
    s = s[:m.start()] + repl + s[m.end():]
    return s

for w in EXTRA:
    s = move_into_b1(s, w)

io.open(P, 'w', encoding='utf-8').write(s)
print('patched')
