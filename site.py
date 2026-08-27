#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""site.py — la page de Marie-Claude Viau, écrite d'un seul tenant.

    python3 site.py

UN SEUL FICHIER, et c'est une décision. La version précédente en avait trois :
le contenu, le gabarit, et un vérificateur qu'il fallait penser à lancer. Pour
une page de cinq blocs et quatre cent cinquante mots, cette cérémonie coûtait
plus qu'elle ne rapportait, et le vérificateur séparé pouvait s'oublier. Ici les
contrôles tournent AVANT l'écriture : si l'un échoue, aucun fichier ne sort.

À QUI ELLE PARLE. Un planificateur d'événements qui vient de voir Marie-Claude
parler douze minutes, debout dans une salle, sur son téléphone, trente secondes
d'attention. Il doit pouvoir faire trois choses, dans cet ordre : la joindre,
savoir quoi lui demander, se rappeler pourquoi elle valait le coup.

CE QU'ELLE NE FAIT PAS. Elle ne vend pas. Marie-Claude, 2026-08-27 : « je veux
pas vendre de conférence, c'est pas dans mon carré de sable ». Aucun prix, aucun
formulaire, aucun catalogue. Une demande qui ne coûte rien à accepter.
"""
import html
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "index.html"

# ═════════════════════════════════════════════════════════════════════════════
# LE CONTENU
# ═════════════════════════════════════════════════════════════════════════════

MC = {
    "nom": "Marie-Claude Viau",
    "role": "Fondatrice de Momenta · Conférencière et panéliste",
    "courriel": "mcviau@momentareseau.com",
    "tel": "514 889-9649",
    "tel_lien": "+15148899649",
    "linkedin": "https://www.linkedin.com/company/momentareseau",
    "site": "https://www.momentareseau.com",
    "ville": "Bromont, Québec",
}

# ✏️ David, 2026-08-27 : la phrase passe entre guillemets, « c'est sa citation ».
# 🔴 Et TOUTE LA PAGE passe au « je ». Ce n'est pas un détail de style : une fiche
# écrite à la troisième personne parle DE quelqu'un, et un acheteur la lit comme
# un dossier. Au « je », c'est elle qui parle, et c'est cohérent avec ce que le
# banc mesure (MacKrill, n = 1 866 : le registre « inspiring » va avec le « je »,
# le registre « informative » va contre).
#
# L'appui a sauté avec la même consigne : « ce n'est pas nécessaire ». Il glosait
# la citation, et la signature devenait inutile dès lors que la page entière est
# écrite à sa voix.
ACCROCHE = {
    # 🔴 L'espace avant le saut n'est pas décorative : le saut est neutralisé sur
    # téléphone, et sans elle les deux moitiés se collent.
    "phrase": "« Je bâtis ce que j’aurais voulu trouver <br>"
              "lors de ma propre transition parentale. »",
}

# Trois demandes, et pas un catalogue. Chacune est une case différente dans une
# programmation, avec un budget et un risque différents.
DEMANDES = [
    ("Une conférence d’inspiration",
     "Mon récit, seule sur scène, en ouverture ou en clôture de journée."),
    ("Une place en panel",
     "Mon expertise sur la transition parentale et l’accomplissement personnel, "
     "dans un format de discussion."),
    ("De la formation sur mesure",
     "En entreprise, sur la conciliation travail-famille, en particulier pour les "
     "femmes en transition parentale."),
]

SUJETS = "Deux sujets : la transition parentale, et l’accomplissement personnel."

JALONS = [
    ("20 ans", "dans le milieu des affaires"),
    ("15 ans", "dans le milieu de la conférence"),
    ("10 ans", "à former des femmes en leadership"),
]

PARCOURS = (
    "À l’Institut de Leadership, j’ai cofondé le programme Femmes Leaders. "
    "Dix ans à écouter des femmes parler d’ambition en salle et de charge "
    "mentale aux pauses."
)

# 🔴 Le fait qui sépare le témoignage de l'expertise, et le seul que la
# concurrence ne peut pas produire en racontant son propre accouchement.
CERTIFICATION = (
    "Je suis certifiée en transition parentale par le Center for Parental Leave "
    "Leadership, l’organisme américain fondé par Amy Beacom (Ph. D.)."
)

# L'idée est de MC : « ils vont voir qu'elle travaille avec des tops ». Six noms
# de sommités font plus que n'importe quelle phrase qu'elle écrirait sur elle.
# ⛔ AUCUN TITRE D'ATELIER. Le site public et les fiches du wiki divergent sur
# les six, et la fiche fait autorité. Les titres professionnels, eux, concordent.
FORMATRICES = [
    ("Sonia Lupien",
     "Ph. D., directrice du Centre d’études sur le stress humain, "
     "autrice de « Par amour du stress »"),
    ("Lory Zéphyr",
     "Ph. D., psychologue en périnatalité, autrice aux Éditions de l’Homme"),
    ("Marylise Champagne",
     "Conseillère en orientation, fondatrice de Dix mille matins"),
    ("Mylène Houle Morency",
     "Formatrice agréée et autrice en conciliation travail-famille"),
    ("Marie-Hélène Langlois",
     "Associée et consultante principale, SISMIK Impact"),
    ("Amélie Mongrain",
     "M. Sc., fondatrice d’Ella Conseils, spécialiste de la transition parentale"),
]

# Usage éditorial : ce sont des médias qui l'ont couverte, pas des partenaires.
# ⛔ Le logo de l'Ordre des CRHA n'entrera jamais ici : l'Ordre le réserve aux
# personnes inscrites à son tableau, et une entreprise ne peut pas l'afficher.
MEDIAS = [
    ("assets/medias/radio-canada.png", "Radio-Canada", 584, 102),
    ("assets/medias/tva-nouvelles.png", "TVA Nouvelles", 341, 102),
    ("assets/medias/noovo-info.png", "Noovo Info", 102, 102),
]
BALADOS = ["Elles, le balado", "Bon Papa", "Startop", "UMEA"]
PRESSE = "Je porte le sujet dans les médias québécois depuis 2026."
PRIX = ("Prix coup de cœur au Défi OSEntreprendre 2026, "
        "volet régional Haute-Yamaska et Brome-Missisquoi")

# Une demande qui ne coûte rien à accepter. « Réservez une date » exige un budget
# et un comité ; « dites-nous ce que vous programmez » exige un courriel.
APPEL = {
    "titre": "Une date, une programmation, une idée ?",
    "texte": "Dites-moi ce que vous organisez et ce que vous cherchez à faire "
             "vivre à votre salle. Je réponds moi-même.",
}

# ═════════════════════════════════════════════════════════════════════════════
# LES CONTRÔLES — ils tournent avant l'écriture, pas après
# ═════════════════════════════════════════════════════════════════════════════

# 🔴 LE DÉPÔT EST PUBLIC. Tout ce qui entre ici est lisible pour toujours,
# historique git compris. Autorité : la table de traçabilité de
# `Ce-que-je-vends/Marketing/Trousse-financement-employeur.md`.
INTERDITS = {
    r"Rio Tinto|Desjardins|Beneva|\bCGI\b": "gratuité stratégique, jamais une cliente",
    r"\bBCF\b": "la page d'impact ne nomme plus BCF depuis le 2026-07-29",
    r"Léger|Jeune Chambre": "sondage sous entente de confidentialité",
    r"20\s*[àa-]\s*40\s*%|\+?53\s*%|67\s*%|87\s*%": "outcome du site, provenance non documentée",
    r"100\s*%\s*(des\s+)?(participantes\s+)?recommand": "outcome non documenté",
    "ARIHQ": "attribution non vérifiable du 58 % à 200 %",
    r"départ d.une employée": "MC dit « le remplacement d'une employée qui ne revient pas »",
    r"[—–]": "tiret cadratin ou demi-cadratin, règle dure du protocole anti-signature IA",
    r"\d[\d\s ]*\$": "aucun prix sur cette page : elle provoque un appel, elle ne vend pas",
}


def controler(page):
    """Retourne la liste des fautes. Une seule suffit à empêcher l'écriture."""
    texte = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(
        r"<(script|style)[^>]*>.*?</\1>", " ", page, flags=re.S)))
    fautes = [f"« {m} » : {pourquoi}"
              for m, pourquoi in INTERDITS.items() if re.search(m, texte, re.I)]

    # 🔴 L'ÉCHELLE. Quatre crans de texte, deux d'affichage, et rien d'autre.
    # Une taille en dur est le début de la dérive : personne ne distingue 13 px
    # de 14, mais le code finit par porter les deux et la hiérarchie se dissout.
    for m in re.finditer(r"font-size:\s*([^;}\n]+)", page):
        v = m.group(1).strip()
        if v.startswith("var(--t-") or v.endswith("pt"):
            continue
        fautes.append(f"font-size:{v} — hors des crans nommés")

    # 🔴 L'ORDRE. La phrase pèse plus que le nom : sur cette page, ce qui doit
    # rester est ce qu'elle dit, pas comment elle s'appelle. Un contrôle de
    # tailles ne l'attrape pas, les deux valeurs étant légitimes séparément.
    def bornes(jeton):
        m = re.search(rf"{jeton}:\s*clamp\(\s*([\d.]+)rem[^,]*,[^,]+,\s*([\d.]+)rem\)", page)
        return (float(m.group(1)), float(m.group(2))) if m else None

    aff, nom = bornes("--t-affiche"), bornes("--t-nom")
    if aff and nom:
        for i, bout in enumerate(("plancher", "plafond")):
            if aff[i] < nom[i]:
                fautes.append(f"au {bout}, --t-affiche passe sous --t-nom : "
                              "la phrase doit peser plus que le nom")
    return fautes


