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
    # ✏️ David, 2026-08-27 : « le côté panéliste est important ».
    # 🔴 Ce n'est pas un synonyme de conférencière, c'est une AUTRE case dans une
    # programmation, avec un autre budget et un autre risque. Un planificateur
    # dont la plénière est déjà bookée peut encore la prendre en table ronde, et
    # celui qui hésite à confier 45 minutes à quelqu'un qu'il ne connaît pas la
    # teste en panel. Le mot doit donc être lisible dès l'en-tête.
    "role": "Fondatrice de Momenta · Conférencière et panéliste",
    "courriel": "mcviau@momentareseau.com",
    "telephone": "514 889-9649",
    "telephone_lien": "+15148899649",
    "linkedin": "https://www.linkedin.com/company/momentareseau",
    "site": "https://www.momentareseau.com",
    "ville": "Bromont, Québec",
}

# ✏️ David, 2026-08-27 : l'accroche « nous coûte des talents » doit être
# remplacée par « quelque chose de plus senti et proche de la mission ».
#
# 🔴 C'est la bonne correction, et pour une raison que j'avais ratée : « nous
# coûte des talents » est la langue d'un acheteur RH. Or la salle est faite de
# PLANIFICATEURS D'ÉVÉNEMENTS. Eux n'achètent pas un argument de rétention, ils
# achètent quelqu'un qui va tenir leur salle. La promesse d'une fondatrice à la
# première personne leur parle mieux qu'un calcul de talents.
#
# 📄 La phrase est confirmée à TROIS endroits du wiki : le post de lancement de
# cohorte (avril 2026), Experts-Modules-FINAL, et l'offre ASCENSION v2 pour
# cabinets. C'est une phrase établie, pas une trouvaille.
#
# 📄 Et elle dit la mission, telle que Mission-positionnement.md la porte :
# transformer ce moment charnière en levier de leadership. Sauf qu'elle la dit
# par le manque plutôt que par l'objectif, ce qui est exactement ce qu'on
# cherchait.
TAKE_HOME = {
    # 🐛 L'espace AVANT le <br> n'est pas décoratif. Le saut est neutralisé sous
    # 640 px, et sans cet espace les deux moitiés se collaient : « voulu
    # trouverlors de ma propre ». Un navigateur ignore une espace en fin de ligne
    # quand le saut s'affiche, et s'en sert quand il ne s'affiche pas.
    "phrase": "Je bâtis ce que j’aurais voulu trouver <br>"
              "lors de ma propre transition parentale.",
    "appui": "Ce que je cherchais, ce n’était pas un soin. C’était un réseau. "
             "Sentir que je n’étais pas la seule.",
    "source": "Marie-Claude Viau, fondatrice de Momenta",
}

