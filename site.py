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
    # 🔴 Deux LinkedIn distincts, et ils ne servent pas la même chose. La PAGE de
    # l'entreprise vit dans l'en-tête, parce qu'un acheteur qui explore veut voir
    # Momenta. Le PROFIL de Marie-Claude va dans la fiche de contact, parce qu'un
    # contact enregistré, c'est une personne. Confondre les deux fait suivre une
    # marque à quelqu'un qui voulait suivre une personne.
    "linkedin_perso": "https://www.linkedin.com/in/marieclaudeviau",
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
# ✏️ David, 2026-08-27, sa formulation, retenue telle quelle.
#
# 🔴 Elle tient en deux temps et c'est le SAUT qui fait la phrase : le premier
# membre pose l'habitude, le second retire tout. Une opposition a besoin de deux
# lignes pour se voir ; mise en flux, elle devient une remarque.
#
# 📄 C'est le geste de sa diapo 6 : « on prépare les femmes à devenir leaders, on
# prépare les entreprises à performer. Mais personne ne prépare le retour. »
#
# 🔴 Pas de guillemets ici, contrairement aux versions précédentes : ce n'est plus
# une parole à la première personne mais un constat. Le filet corail suffit à la
# poser, et le « je » revient dans l'appui, qui dit ce qu'elle en a fait.
ACCROCHE = {
    # 🔴 Ce saut-là ne se neutralise PAS sur téléphone. Les précédents coupaient
    # une phrase trop longue et pouvaient tomber ailleurs sans dommage ; celui-ci
    # sépare deux propositions qui s'opposent. Le supprimer casserait la phrase.
    "phrase": "On prépare toujours le départ.<br>Jamais le retour.",
    "appui": "Le retour au travail après un congé parental : j’ai bâti ce que "
             "j’aurais voulu trouver à ce moment-là, pour les femmes et les "
             "organisations qui traversent cette transition.",
}

# ✏️ David, 2026-08-28 : « une section statistique qui fait sortir les
# statistiques les plus percutantes qu'on a dans le wiki », trois d'entre elles.
#
# 📄 Autorité : `Ce-que-je-vends/Stats-conge-parental-sources.md`, où chaque
# chiffre porte sa source, son échantillon et la réponse à donner si on la
# challenge. Trois sur une trentaine, et le tri n'a pas été fait sur le punch :
# la moitié de l'arsenal est inutilisable ICI. Les outcomes du programme sont
# sous Signal-012 (provenance jamais documentée), les montants en dollars sont
# interdits sur une page qui ne vend rien, et les stats de cabinets d'avocats
# parlent à un acheteur B2B, pas à un planificateur.
#
# 🔴 L'ordre fait l'argument, et il n'est pas décoratif : elles reviennent toutes,
# une sur trois y laisse sa confiance, et le soutien change la donne. Le premier
# chiffre installe, le deuxième blesse, le troisième répond. Retirer celui du
# milieu laisserait un problème sans dommage ; retirer le dernier laisserait un
# dommage sans issue, et la page se terminerait sur un constat déprimant.
#
# 🟡 Le troisième est reformulé par rapport au pitch du wiki, qui dit « le
# soutien structuré au retour de congé réduit la dépression et le burnout ». La
# revue du Lancet mesure l'effet du CONGÉ PARENTAL sur la santé mentale des
# parents, pas celui d'un accompagnement au retour. La formulation d'ici reste
# ce que la revue démontre vraiment. Un chiffre qu'on affiche sur une page
# publique doit tenir si quelqu'un ouvre l'article, et celui-là est le seul des
# trois dont le pitch oral s'éloignait de la source.
#
# 🔴 La source se lit sous chaque chiffre, pas en note de bas de page. C'est ce
# qui sépare une page de conférencière d'une infographie : un planificateur qui
# reprend un chiffre dans sa propre note interne a besoin de savoir d'où il
# vient, et il ne reviendra pas le chercher.
CHIFFRES = [
    ("88 %",
     "des mères canadiennes retournent au travail après leur congé parental.",
     "Statistique Canada, cohortes 2009 et 2019"),
    ("1 sur 3",
     "perd confiance en ses capacités professionnelles au retour.",
     "Benefits Canada, sondage auprès de 1 000 Canadiennes"),
    ("49 études",
     "recensées par The Lancet. Mieux le congé parental est soutenu, meilleure "
     "est la santé mentale des mères.",
     "The Lancet Public Health, 2023, revue systématique"),
]
CHIFFRES_TITRE = "Le sujet en trois chiffres"
CHIFFRES_INTRO = "Les chiffres que je cite en salle, avec leur source."

