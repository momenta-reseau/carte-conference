#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verifier.py — la barrière avant toute publication.

    python3 verifier.py

🔴 Le dépôt est PUBLIC. Tout ce qui entre dans index.html est lisible par
n'importe qui, pour toujours, y compris dans l'historique git. Ce script refuse
la publication si un interdit y figure. Il ne corrige rien, il bloque.
"""
import html
import re
import sys
from pathlib import Path

PAGE = Path(__file__).resolve().parent / "index.html"

# Autorité : la table de traçabilité de Trousse-financement-employeur.md
INTERDITS = {
    "Rio Tinto": "gratuité stratégique, jamais une cliente",
    "Desjardins": "gratuité stratégique, jamais une cliente",
    "Beneva": "gratuité stratégique, jamais une cliente",
    r"\bCGI\b": "gratuité stratégique, jamais une cliente",
    r"\bBCF\b": "la page d'impact ne nomme plus BCF depuis le 2026-07-29",
    "Léger": "sondage Jeune Chambre sous entente de confidentialité",
    "Jeune Chambre": "sondage sous entente de confidentialité",
    r"20\s*[àa-]\s*40\s*%": "outcome du site, provenance non documentée (Signal-012)",
    r"\+?53\s*%": "outcome du site, provenance non documentée (Signal-012)",
    r"67\s*%": "outcome du site, provenance non documentée (Signal-012)",
    r"100\s*%\s*(des\s+)?(participantes\s+)?recommand": "outcome non documenté",
    r"87\s*%": "outcome du site, provenance non documentée (Signal-012)",
    "ARIHQ": "attribution non vérifiable du 58 % à 200 %",
    r"départ d.une employée": "MC dit « le remplacement d'une employée qui ne revient pas »",
}

if not PAGE.exists():
    sys.exit("ARRÊT : index.html absent. Lancer build.py d'abord.")

brut = PAGE.read_text(encoding="utf-8")
texte = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(
    r"<(script|style)[^>]*>.*?</\1>", " ", brut, flags=re.S)))

fautes = [f"{m} — {pourquoi}" for m, pourquoi in INTERDITS.items()
          if re.search(m, texte, re.I)]
if re.search(r"[—–]", texte):
    fautes.append("tiret cadratin ou demi-cadratin — règle dure du protocole")

if fautes:
    print("\nPUBLICATION REFUSÉE\n" + "-" * 19)
    for f in fautes:
        print(f"  ⛔ {f}")
    sys.exit(1)

print(f"ok  {len(INTERDITS)} interdits vérifiés, aucun présent")
print(f"ok  {len(texte.split())} mots dans la page")