# ── Qui parle ────────────────────────────────────────────────────────────────
#
# ✏️ David, 2026-08-27, rapportant MC : « ça fait 15 ans que je suis dans le
# milieu des conférences, 10 ans dans le milieu de la formation dont 10 à
# l'Institut de Leadership où j'ai cofondé le programme Femmes Leaders. Ça fait
# 20 ans que je suis dans le milieu des affaires. » Et la consigne : « on veut
# faire comprendre aux acheteurs que MC est une figure crédible dans le domaine
# de la transition parentale. Sans surcharger la page. »
#
# 🔴 Ce que la carte n'avait pas du tout : une raison de la croire. Elle disait
# où MC avait parlé et ce qu'elle raconte, jamais ce qui la rend légitime sur ce
# sujet-là. Un acheteur qui hésite entre deux conférencières tranche là-dessus.
#
# 🔴 LE POINT LE PLUS FORT EST LA CERTIFICATION, et il ne figurait nulle part.
# Sans elle, MC est une femme qui raconte ce qui lui est arrivé, ce qui est
# émouvant et remplaçable. Avec elle, elle a traversé la transition ET elle en
# connaît la littérature. C'est ce qui sépare le témoignage de l'expertise, et
# c'est exactement ce qu'un acheteur cherche à savoir.
#
# 🟡 « 15 ans en conférence » n'a AUCUNE trace dans le wiki. Source unique : ce
# message de David rapportant MC, le 2026-08-27. À confirmer avec elle.
#
# ⚠️ Écart connu et assumé : la page « À propos » du site public dit « depuis
# neuf ans » là où MC dit dix. Le message de David est la source la plus récente
# et la plus directe. À aligner sur le site, ou à corriger ici.
#
# ⛔ Ce qui n'entre PAS ici : le nom du conférencier avec qui MC a travaillé.
# Elle est d'accord pour en parler, elle n'y voit « pas de plus-value » pour le
# moment. Une carte publique n'est pas l'endroit d'un nom qu'on n'a pas tranché.
QUI_PARLE = {
    "jalons": [
        ("20 ans", "dans le milieu des affaires"),
        ("15 ans", "dans le milieu de la conférence"),
        ("10 ans", "à former des femmes en leadership"),
    ],
    # 🐛 « la transition parentale, que personne n'outille » redisait la phrase de
    # fermeture, qui le dit mieux et sans le nommer. Ne reste que le fait : d'où
    # elle tient ce qu'elle sait.
    "parcours": "À l’Institut de Leadership, Marie-Claude Viau a cofondé le programme "
                "Femmes Leaders. Dix ans à écouter des femmes parler d’ambition en "
                "salle et de charge mentale aux pauses.",
    # 🐛 La phrase finissait par « elle a traversé cette transition et elle en
    # connaît la littérature », qui redisait l'accroche de la page (elle l'a
    # traversée) et commentait le fait au lieu de le laisser porter.
    "certification": "Elle est certifiée en transition parentale par le Center for "
                     "Parental Leave Leadership, l’organisme américain fondé par "
                     "Amy Beacom (Ph. D.).",
    "engagements": "Momenta est liée à la Fondation Mères avec Pouvoir, qui soutient "
                   "les cheffes de famille monoparentale à faible revenu ayant de jeunes "
                   "enfants. Marie-Claude est impliquée dans le Bromont Ultra, un "
                   "événement philanthropique annuel.",
    "source": "Institut de Leadership, Center for Parental Leave Leadership, "
              "momentareseau.com",
}


# ── Ce qu'on peut lui demander ───────────────────────────────────────────────
#
# ✏️ MC elle-meme, memo vocal du 2026-08-27, transmis par David :
#   « Je veux pas vendre de conference. C'est pas dans mon carre de sable. Si je
#     vends ca, je sors de mon carre de sable puis je vais perdre de l'energie. »
#   « Par contre, dans mon parcours, j'ai des formatrices telles que Sonia
#     Lupien... Ca je pourrais l'annoncer, fait que la ils vont voir : OK, elle a
#     une credibilite waouh, elle travaille avec des tops. »
#   « Apres ca je fais une conference d'inspiration, c'est ca que je vois vendre
#     pour l'annee. Sinon je vends de la formation sur mesure sur differents
#     themes qui touchent la conciliation travail-famille. »
#
# 🔴 CE QUI TOMBE : le catalogue de trois conferences. Il vendait exactement ce
# qu'elle refuse de vendre. Un catalogue dit « choisissez un produit » ; elle veut
# qu'on l'appelle. Et trois titres de conference sur une page font d'elle une
# fournisseuse de conferences, ce qu'elle n'est pas et ne veut pas devenir.
#
# 🔴 CE QUI ENTRE, ET C'EST SON IDEE : les formatrices. « Sonia Lupien dans ton
# parcours, est-ce que vous la vendez ? » est exactement l'appel qu'on cherche a
# provoquer. Une page qui nomme des sommites fait plus pour sa credibilite que
# n'importe quelle phrase qu'elle ecrirait sur elle-meme.
#
# ⛔ AUCUN TITRE D'ATELIER SUR LA PAGE, et c'est une decision, pas un oubli.
# CLAUDE.md §0 : la fiche de la formatrice fait autorite sur le titre, « tout
# autre fichier qui ecrit un titre d'atelier est une copie, donc suspect ». Or le
# site public et les fiches divergent sur SIX titres sur six (le site publie des
# libelles de theme, les fiches portent les titres d'atelier). Publier l'un ou
# l'autre, c'est publier un des deux camps d'un conflit ouvert. Les NOMS et les
# TITRES PROFESSIONNELS, eux, concordent partout, et c'est eux qui portent la
# credibilite que MC cherche.
#
# 📄 Les six sont deja nommees publiquement sur momentareseau.com avec ces titres
# exacts. Rien de neuf n'est expose ici.
#
# 🟡 Dans le memo, MC nomme aussi « Laris », que la transcription vocale n'a pas
# rendu et qu'aucune fiche du wiki ne permet d'identifier. Non repris. À lui
# demander si elle voulait ajouter quelqu'un qui n'est pas dans les six.
DEMANDES = [
    ("Une conférence d’inspiration",
     "Son récit, seule sur scène. Le format qu’elle porte elle-même, en ouverture "
     "ou en clôture de journée."),
    ("Une place en panel",
     "Une position tenue en réaction, sans support et sans minutage à elle."),
    ("De la formation sur mesure en entreprise",
     "Sur la conciliation travail-famille, ajustée aux thèmes que vous voulez "
     "travailler avec vos équipes."),
]