# Trois demandes, et pas un catalogue. Chacune est une case différente dans une
# programmation, avec un budget et un risque différents.
# ✏️ David : « donne un peu plus de détails » sur la conférence, et « une place
# comme PANÉLISTE, pas en panel ».
#
# 🔴 Il a raison sur les deux plans. « En panel » calque l'anglais et nomme un
# format ; « comme panéliste » nomme une PERSONNE, ce qu'un planificateur cherche
# quand il remplit une table ronde. On n'achète pas un panel, on invite quelqu'un.
#
# 📄 Le détail du récit vient du deck : le postpartum non diagnostiqué, la
# remontée par la course, et ce qu'elle a quitté pour fonder Momenta. Tout est
# déjà public (LinkedIn, Noovo, la lettre ouverte).
DEMANDES = [
    ("Une conférence d’inspiration",
     "Mon récit, seule sur scène : le postpartum que je n’ai pas vu venir, la "
     "remontée par la course, et ce que j’ai quitté pour bâtir Momenta. En "
     "ouverture ou en clôture de journée."),
    # ✏️ David, 2026-08-28 : « en discussion et sans support » s'en va.
    # 🔴 La phrase disait ce qu'elle n'apporte PAS. « Sans support » est un
    # renseignement de régie, pas un argument, et il fallait déjà savoir que
    # « support » veut dire diapositives pour le comprendre. Ce qui le remplace
    # nomme les dispositifs où elle entre : c'est ce qu'un planificateur coche
    # quand il remplit une grille, et ça suit la logique de la carte de gauche,
    # qui se termine elle aussi par un renseignement de programmation.
    ("Une place comme panéliste",
     "Mon expertise sur la transition parentale et l’accomplissement personnel, "
     "en table ronde, sur un plateau ou devant une salle."),
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

# ✏️ David, 2026-08-27, mot pour mot. La version d'avant disait « ambition en
# salle et charge mentale aux pauses » : joli, mais flou. Celle-ci nomme le sujet
# exact, et c'est le contraste qui porte l'argument — ce dont on parle sur scène
# n'est pas ce dont on parle quand le micro est fermé.
PARCOURS = (
    "À l’Institut de Leadership, j’ai cofondé le programme Femmes Leaders. "
    "Dix ans à écouter des femmes parler d’ambition durant les conférences, et "
    "de leurs difficultés de transition parentale durant les pauses."
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
    # 🐛 « Conseillère EN orientation » est une déformation d'un titre réservé.
    # L'OCCOQ est formel : seul « conseillère d'orientation » (c.o.) est réservé
    # par l'article 36 du Code des professions, et personne ne peut s'attribuer un
    # titre approchant. Le site de Momenta porte la même erreur, à signaler à MC.
    ("Marylise Champagne",
     "Conseillère d’orientation, fondatrice de Dix mille matins"),
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
# 📄 Chaque lien relevé sur momentareseau.com/medias, en lisant le DOM rendu
# plutôt que le HTML brut : GoHighLevel place les liens dans des blocs éloignés de
# leurs images, et l'association par proximité textuelle donnait n'importe quoi.
# Le rattachement fiable est géométrique, image et lien à la même ordonnée.
#
# ⚠️ Le lien de TVA passe par la redirection d'identification anonyme de Québecor.
# Elle boucle sous curl et se résout dans un navigateur : vérifié dans Chrome, la
# page s'ouvre sur la lettre ouverte et nomme Marie-Claude.
MEDIAS = [
    ("assets/medias/radio-canada.png", "Radio-Canada", 584, 102,
     "https://ici.radio-canada.ca/nouvelle/2259116/conge-maternite-accompagnement-marie-claude-viau"),
    ("assets/medias/tva-nouvelles.png", "TVA Nouvelles", 341, 102,
     "https://www.tvanouvelles.ca/2026/03/08/le-silence-sur-le-post-partum-nous-coute-des-talents"),
    ("assets/medias/noovo-info.png", "Noovo Info", 102, 102,
     "https://vimeo.com/1170824554/69fe8b024b"),
    # ✏️ David : « il faut ajouter le Journal de Montréal, sa lettre ouverte ».
    # 📄 Logo pris à la source, sur l'article lui-même, et recoloré en vert nuit :
    # celui du site est blanc, invisible sur crème. La variante sur DEUX lignes est
    # choisie contre l'horizontale : celle-ci fait 13,6:1 et aurait occupé le quart
    # de la rangée à hauteur égale ; la double fait 4,6:1, presque le ratio de
    # Radio-Canada.
    ("assets/medias/journal-de-montreal.png", "Le Journal de Montréal", 472, 102,
     "https://www.journaldemontreal.com/2026/03/08/le-silence-sur-le-post-partum-nous-coute-des-talents"),
]
# 📄 Extraites de momentareseau.com/medias, où elles sont déjà publiées. Ce sont
# des pochettes carrées avec des visages, pas des mots-symboles comme les logos
# de presse : elles se posent donc en vignettes, à part, et non dans la même
# rangée. Ramenées de 401 px et jusqu'à 293 ko à 144 px et 100 ko pour les quatre,
# parce qu'un acheteur les charge sur son forfait, debout dans une salle.
# 🔴 Deux libellés par pochette : le court se lit sous la vignette, le complet
# vit dans l'attribut alt. Une légende de 72 px de large qui se casse en deux
# lignes désaligne toute la rangée, et « le balado » n'apprend rien à personne.
# 🔴 Chaque pochette mène à L'ÉPISODE, pas au balado. Un acheteur veut l'entendre
# elle, pas découvrir une série. Le site de Momenta, lui, fait pointer les
# pochettes vers les sites des balados et met les épisodes dans une rangée de
# petites icônes en dessous.
#
# 🐛 Et cette lecture a trouvé un défaut SUR LE SITE DE MOMENTA : la pochette
# d'« Elles » y pointe vers bonpapa.ca, et celle de Startop n'est pas cliquable
# du tout. À signaler à MC ; ici les quatre liens sont les bons.
BALADOS = [
    ("assets/medias/elles.png", "Elles", "Elles, le balado",
     "https://open.spotify.com/episode/4ynHe3r4tA8xNjfH9uQl8t"),
    ("assets/medias/bon-papa.png", "Bon Papa", "Bon Papa, le balado",
     "https://open.spotify.com/episode/1yO1k2xmfmrY4YIrfvrihF"),
    ("assets/medias/startop.png", "Startop", "Startop, le balado",
     "https://open.spotify.com/episode/2Mm3four3badsBPEdOfte5"),
    ("assets/medias/umea.png", "UMEA", "UMEA, le balado",
     "https://open.spotify.com/episode/5Zk0mOxzvFU53o0ebnSfqs"),
]
# ✏️ David : cette ligne devient un TITRE. Elle annonçait les logos depuis
# dessous, ce qui la laissait flotter entre deux choses ; en tête, elle les
# rassemble et donne son nom à ce qui suit.
PRESSE = "Je porte le sujet dans les médias québécois"
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
# LA FICHE DE CONTACT
# ═════════════════════════════════════════════════════════════════════════════
#
# ✏️ David, 2026-08-28 : « est-ce qu'on peut ajouter un bouton Ajouter
# Marie-Claude à mes contacts ? »
#
# 🔴 C'est le geste que fait vraiment un planificateur après une conférence, et
# aucun formulaire ne le remplace. Un courriel se remet à demain ; un contact
# enregistré survit à la journée et remonte tout seul le jour où il cherche
# quelqu'un pour une date.
#
# 📄 Format vCard 3.0 et pas 4.0 : c'est le seul que lisent à la fois iOS,
# Android, Outlook et Google Contacts. Les fins de ligne sont en CRLF parce que
# la RFC 6350 l'impose et que certains lecteurs Android refusent le fichier sans.
#
# 🔴 La photo est aplatie sur le crème avant d'être encodée : le PNG d'origine est
# une feuille découpée sur fond transparent, et la transparence devient NOIRE en
# JPEG. Sept kilo-octets, ce qui garde la fiche sous les dix.

def vcard():
    """La fiche, prête à ouvrir dans les contacts."""
    photo = (RACINE / "assets" / "mc-photo-b64.txt").read_text().strip()
    lignes = [
        "BEGIN:VCARD", "VERSION:3.0",
        f"N:Viau;Marie-Claude;;;",
        f"FN:{MC['nom']}",
        "ORG:Momenta",
        # ✏️ David : « son titre doit être simplement Fondatrice de Momenta ».
        # 🔴 Une fiche de contact dit ce que quelqu'un EST, pas ce qu'il vend. Le
        # champ ORG porte déjà Momenta ; certains carnets d'adresses recollent les
        # deux et affichaient « Fondatrice · Conférencière et panéliste, Momenta ».
        "TITLE:Fondatrice de Momenta",
        f"EMAIL;type=INTERNET;type=WORK:{MC['courriel']}",
        f"TEL;type=CELL;type=VOICE:{MC['tel_lien']}",
        f"URL:{MC['site']}",
        # X-SOCIALPROFILE est la clé qu'iOS lit pour afficher un profil social
        # dans la fiche ; les autres lecteurs retombent sur l'URL qui suit.
        f"X-SOCIALPROFILE;type=linkedin:{MC['linkedin_perso']}",
        f"URL;type=LinkedIn:{MC['linkedin_perso']}",
        "ADR;type=WORK:;;;Bromont;Québec;;Canada",
        # ✏️ David, 2026-08-28 : la note s'en va. Elle décrivait son offre dans un
        # champ que les carnets d'adresses affichent en gros bloc de texte sous la
        # fiche, ce qui donne à un contact l'allure d'une annonce. Une fiche porte
        # des coordonnées ; ce qu'elle fait se lit sur la page, pas dans le carnet.
        f"PHOTO;ENCODING=b;TYPE=JPEG:{photo}",
        "END:VCARD",
    ]
    return "\r\n".join(lignes) + "\r\n"


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
  /* 🔄 L'affiche remonte à 26-42. Elle était descendue à 24-38 pour faire entrer
     « Momenta accompagne le moment que personne ne prépare » ; la formulation
     retenue est plus courte de huit signes et tient à toutes les tailles
     essayées, jusqu'à 46. On reprend donc la valeur qui donne son poids à
     l'affiche sans écraser le nom : l'écart reste de 6 px au plancher et 8 au
     plafond. */
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
/* 🐛 L'espace sous un titre appartient AU TITRE, jamais au voisin. Les h3 des
   cartes recevaient le leur du paragraphe qui suit (`.carte p{margin-top:8px}`),
   et « Avec qui je travaille », qui n'a pas ce voisin, se retrouvait collé à son
   texte : zéro pixel, mesuré. Un espacement qui dépend de ce qui suit se perd
   dès qu'on change ce qui suit. */
h2,h3{margin-bottom:8px}
h2{font-size:var(--t-titre)}
h3{font-size:var(--t-section)}
/* Un titre de bloc à l'intérieur d'une section a besoin d'air AU-DESSUS pour se
   détacher de ce qui précède. C'était un style en ligne dans le HTML. */
h3.bloc{margin-top:28px}
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
.contacts{display:flex; flex-wrap:wrap; align-items:center; gap:10px 22px; margin-top:24px}
.contacts a{
  display:inline-flex; align-items:center; gap:8px;
  padding:12px 20px; border-radius:25px; text-decoration:none;
  font-size:var(--t-corps); font-weight:600; border:2px solid transparent;
  transition:background-color 160ms ease-out, color 160ms ease-out;
}
.contacts .plein{background:var(--corail); color:var(--blanc)}
.contacts .plein:hover{background:#ff8a86}
/* ✏️ David : « enlève les contours blancs ». Ils faisaient quatre boutons de
   poids égal dans l'en-tête, donc quatre appels à l'action, donc aucun. Le
   courriel garde seul sa pastille corail ; les trois autres redeviennent ce
   qu'ils sont, des coordonnées qu'on consulte. Ils passent au gris chaud pour
   descendre d'un cran sans devenir illisibles : 11,3:1 sur le vert nuit. */
.contacts .vide{border-color:transparent; color:var(--gris); padding:12px 6px}
.contacts .vide:hover{color:var(--blanc)}
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
/* L'appui se cale sur le filet, sans le prolonger : il commente la phrase, il
   n'en fait pas partie. */
.apres-citation{padding-left:25px; margin-top:16px}
/* 🔄 Le saut n'est plus neutralisé sur téléphone. Il l'était quand il servait à
   couper une phrase trop longue : là où il tombait n'avait pas d'importance, et
   le supprimer évitait quatre lignes. Depuis que la phrase oppose deux
   propositions, le saut EST la phrase, et il tient à toutes les largeurs. */
/* 🔴 La signature a disparu avec l'appui : dès lors que la page entière est
   écrite au « je », elle est signée de bout en bout et une attribution sous la
   citation redirait le nom qui est déjà dans l'en-tête. */

/* ═══ Les cartes ══════════════════════════════════════════════════════════ */
.trois{display:grid; gap:12px; grid-template-columns:1fr; margin:16px 0}
@media(min-width:760px){.trois{grid-template-columns:repeat(3,1fr)}}
.carte{background:var(--blanc); border-radius:var(--rayon); padding:20px}
.carte h3{color:var(--corail); line-height:1.3}
.carte p{font-size:var(--t-corps); color:var(--vert2); margin:0}

/* ═══ Les jalons ══════════════════════════════════════════════════════════ */
.jalons{display:flex; flex-wrap:wrap; gap:24px; margin:4px 0 16px}
.jalon .n{font-size:var(--t-nom); font-weight:700; color:var(--corail); line-height:1}
.jalon p{margin:4px 0 0; color:var(--vert2); max-width:225px}

/* ═══ Les chiffres ════════════════════════════════════════════════════════
   Un chiffre n'est PAS un jalon, même s'il lui ressemble : le jalon dit qui
   elle est et se lit d'un coup, le chiffre traîne une source qu'il faut pouvoir
   vérifier. Deux rôles, deux classes, et la même valeur de `--t-nom` pour le
   nombre lui-même parce que c'est le même geste de lecture.

   🔴 Sans carte, contrairement aux demandes qui suivent juste en dessous. Deux
   rangées de trois rectangles blancs à la file se liraient comme une seule et
   la page perdrait son rythme. Ici le corail des nombres suffit à poser le
   bloc sur le crème. */
.chiffres{display:grid; gap:24px; grid-template-columns:1fr; margin:18px 0 0}
@media(min-width:760px){.chiffres{grid-template-columns:repeat(3,1fr); gap:32px}}
.chiffre .n{font-size:var(--t-nom); font-weight:700; color:var(--corail); line-height:1}
.chiffre p{margin:6px 0 0; color:var(--vert2)}
.chiffre .source{margin-top:8px}

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
/* Un logo cliquable doit se donner comme cliquable. L'opacité au repos les
   rassemble en une rangée calme ; le survol détache celui qu'on vise. */
.logos a{display:block; opacity:.82; transition:opacity 160ms ease-out}
.logos a:hover{opacity:1}
.logos a:focus-visible,.pochette a:focus-visible{
  outline:3px solid var(--corail); outline-offset:4px; border-radius:6px}
.pochette a{text-decoration:none; display:block}
.pochette a:hover img{opacity:.85}
.pochette img{transition:opacity 160ms ease-out}
.logos img{height:34px; width:auto; display:block}
.logos img[width="102"]{height:52px}
.logos img[width="472"]{height:40px}
@media(max-width:520px){
  .logos{gap:22px 26px} .logos img{height:27px}
  .logos img[width="102"]{height:42px}
  .logos img[width="472"]{height:33px}
}
/* ═══ Les balados ═════════════════════════════════════════════════════════
   Des pochettes, pas des logos : elles portent des visages et de la couleur, et
   se mettraient à crier si elles montaient à la hauteur des mots-symboles de
   presse. Elles se posent donc en vignettes carrées sous eux, avec leur nom
   dessous, parce qu'une pochette de balado ne se reconnaît pas à 72 px. */
.pochettes{display:flex; flex-wrap:wrap; gap:18px; margin:24px 0 16px}
.pochette{margin:0; width:80px}
.pochette img{width:72px; height:72px; border-radius:var(--rayon); display:block}
.pochette figcaption{font-size:var(--t-source); color:var(--vert2);
  margin-top:8px; line-height:1.3}

/* ═══ L'appel, la dernière chose qu'on lit ════════════════════════════════ */
.appel{background:var(--vert); color:var(--blanc)}
.appel h2{color:var(--blanc)}
.appel .phrase{margin-bottom:12px}
.appel .doux{color:var(--gris)}
.appel .source{color:var(--gris)}

/* Le pied ne porte plus qu'un logo, centré. Il prolonge le vert nuit de l'appel
   sans filet entre les deux : la page se termine sur un aplat, pas sur une
   dernière rangée d'informations. */
/* ✏️ David, 2026-08-28 : « on va rapetisser beaucoup le logo en pied de page ».
   🔴 Il passe de 24 à 15 px, presque de moitié. À cette taille il ne se lit plus
   comme un titre mais comme une signature, ce qu'il est : le pied ne dit plus
   rien depuis qu'on en a retiré les coordonnées, il ferme. Le logo de l'en-tête
   reste à 26 px, et l'écart entre les deux dit lequel des deux compte. */
footer{background:var(--vert); padding:32px 0 34px}
footer .logo{height:15px; display:block; margin:0 auto}

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
    # 🐛 David : « l'icône avec la personne et le plus est curieuse, on voit très
    # mal le + ». Vrai : à 17 px, un petit plus collé à une silhouette devient une
    # tache. Remplacé par un carnet d'adresses, qui se lit à sa SILHOUETTE et non
    # à un détail — un rectangle avec un onglet, reconnaissable même flou.
    "contact": 'M20 2H8a2 2 0 00-2 2v3H4v2h2v3H4v2h2v3H4v2h2v3a2 2 0 002 2h12a2 2 0 '
               '002-2V4a2 2 0 00-2-2zm-6 4.5a2.5 2.5 0 110 5 2.5 2.5 0 010-5zM19 18H9v-1.1'
               'c0-2 4-3.1 5-3.1s5 1.1 5 3.1V18z',
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
    chiffres = "".join(
        f'<div class="chiffre"><div class="n">{e(n)}</div><p>{e(t)}</p>'
        f'<p class="source">{e(src)}</p></div>'
        for n, t, src in CHIFFRES)
    logos = "".join(
        f'<a href="{url}" target="_blank" rel="noopener" aria-label="{e(alt)}, lire l\'article">'
        f'<img src="{src}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy"></a>'
        for src, alt, w, h, url in MEDIAS)
    pochettes = "".join(
        f'<figure class="pochette"><a href="{url}" target="_blank" rel="noopener" '
        f'aria-label="{e(complet)}, écouter l\'épisode">'
        f'<img src="{src}" alt="{e(complet)}" width="144" height="144" loading="lazy">'
        f'<figcaption>{e(court)}</figcaption></a></figure>'
        for src, court, complet, url in BALADOS)

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
        <!-- 🔴 `download` force l'enregistrement plutôt que l'affichage. Sur iOS
             le fichier s'ouvre dans l'aperçu de contact avec « Ajouter aux
             contacts » ; sur Android il se télécharge puis s'ouvre pareil. -->
        <a href="marie-claude-viau.vcf" download class="vide"><svg viewBox="0 0 24 24"><path d="{ICONES['contact']}"/></svg>Ajouter à mes contacts</a>
        {lien(MC['site'], "momentareseau.com", "web")}
      </div>
    </div>
    <img class="portrait" src="assets/mc-feuille.png"
         alt="Portrait de {e(MC['nom'])}" width="760" height="760">
  </div>
</div></header>

<section><div class="dedans">
  <p class="phrase citation">{e(ACCROCHE['phrase'])}</p>
  <p class="doux apres-citation">{e(ACCROCHE['appui'])}</p>
</div></section>

<section><div class="dedans">
  <h2>Ce que vous pouvez me demander</h2>
  <p class="doux">{e(SUJETS)}</p>
  <div class="trois">{demandes}</div>
</div></section>

<!-- ✏️ David, 2026-08-28 : les chiffres passent en troisième, après la demande.
     🔴 Ils étaient entre l'accroche et la demande, où ils retardaient la seule
     chose que la page a à offrir. L'ordre qui tient : elle affirme, elle dit ce
     qu'on peut lui demander, PUIS elle donne de quoi le défendre. Un
     planificateur convaincu par la phrase veut savoir ce qu'il peut réserver
     avant de savoir pourquoi le sujet compte ; les chiffres, il ne s'en sert
     qu'après, devant son comité.
     🔴 Ils restent AVANT « D'où je parle » : ils prouvent que le sujet est
     légitime, pas qu'elle l'est. Les deux blocs ne répondent pas à la même
     question et les fondre les affaiblirait tous les deux. -->
<section><div class="dedans">
  <h2>{e(CHIFFRES_TITRE)}</h2>
  <p class="doux">{e(CHIFFRES_INTRO)}</p>
  <div class="chiffres">{chiffres}</div>
</div></section>

<section><div class="dedans">
  <h2>D’où je parle</h2>
  <div class="jalons">{jalons}</div>
  <p class="doux">{e(PARCOURS)}</p>
  <p class="doux">{e(CERTIFICATION)}</p>
  <h3 class="bloc">{e(PRESSE)}</h3>
  <div class="logos">{logos}</div>
  <div class="pochettes">{pochettes}</div>
  <p class="doux">{e(PRIX)}</p>
  <h3 class="bloc">Avec qui je travaille</h3>
  <p class="doux">Le parcours que j’ai bâti est animé par des sommités
     québécoises. Elles interviennent aussi en entreprise.</p>
  <div class="gens">{gens}</div>
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

<!-- ✏️ David : « le call to action et le pied de page sont fusionnés en ce moment.
     On enlève la section du bas, on met un petit logo Momenta centré en bas
     complètement. »

     🔴 Deux blocs vert nuit qui se suivent lisaient comme un seul, et le second
     répétait des coordonnées déjà données deux fois : dans l'en-tête et dans le
     bouton juste au-dessus. Une page qui redit ses coordonnées trois fois n'en
     donne aucune, elle donne une liste.

     Le pied ne porte plus qu'une signature de marque. Il n'a plus de titre, plus
     de lien, rien à lire : il ferme. -->
<footer><div class="dedans">
  <img class="logo" src="assets/logo-light.png" alt="Momenta">
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
    fiche = RACINE / "marie-claude-viau.vcf"
    fiche.write_text(vcard(), encoding="utf-8")
    lisible = re.sub(r"<[^>]+>", " ", re.sub(r"<style[^>]*>.*?</style>", " ", page, flags=re.S))
    mots = len(lisible.split())
    print(f"écrit : {SORTIE}")
    print(f"  {len(page)} octets · {mots} mots · {page.count('<section')+1} blocs")
    print(f"  fiche de contact : {fiche.name}, {len(fiche.read_text())//1024} ko")
    print(f"  {len(INTERDITS)} interdits vérifiés · échelle à six crans · plancher 15 px")