# ═════════════════════════════════════════════════════════════════════════════
# LA FORME
# ═════════════════════════════════════════════════════════════════════════════

FINE, INSEC = " ", " "


def typo(t):
    """Les espaces insécables du français.

    Sans ça, « 100 000 $ » se coupe entre le 100 et le 000 en fin de ligne et
    le « % » peut se retrouver seul au début de la suivante.
    """
    for _ in range(3):                       # séparateur de milliers, en cascade
        # La négation exclut les numéros de téléphone : « 514 889-9649 » n'est
        # pas un millier, et recevait une espace fine sans elle.
        t = re.sub(r"(\d)\s(\d{3})\b(?![\s]*[-‑])", rf"\1{FINE}\2", t)
    t = re.sub(r"(\d)\s+([%$€])", rf"\1{INSEC}\2", t)
    t = re.sub(r"\s+([;:!?])", rf"{FINE}\1", t)
    return t.replace("« ", f"«{FINE}").replace(" »", f"{FINE}»")


def e(t):
    """Échappe, compose, et laisse passer les sauts voulus."""
    return typo(html.escape(t).replace("&lt;br&gt;", "<br>"))


CSS = """
*,*::before,*::after{box-sizing:border-box}

/* ═══ Les jetons ═══════════════════════════════════════════════════════════
   Palette : autorité `Boite-a-outils/Identite-visuelle.md`. Le dosage mesuré
   du vrai site est ~73 % de neutres, ~24 % de vert nuit, 2 % de corail. AUCUNE
   ombre portée : 142 déclarations sur 148 valent `none` sur momentareseau.com.

   L'échelle : quatre crans de texte, deux d'affichage. Elle S'OUVRE avec la
   largeur. Sur un téléphone la page ne sert que quatre tailles (26/20/17/15),
   parce que deux crans séparés de deux pixels ne créent pas de hiérarchie, ils
   créent du bruit ; les crans d'affichage s'y rejoignent et la couleur prend le
   relais. Sur écran large ils se séparent et la page en sert six.

   Le plancher de 15 px est mesuré, pas jugé. Legge et Bigelow, Journal of
   Vision 2011 : la lecture fluente commence à 1,40 mm de hauteur d'x à 40 cm.
   Sur un iPhone avec Montserrat, 14 px donnent 1,32 mm et 15 px donnent 1,41. */
:root{
  --vert:#01282b; --vert2:#3e5b5d; --corail:#ff706b;
  --creme:#f2f0eb; --blanc:#fcfcfa; --gris:#ded9d4;
  --rayon:12px; --large:900px;
  --t-affiche: clamp(1.625rem, 3.4vw, 2.625rem);  /* 26-42  ce qui doit rester */
  --t-nom:     clamp(1.25rem, 2.8vw, 2.125rem);   /* 20-34  qui parle, un jalon */
  --t-titre:   clamp(1.25rem, 2vw, 1.625rem);     /* 20-26  le nom d'une section */
  --t-section: 1.25rem;                           /* 20     un titre de bloc     */
  --t-corps:   1.0625rem;                         /* 17     tout le texte        */
  --t-source:  .9375rem;                          /* 15     une attribution      */
}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--creme); color:var(--vert);
  font-family:Montserrat,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size:var(--t-corps); line-height:1.55;
}
.dedans{max-width:var(--large); margin:0 auto; padding:0 20px}
section{padding:40px 0}
section+section{border-top:1px solid var(--gris)}
h1,h2,h3{margin:0; font-weight:700; line-height:1.15; letter-spacing:-.01em}
h2{font-size:var(--t-titre); margin-bottom:8px}
h3{font-size:var(--t-section)}
p{margin:0 0 12px}
p:last-child{margin-bottom:0}

/* 🔴 UNE CLASSE EST UN RÔLE, JAMAIS UN EMPLACEMENT. Une règle qui se nomme par
   ce qui l'entoure (« la source, dans le bloc du haut ») finit par attraper des
   choses qui n'ont rien à voir : une signature d'auteur et l'attribution d'un
   chiffre ne sont pas la même chose et ne peuvent pas partager un style. */
.doux{color:var(--vert2); max-width:68ch}     /* ce qui accompagne */
.source{font-size:var(--t-source); color:var(--vert2); margin-top:6px}

/* ═══ En-tête ═════════════════════════════════════════════════════════════ */
header{background:var(--vert); color:var(--blanc); padding:40px 0 36px}
header .logo{height:26px; display:block; margin-bottom:28px}
header h1{font-size:var(--t-nom)}
header .role{color:var(--gris); margin-top:10px}

/* La feuille se pose telle quelle. 🔴 Le masque est DANS le PNG, découpé par
   ~/bin/feuille_momenta.py. Ne jamais lui remettre un border-radius par-dessus :
   la vraie forme est une superellipse, la fausse l'abîmerait. */
.duo{display:flex; flex-direction:column-reverse; gap:26px}
.portrait{width:min(230px,58%); height:auto; display:block; align-self:flex-start}
@media(min-width:760px){
  .duo{flex-direction:row; align-items:center; justify-content:space-between; gap:36px}
  .duo .texte{flex:1; min-width:0}
  .portrait{width:250px; flex:none; align-self:center}
}

/* ═══ Les contacts, le geste le plus important de la page ═════════════════ */
.contacts{display:flex; flex-wrap:wrap; gap:10px; margin-top:24px}
.contacts a{
  display:inline-flex; align-items:center; gap:8px;
  padding:12px 20px; border-radius:25px; text-decoration:none;
  font-size:var(--t-corps); font-weight:600; border:2px solid transparent;
  transition:background-color 160ms ease-out, color 160ms ease-out;
}
.contacts .plein{background:var(--corail); color:var(--blanc)}
.contacts .plein:hover{background:#ff8a86}
.contacts .vide{border-color:var(--gris); color:var(--blanc)}
.contacts .vide:hover{background:rgba(255,255,255,.08)}
.contacts svg{width:17px; height:17px; flex:none; fill:currentColor}
.contacts a:active{transform:translateY(1px)}
/* Le geste principal de cette page est de cliquer un lien. Sans anneau de
   focus, qui navigue au clavier ne sait pas où il est. */
.contacts a:focus-visible,footer a:focus-visible{
  outline:3px solid var(--corail); outline-offset:3px; border-radius:25px;
}

/* ═══ L'accroche ══════════════════════════════════════════════════════════ */
.phrase{font-size:var(--t-affiche); font-weight:700; line-height:1.18;
  letter-spacing:-.015em; margin-bottom:16px}
/* Un filet à gauche, jamais un cadre : le kit ne cerne rien. Il marque la phrase
   comme une parole rapportée, et il empêche les trois sections crème de se
   suivre sans relief. */
.citation{padding-left:22px; border-left:3px solid var(--corail); margin:0}
/* Le saut est écrit pour couper la phrase en deux sur un écran large. Sur un
   téléphone chaque moitié se recasse, et une accroche sur quatre lignes ne
   s'accroche plus, elle se lit. */
@media(max-width:640px){.phrase br{display:none}}
/* 🔴 La signature a disparu avec l'appui : dès lors que la page entière est
   écrite au « je », elle est signée de bout en bout et une attribution sous la
   citation redirait le nom qui est déjà dans l'en-tête. */

/* ═══ Les cartes ══════════════════════════════════════════════════════════ */
.trois{display:grid; gap:12px; grid-template-columns:1fr; margin:16px 0}
@media(min-width:760px){.trois{grid-template-columns:repeat(3,1fr)}}
.carte{background:var(--blanc); border-radius:var(--rayon); padding:20px}
.carte h3{color:var(--corail); line-height:1.3}
.carte p{font-size:var(--t-corps); color:var(--vert2); margin:8px 0 0}

/* ═══ Les jalons ══════════════════════════════════════════════════════════ */
.jalons{display:flex; flex-wrap:wrap; gap:24px; margin:4px 0 16px}
.jalon .n{font-size:var(--t-nom); font-weight:700; color:var(--corail); line-height:1}
.jalon p{margin:4px 0 0; color:var(--vert2); max-width:225px}

/* ═══ Les formatrices ═════════════════════════════════════════════════════
   Une liste, pas des cartes : ce sont des noms qu'on parcourt pour en
   reconnaître un. Une grille de six ferait un mur à déchiffrer. */
.gens{margin:14px 0 4px}
.qui{padding:12px 0; display:flex; flex-wrap:wrap; align-items:baseline; gap:4px 12px}
.qui+.qui{border-top:1px solid var(--gris)}
.qui strong{font-size:var(--t-corps); min-width:214px}
.qui span{font-size:var(--t-corps); color:var(--vert2); flex:1}
@media(max-width:640px){
  .qui{display:block}
  .qui strong{display:block; min-width:0}
  .qui span{display:block; margin-top:2px}
}

/* ═══ Les logos ═══════════════════════════════════════════════════════════
   Hauteur des LETTRES égalisée, pas celle des cadres : le carré de Noovo
   n'occupe que ~60 % de sa hauteur en lettrage, il monte donc plus haut. */
.logos{display:flex; flex-wrap:wrap; align-items:center; gap:26px 36px; margin:16px 0}
.logos img{height:34px; width:auto; display:block}
.logos img[width="102"]{height:52px}
@media(max-width:520px){
  .logos{gap:22px 26px} .logos img{height:27px}
  .logos img[width="102"]{height:42px}
}
.puces{display:flex; flex-wrap:wrap; gap:8px; margin:12px 0 16px}
.puces span{background:var(--gris); border-radius:25px; padding:8px 16px;
  font-size:var(--t-corps)}

/* ═══ L'appel, la dernière chose qu'on lit ════════════════════════════════ */
.appel{background:var(--vert); color:var(--blanc)}
.appel h2{color:var(--blanc)}
.appel .phrase{margin-bottom:12px}
.appel .doux{color:var(--gris)}
.appel .source{color:var(--gris)}

footer{background:var(--vert); color:var(--gris); padding:32px 0;
  font-size:var(--t-source)}
footer .logo{height:22px; display:block; margin-bottom:20px}
footer a{color:inherit; text-decoration:underline; text-underline-offset:2px}
footer a:hover{color:var(--blanc)}

/* La page imprimée devient la pièce jointe qu'on fait suivre à son comité. */
@media print{
  body{background:var(--blanc); font-size:11pt}
  header,footer,.appel{background:var(--blanc)!important; color:var(--vert)!important}
  header .role,footer,.appel .doux{color:var(--vert2)!important}
  .contacts{display:none}
  .portrait{width:150px}
  section{padding:16px 0; break-inside:avoid}
  .carte{border:1px solid var(--gris)}
}
"""