FORMATRICES = {
    "intro": "Le parcours Momenta est animé par des sommités québécoises. "
             "Elles interviennent aussi en entreprise.",
    # 🔴 Chaque titre porte le mot qui fait RECONNAITRE la personne, pas celui qui
    # la decrit le mieux. « Neuroscientifique du stress » est exact et anonyme ;
    # « directrice du Centre d'etudes sur le stress humain, autrice de Par amour
    # du stress » se reconnait. C'est ce que MC demande : « ils vont voir qu'elle
    # travaille avec des tops ». Un planificateur ne verifie pas un CV, il
    # reconnait un nom ou il ne le reconnait pas.
    #
    # 📄 Sources, une par ligne : fiche `Formatrices/Sonia-Lupien.md` (CESH,
    # Universite de Montreal, « Par amour du stress ») · site loryzephyr.com et
    # Editions de l'Homme (quatre ouvrages, balado « Ca va maman ? ») · fiche
    # `Marylise-Champagne.md` (Dix mille matins) · fiche `Mylene-Houle-Morency.md`
    # (tagline du tableur Intervenantes) · momentareseau.com pour les deux
    # dernieres, qui les nomme deja avec ces titres exacts.
    "liste": [
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
    ],
    "source": "momentareseau.com, parcours Essentielle",
}

# ── L'appel ──────────────────────────────────────────────────────────────────
#
# ✏️ David, 2026-08-27 : « ce qu'on veut c'est générer un appel et une demande.
# Pas booker tout de suite la vente. »
#
# 🔴 D'ou une demande qui ne coute rien a accepter. « Reservez une date » exige
# un budget, un comite et un contrat ; « dites-nous ce que vous programmez »
# n'exige qu'un courriel. Le second se fait le jour meme, le premier jamais.
#
# 🔴 Et il n'y a PAS de prix sur la page. Un tarif transforme la conversation en
# comparaison avant meme qu'elle commence, et il ferme la porte a l'acheteur dont
# le budget est ailleurs mais qui aurait pris un panel.
APPEL = {
    "titre": "Une date, une programmation, une idée ?",
    "texte": "Dites à Marie-Claude ce que vous organisez et ce que vous cherchez à "
             "faire vivre à votre salle. Elle répond elle-même.",
}

