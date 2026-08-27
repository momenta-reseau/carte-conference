#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""contenu.py — tout le texte et tous les chiffres de la carte, isolés du gabarit.

🔴 CHAQUE CHIFFRE PORTE SA SOURCE. La table de traçabilité de
`Ce-que-je-vends/Marketing/Trousse-financement-employeur.md` fait autorité, et rien
n'entre ici sans y figurer.

⛔ CE QUI NE PEUT JAMAIS ENTRER, le dépôt étant PUBLIC :
   · les outcomes du site (20-40 % moins de départs, +53 % d'intention de rester,
     87 % valorisées, 67 % santé mentale, 100 % recommandent) — provenance non
     documentée, Signal-012 ouvert. Un employeur qui challenge les ferait tomber.
   · Rio Tinto, Desjardins, CGI, Beneva comme clientes — ce sont des GRATUITÉS.
   · le nom d'une participante, quel qu'il soit.
   · les données du sondage Jeune Chambre / Léger — entente de confidentialité.
   · « le départ d'une employée » : MC dit « le remplacement d'une employée qui
     ne revient pas », et c'est une règle, pas une préférence.
"""

# ── À qui on s'adresse ───────────────────────────────────────────────────────
# Un acheteur de conférence ou de formation qui vient de voir MC parler douze
# minutes. Il veut trois choses, dans cet ordre : la rejoindre, retrouver ce
# qu'elle a dit, savoir ce qu'elle vend. La page suit cet ordre.

MC = {
    "nom": "Marie-Claude Viau",
    "role": "Fondatrice de Momenta · Conférencière",
    "courriel": "mcviau@momentareseau.com",
    "telephone": "514 889-9649",
    "telephone_lien": "+15148899649",
    "linkedin": "https://www.linkedin.com/company/momentareseau",
    "site": "https://www.momentareseau.com",
    "ville": "Bromont, Québec",
}

# ✏️ David, 2026-08-27 : « la première citation parle de l'État et c'est pas la
# plus punchy ». Remplacee par le titre de la LETTRE OUVERTE de MC dans le Journal
# de Montreal, 8 mars 2026 (📄 Presences-medias.md). Trois raisons de preferer
# celle-la : elle est d'elle, elle a deja ete testee sur un large public
# (170 000 vues en 48 h), et « nous coute des talents » est la langue de
# l'acheteur. La phrase sur l'Etat n'est pas perdue : elle ferme la carte, comme
# elle ferme le talk.
TAKE_HOME = {
    "phrase": "Le silence sur le post-partum<br>nous coûte des talents.",
    "appui": "Pas le congé. L’atterrissage. Le moment qui casse une carrière n’est pas "
             "le départ, ce sont les douze à dix-huit mois qui suivent le retour.",
    "source": "Lettre ouverte de Marie-Claude Viau, Journal de Montréal, 8 mars 2026. "
              "Thèse portée au panel de l’Ordre des CRHA, juin 2026",
}

# La phrase qui ferme la carte, comme elle ferme la conference.
FERMETURE = {
    "phrase": "L’État mesure si je reviens.<br>Personne ne mesure si je reste.",
    "appui": "88 % des mères canadiennes reviennent au travail après leur congé. "
             "Le retour n’est pas l’enjeu. C’est ce qui se passe dans les mois qui suivent.",
    "source": "Statistique Canada, Enquête sur la couverture de l’assurance-emploi",
}

CONFERENCE = {
    "titre": "Le retour au travail",
    "chapeau": "Une conférence sur la transition parentale, racontée par quelqu’un "
               "qui l’a traversée avant de bâtir ce qui lui a manqué.",
    "points": [
        "Ce que vivent les femmes dans les mois qui suivent le retour, "
        "et pourquoi personne ne le mesure.",
        "Pourquoi ce n’est plus une question de bien faire, mais de rétention.",
        "Ce que la recherche prouve, et ce qu’elle ne prouve pas encore.",
    ],
    # 🟡 Les formats et le cachet ne sont documentés NULLE PART dans le wiki.
    # On ne les invente pas. « Sur demande » est la seule chose vraie.
    "formats": "Formats et disponibilités sur demande.",
}

# ── Les chiffres de la présentation, réutilisables à l'interne ───────────────
CHIFFRES = [
    {"n": "88 %", "t": "des mères canadiennes reviennent au travail après leur congé parental",
     "src": "Statistique Canada"},
    {"n": "33 %", "t": "perdent confiance en leurs capacités professionnelles au retour",
     "src": "Benefits Canada, 1 000 femmes"},
    {"n": "30 000 $", "t": "le coût moyen du remplacement d’une employée qui ne revient pas, "
                           "et plus de 100 000 $ pour 15 % des employeurs",
     "src": "Randstad Canada, 2024"},
    {"n": "0", "t": "étude canadienne qui mesure si elles sont encore là douze mois "
                    "après le retour",
     "src": "RQAP et Statistique Canada mesurent le retour, personne ne mesure le maintien",
     "fort": True},
]

RESULTATS = {
    "intro": "Cohorte du printemps 2026. Sondage de fin de parcours auprès de 22 des "
             "42 participantes, avant et après.",
    "lignes": [
        ("Sentiment d’être soutenue", "4,3", "8,1", True),
        ("Posture de leadership en transition", "5,0", "7,6", False),
        ("Clarté sur la prochaine étape professionnelle", "4,9", "7,3", False),
        ("Charge mentale et équilibre", "4,6", "7,1", False),
        ("Confiance en sa valeur professionnelle", "6,6", "8,2", False),
    ],
    "appuis": [
        ("73", "Net Promoter Score"),
        ("91 %", "estiment que leur organisation bénéficierait du programme"),
        ("78 %", "des participantes géraient une équipe ou des projets"),
    ],
    "note": "Auto-évaluation sur 10. n = 22 sur 42.",
}

# ── La preuve de scène, relevée dans Presences-medias.md ────────────────────
PRESSE = {
    "intro": "Marie-Claude porte le sujet dans les médias québécois depuis 2026.",
    "grands": ["Radio-Canada", "LCN", "Noovo Info", "TVA Nouvelles",
               "Journal de Montréal", "La Voix de l’Est", "M105", "107.7 Estrie"],
    "scenes": [
        ("Panel de l’Ordre des CRHA", "SST, Loi 27 et risques psychosociaux · juin 2026"),
        ("Journée immersive Momenta", "Première édition, Bromont · juin 2026"),
        ("Six webinaires publics", "Série gratuite avec personnalités invitées"),
    ],
    "balados": ["Elles, le balado", "Bon Papa", "Startop", "UMEA"],
    "portee": "Sa lettre ouverte du 8 mars 2026 a été vue 170 000 fois et partagée "
              "230 fois en 48 heures.",
    "prix": "Prix coup de cœur au Défi OSEntreprendre 2026, volet régional "
            "Haute-Yamaska et Brome-Missisquoi",
}

# ── L'offre, pour l'acheteur qui est aussi RH ───────────────────────────────
OFFRE = {
    "citation": "La conformité sans accompagnement, c’est du papier.",
    "citation_source": "Marie-Claude Viau, panel de l’Ordre des CRHA sur la Loi 27",
    "intro": "Au-delà de la conférence, Momenta accompagne la transition parentale "
             "dans les organisations.",
    "items": [
        ("Le parcours Essentielle",
         "Cinq mois de développement du leadership, en cohorte, animé par des sommités "
         "québécoises. Deux heures aux deux semaines, sur l’heure du dîner, séances "
         "enregistrées.",
         "1 495 $ · reconnu par l’Ordre des CRHA pour 14 heures de formation continue, "
         "donc admissible au budget de formation et à la loi du 1 %"),
        ("Pour les organisations",
         "Le même parcours offert aux employées, avec un volet pour les gestionnaires "
         "qui reçoivent quelqu’un au retour.",
         "Sur mesure"),
        ("La Journée immersive",
         "Une journée en présentiel : ateliers, conférences, réseautage, plein air.",
         "Deuxième édition · 6 novembre 2026 · Bromont"),
        ("Formation en entreprise et accompagnement individuel",
         "Ateliers pour les équipes de gestion, et du un pour un quand la cohorte "
         "ne suffit pas.",
         "Sur demande"),
    ],
}

HONNETETE = (
    "Ce qu’on ne peut pas prouver encore : qu’un accompagnement retient les femmes. "
    "Aucune étude avec groupe témoin n’existe, ni au Québec ni au Canada. "
    "Ce qui est mesuré, c’est que la pénalité existe et que la plupart des femmes "
    "traversent ce moment sans aucun soutien formel."
)
