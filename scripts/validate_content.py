#!/usr/bin/env python3
import sys, yaml, re
from pathlib import Path

def check():
    for f in Path("content").rglob("*.md"):
        text = f.read_text()
        if "sonno" in f.name or "seggiolini" in f.name or "alimentazione" in f.name:
            if "Fonti:" not in text:
                print(f"ERRORE: {f} manca Fonti istituzionali")
                sys.exit(1)
            if not re.search(r"prezzo_verificato_il:\s*\d{2}/\d{2}/\d{4}", text):
                print(f"ERRORE: {f} manca prezzo_verificato_il")
                sys.exit(1)
    print("Validazione OK")

if __name__ == "__main__":
    check()