# La phrase qui ferme la carte, comme elle ferme la conference.
FERMETURE = {
    "phrase": "L’État mesure si je reviens.<br>Personne ne mesure si je reste.",
    # 🐛 « Le retour n'est pas l'enjeu, c'est ce qui se passe dans les mois qui
    # suivent » paraphrasait la phrase juste au-dessus. Le chiffre suffit : c'est
    # lui qui rend la phrase vraie, pas une glose.
    "appui": "88 % des mères canadiennes reviennent au travail après leur congé.",
    "source": "Statistique Canada, Enquête sur la couverture de l’assurance-emploi",
}

# ── Les trois conferences ────────────────────────────────────────────────────
#
# 🔴 Un planificateur ne booke pas un sujet, il remplit une CASE dans une
# programmation. Sans catalogue, il repart emu et incapable de dire a son comite
# quoi lui acheter. Les trois ci-dessous ne se chevauchent pas et couvrent les
# quatre milieux que le salon nomme : corporatif, associatif, municipal,
# tourisme d'affaires.
#
# 🔴 Les trois registres sont MESURES comme opposes (MacKrill, n = 1 866) :
# « inspiring » va avec le « je », « informative » va contre. Ce sont donc trois
# produits distincts, jamais trois parties d'une meme conference.
#
# 🟡 Les durees et les formats ne sont documentes NULLE PART. « Sur demande »
# est la seule chose vraie tant que MC ne les a pas fixes.

# ── Deux sujets, deux formats ────────────────────────────────────────────────
#
# ✏️ David, 2026-08-27 : « mets l'accent sur le fait que MC peut être une
# conférencière ET/OU une panéliste pour parler de transition parentale et
# d'accomplissement », puis « le côté panéliste est important ».
#
# 🔴 Ce qui manquait : la carte vendait un SUJET et un seul FORMAT. Or un
# planificateur raisonne en cases de programmation, et il en a plusieurs :
# la plénière, la table ronde, l'atelier. Nommer les deux formats double le
# nombre de cases où MC peut entrer sans rien changer à son propos.
#
# 🔴 Le panel n'est pas une conférence au rabais. Il demande l'inverse : tenir
# une position en réaction, sans support, sans minutage à soi, avec le risque
# d'un contradicteur. Un acheteur ne le confie pas à quelqu'un qui n'a fait que
# lire un texte. La preuve documentée existe (Ordre des CRHA, juin 2026), et la
# citation la plus tranchée de toute la page en vient. C'est le meilleur
# argument possible et il ne coûte rien à écrire.
#
# 🔴 « Accomplissement » ouvre un second marché. Le récit de la course et de
# l'ultramarathon se programme dans un gala, un congrès municipal ou un
# lancement d'année où la parentalité n'est le sujet de personne. Sans cette
# ligne, l'acheteur classe MC dans « parentalité » et ne la rappelle jamais
# pour autre chose.
FORMATS = {
    "sujets": [
        ("La transition parentale",
         "Ce qui casse dans les mois qui suivent le retour, pourquoi personne ne "
         "le mesure, et ce que la Loi 27 en fait une obligation."),
        ("L’accomplissement",
         "La remontée par la course, de trois kilomètres à l’ultramarathon. Ce que "
         "ça prend, ce que ça coûte, et pourquoi ça se programme aussi devant une "
         "salle qui n’a rien à voir avec la parentalité."),
    ],
    "panel": {
        "titre": "En panel ou en table ronde",
        # 🐛 Ce bloc répétait mot pour mot la carte « Une place en panel » posée
        # juste au-dessus. Il ne garde que ce qu'il est seul à apporter : la preuve
        # qu'elle l'a déjà fait, devant un auditoire exigeant.
        "texte": "En juin 2026, elle a siégé au panel de l’Ordre des CRHA sur la "
                 "Loi 27 et les risques psychosociaux, devant un auditoire de "
                 "professionnels agréés.",
        "citation": "La conformité sans accompagnement, c’est du papier.",
        "source": "Marie-Claude Viau, panel de l’Ordre des CRHA sur la Loi 27",
    },
}