ICONES = {
    "courriel": 'M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 '
                '00-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z',
    "tel": 'M6.6 10.8a15 15 0 006.6 6.6l2.2-2.2a1 1 0 011-.2 11 11 0 003.5.6 1 '
           '1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 '
           '1c0 1.2.2 2.4.6 3.5a1 1 0 01-.3 1l-2.2 2.3z',
    "in": 'M6.9 21H3.4V9h3.5v12zM5.1 7.4a2 2 0 110-4.1 2 2 0 010 4.1zM21 21h-3.5v-5.8'
          'c0-1.4 0-3.2-2-3.2s-2.2 1.5-2.2 3.1V21H9.9V9h3.3v1.6h.1a3.7 3.7 0 013.3-1.8'
          'c3.5 0 4.2 2.3 4.2 5.3V21z',
    "web": 'M12 2a10 10 0 100 20 10 10 0 000-20zm6.9 6h-3a15.6 15.6 0 00-1.4-3.6A8 8 '
           '0 0118.9 8zM12 4c.7 1 1.2 2.3 1.6 4h-3.2c.4-1.7.9-3 1.6-4zM4.3 14a8 8 0 '
           '010-4h3.4a16.6 16.6 0 000 4H4.3zm.8 2h3a15.6 15.6 0 001.4 3.6A8 8 0 015.1 '
           '16zm3-8h-3a8 8 0 014.4-3.6A15.6 15.6 0 008.1 8zM12 20c-.7-1-1.2-2.3-1.6-4h3.2'
           'c-.4 1.7-.9 3-1.6 4zm2-6h-4a14.7 14.7 0 010-4h4a14.7 14.7 0 010 4zm.5 5.6'
           'a15.6 15.6 0 001.4-3.6h3a8 8 0 01-4.4 3.6zm1.8-5.6a16.6 16.6 0 000-4h3.4a8 '
           '8 0 010 4h-3.4z',
}


