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

# ── L'échelle typographique, cinq crans et pas un sixième ────────────────────
#
# ✏️ David, 2026-08-27 : « les plus petits formats de police sont trop petits.
# Regarde ce qu'on fait dans Mon Espace pour t'y fier. »
#
# 🔴 Le défaut n'était pas une taille mais leur NOMBRE : huit valeurs fixes
# coexistaient, dont 13 et 14 px que personne ne distingue. Mon Espace a réglé le
# même problème le 2026-08-17 et en a tiré la règle : la hiérarchie se fait par la
# graisse et la couleur, pas par des demi-pixels.
#
# 🔴 Ce contrôle existe parce qu'une échelle se défait par une seule ligne de CSS
# ajoutée un soir. Il en a d'ailleurs attrapé une le jour même : `.titre-conf h3`
# portait un 16 px en dur, un neuvième cran né d'une seule règle, qui écrivait le
# titre d'une demande plus petit que le corps qui le suivait.
#
# Ce qui reste autorisé en dur : les grands titres, qui vivent en `clamp()` et
# dépassent tous le cran le plus haut, et le CSS d'impression en points.
# 🔴 Deuxième passe, le même jour. `--t-detail` est SUPPRIMÉ de la liste, pas
# renommé : c'était un second corps de texte que rien ne distinguait du premier,
# et son nom accueillait n'importe quoi. Quatre crans, un par rôle. Si ce
# contrôle échoue sur un cran inconnu, la bonne réponse est de rattacher la règle
# à un rôle existant, jamais d'ajouter une entrée ici.
CRANS = {"var(--t-titre)", "var(--t-section)", "var(--t-corps)", "var(--t-source)"}
PLANCHER_PX = 15   # `--t-source`. Legge et Bigelow 2011 : 14 px passent sous la
                   # plage de lecture fluente dès que le téléphone s'éloigne.

for m in re.finditer(r"font-size:\s*([^;}\n]+)", brut):
    v = m.group(1).strip()
    if any(c in v for c in CRANS) or v.endswith("pt"):
        continue
    px = re.match(r"^(\d+(?:\.\d+)?)px$", v)
    if px and float(px.group(1)) < PLANCHER_PX:
        fautes.append(f"font-size:{v} — sous le plancher de {PLANCHER_PX} px")
    elif px and float(px.group(1)) <= 26:
        fautes.append(f"font-size:{v} — taille en dur hors des cinq crans")

if fautes:
    print("\nPUBLICATION REFUSÉE\n" + "-" * 19)
    for f in fautes:
        print(f"  ⛔ {f}")
    sys.exit(1)

print(f"ok  {len(INTERDITS)} interdits vérifiés, aucun présent")
print(f"ok  échelle typographique : {len(CRANS)} crans, plancher à {PLANCHER_PX} px")
print(f"ok  {len(texte.split())} mots dans la page")