THEMES = [
    {
        "titre": "Je me suis sauvée avant de sauver quoi que ce soit",
        "case": "Ouverture ou clôture de journée",
        "pour": "Galas, congrès, colloques municipaux, tourisme d’affaires. "
                "Salle mixte, aucun prérequis.",
        "quoi": "Le récit complet : le postpartum non diagnostiqué, la remontée par "
                "la course, l’ultramarathon, et ce qu’il a fallu abandonner pour "
                "fonder Momenta. Une histoire qui ne se referme pas sur une morale.",
    },
    {
        "titre": "Pas le congé. L’atterrissage.",
        "case": "Bloc thématique ou panel",
        "pour": "Congrès RH, ordres professionnels, associations sectorielles, "
                "comités de santé et sécurité.",
        "quoi": "Le moment qui casse une carrière n’est pas le départ, ce sont les "
                "douze à dix-huit mois qui suivent le retour. La Loi 27 en fait une "
                "obligation légale. Thèse déjà portée devant l’Ordre des CRHA.",
    },
    {
        "titre": "L’ambition n’a pas disparu. Elle a changé de forme.",
        "case": "Conférence ou atelier",
        "pour": "Réseaux de femmes en affaires, semaines thématiques municipales, "
                "comités d’égalité, événements corporatifs féminins.",
        "quoi": "Dix ans à former des femmes en leadership, à les entendre parler "
                "d’ambition en salle et de charge mentale aux pauses. Ce que la "
                "transition parentale déplace, et ce qu’elle ne détruit pas.",
    },
]

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
    "formats": "Durées, formats et disponibilités sur demande.",
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
    # ✏️ David, 2026-08-27 : « les bons logos des bonnes organisations, pas une
    # liste exhaustive, mais tout ce que ça prend pour prouver la crédibilité ».
    #
    # 🔴 Les logos ne sont NULLE PART chez Momenta : ni sur /medias, qui ne porte
    # que des vignettes de vidéos et des pochettes de balados, ni dans le Package
    # Média du Drive. La case « Intégrer logos médias dans le pitch B2B » de
    # Presences-medias.md n'a jamais été cochée. Ils viennent donc de Wikimedia
    # Commons, tous trois en domaine public, et tous trois des MARQUES DÉPOSÉES
    # de leurs propriétaires : on les cite comme un fait, jamais comme un
    # partenariat ou un appui.
    #
    # 🟡 Trois seulement, et ce sont les trois grandes salles de nouvelles du
    # Québec. La Voix de l'Est, M105 et 107,7 Estrie sortent : devant un
    # planificateur de Montréal, le régional dilue plus qu'il n'ajoute. LCN, le
    # Journal de Montréal et OSEntreprendre n'ont pas de logo libre ; ils restent
    # en toutes lettres juste en dessous, ce qui les sert aussi bien.
    "logos": [
        ("assets/medias/radio-canada.png", "Radio-Canada", 584, 102),
        ("assets/medias/tva-nouvelles.png", "TVA Nouvelles", 341, 102),
        ("assets/medias/noovo-info.png", "Noovo Info", 102, 102),
    ],
    "sans_logo": "Reportage de fond à Radio-Canada, entrevues à LCN et à Noovo Info, "
                 "et une lettre ouverte signée dans le Journal de Montréal.",
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
         # 🐛 La carte affichait 1 495 $, le tarif de LISTE. Le site en production
         # affiche 1 395 $ en paiement unique depuis le 2026-08-02, ce qui tranche
         # D-016 et ses quatre valeurs contradictoires. Un acheteur qui compare la
         # carte au site aurait vu deux prix.
         "1 395 $ en paiement unique, ou 5 versements de 299 $ · reconnu par l’Ordre "
         "des CRHA pour 14 heures de formation continue, donc admissible au budget "
         "de formation et à la loi du 1 %"),
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