def lien(url, texte, icone, plein=False):
    return (f'<a href="{url}" class="{"plein" if plein else "vide"}">'
            f'<svg viewBox="0 0 24 24"><path d="{ICONES[icone]}"/></svg>{e(texte)}</a>')


def rendre():
    demandes = "".join(f'<div class="carte"><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                       for t, d in DEMANDES)
    jalons = "".join(f'<div class="jalon"><div class="n">{e(n)}</div><p>{e(t)}</p></div>'
                     for n, t in JALONS)
    gens = "".join(f'<div class="qui"><strong>{e(n)}</strong><span>{e(t)}</span></div>'
                   for n, t in FORMATRICES)
    logos = "".join(f'<img src="{s}" alt="{e(a)}" width="{w}" height="{h}" loading="lazy">'
                    for s, a, w, h in MEDIAS)
    puces = "".join(f"<span>{e(b)}</span>" for b in BALADOS)

    return f"""<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(MC['nom'])} · Conférencière et panéliste</title>
<meta name="description" content="{e(SUJETS)}">
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/favicon-180.png">
<meta name="theme-color" content="#01282b">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<header><div class="dedans">
  <img class="logo" src="assets/logo-light.png" alt="Momenta">
  <div class="duo">
    <div class="texte">
      <h1>{e(MC['nom'])}</h1>
      <div class="role">{e(MC['role'])}</div>
      <div class="contacts">
        {lien("mailto:" + MC['courriel'], "Écrire à Marie-Claude", "courriel", True)}
        {lien("tel:" + MC['tel_lien'], MC['tel'], "tel")}
        {lien(MC['linkedin'], "LinkedIn", "in")}
        {lien(MC['site'], "momentareseau.com", "web")}
      </div>
    </div>
    <img class="portrait" src="assets/mc-feuille.png"
         alt="Portrait de {e(MC['nom'])}" width="760" height="760">
  </div>
</div></header>

<section><div class="dedans">
  <p class="phrase citation">{e(ACCROCHE['phrase'])}</p>
</div></section>

<section><div class="dedans">
  <h2>Ce que vous pouvez me demander</h2>
  <p class="doux">{e(SUJETS)}</p>
  <div class="trois">{demandes}</div>
</div></section>

<section><div class="dedans">
  <h2>D’où je parle</h2>
  <div class="jalons">{jalons}</div>
  <p class="doux">{e(PARCOURS)}</p>
  <p class="doux">{e(CERTIFICATION)}</p>
  <div class="logos">{logos}</div>
  <p class="doux">{e(PRESSE)}</p>
  <div class="puces">{puces}</div>
  <p class="doux">{e(PRIX)}</p>
  <h3 style="margin-top:28px">Avec qui je travaille</h3>
  <p class="doux">Le parcours que j’ai bâti est animé par des sommités
     québécoises. Elles interviennent aussi en entreprise.</p>
  <div class="gens">{gens}</div>
  <div class="source">momentareseau.com, parcours Essentielle</div>
</div></section>

<section class="appel"><div class="dedans">
  <h2>{e(APPEL['titre'])}</h2>
  <p class="doux">{e(APPEL['texte'])}</p>
  <!-- ✏️ David : « le seul call to action c'est écrire à MC ». Le téléphone
       sort d'ici. Deux boutons côte à côte ne sont pas un appel, c'est un choix,
       et un choix se remet à plus tard. Le numéro reste joignable dans l'en-tête
       et dans le pied, où il est une coordonnée et non une action. -->
  <div class="contacts">
    {lien("mailto:" + MC['courriel'], "Écrire à Marie-Claude", "courriel", True)}
  </div>
</div></section>

<footer><div class="dedans">
  <img class="logo" src="assets/logo-light.png" alt="Momenta">
  <p>{e(MC['nom'])} · {e(MC['ville'])}<br>
    <a href="mailto:{MC['courriel']}">{e(MC['courriel'])}</a> ·
    <a href="tel:{MC['tel_lien']}">{e(MC['tel'])}</a></p>
  <p><a href="{MC['linkedin']}">LinkedIn</a> ·
     <a href="{MC['site']}">momentareseau.com</a></p>
</div></footer>

</body></html>
"""


if __name__ == "__main__":
    page = rendre()
    fautes = controler(page)
    if fautes:
        print("PUBLICATION REFUSÉE\n" + "-" * 19)
        for f in fautes:
            print(f"  ⛔ {f}")
        sys.exit(1)
    SORTIE.write_text(page, encoding="utf-8")
    lisible = re.sub(r"<[^>]+>", " ", re.sub(r"<style[^>]*>.*?</style>", " ", page, flags=re.S))
    mots = len(lisible.split())
    print(f"écrit : {SORTIE}")
    print(f"  {len(page)} octets · {mots} mots · {page.count('<section')+1} blocs")
    print(f"  {len(INTERDITS)} interdits vérifiés · échelle à six crans · plancher 15 px")
