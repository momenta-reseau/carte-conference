#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build.py — assemble index.html, la carte de conférencière de Marie-Claude Viau.

    python3 build.py

Même patron que le site du condo : un script, un fichier de contenu, une page.
Aucune dépendance, aucun cadriciel, aucun appel réseau au chargement sauf la
police depuis Google Fonts.

Ce que la page doit faire, dans cet ordre, pour un acheteur de conférence qui
vient de la voir parler douze minutes :
  1. la rejoindre en un geste
  2. retrouver ce qu'elle a dit, chiffres et sources compris
  3. savoir ce que Momenta vend

Contraintes de forme, autorité `Boite-a-outils/Identite-visuelle.md` :
  · dosage mesuré du site : ~73 % de neutres, ~24 % de vert nuit, 2 % de corail
  · AUCUNE ombre portée : 142 déclarations sur 148 valent none sur le vrai site
  · rayon dominant 12 px
  · Montserrat partout. Baga est servie depuis le stockage GoHighLevel de Momenta
    et n'est pas garantie hors du site ; les titres sont donc en Montserrat, ce
    qui suit aussi la règle posée par David le 2026-08-27.
"""
import html
import re
from pathlib import Path

import contenu as C

RACINE = Path(__file__).resolve().parent

VERT = "#01282b"
VERT_2 = "#3e5b5d"
CORAIL = "#ff706b"
CREME = "#f2f0eb"
BLANC_CASSE = "#fcfcfa"
GRIS_CHAUD = "#ded9d4"


# Espace fine insecable et espace insecable.
FINE, INSEC = "\u202f", "\u00a0"


def typographie(t):
    """Applique les espaces insecables du francais.

    🐛 Sans ca, « plus de 100 000 $ » se coupait entre le 100 et le 000 en fin de
    ligne, et « 88 % » pouvait laisser le % seul au debut de la suivante. C'est
    une regle de composition francaise, pas une preference : un nombre ne se
    fractionne pas et l'unite ne quitte pas son nombre.
    """
    # separateur de milliers : 100 000 -> 100 fine 000, autant de fois qu'il faut.
    # 🐛 La negation en fin de motif exclut les NUMEROS DE TELEPHONE : sans elle,
    # « 514 889-9649 » recevait une espace fine, comme si 514 etait un millier.
    for _ in range(3):
        t = re.sub(r"(\d)\s(\d{3})\b(?![\s]*[-\u2011])", rf"\1{FINE}\2", t)
    # l'unite reste collee au nombre
    t = re.sub(r"(\d)\s+([%$€])", rf"\1{INSEC}\2", t)
    # ponctuation haute : espace fine insecable avant
    t = re.sub(r"\s+([;:!?])", rf"{FINE}\1", t)
    # guillemets francais
    t = t.replace("« ", f"«{FINE}").replace(" »", f"{FINE}»")
    return t


def e(t):
    """Échappe, applique la typographie, laisse passer les <br> voulus."""
    return typographie(html.escape(t).replace("&lt;br&gt;", "<br>"))


CSS = f"""
*,*::before,*::after{{box-sizing:border-box}}
:root{{
  --vert:{VERT}; --vert2:{VERT_2}; --corail:{CORAIL};
  --creme:{CREME}; --blanc:{BLANC_CASSE}; --gris:{GRIS_CHAUD};
  /* ✏️ David, 2026-08-27 : « il y a trop d'espace vide dans le site, augmente un
     peu la densité ». La colonne passe de 820 à 900 px.
     🔴 Elle ne monte pas plus haut : à 900 px et 16 px de corps, une ligne de
     texte suivi fait déjà ~85 signes, la limite haute du confortable. Le reste
     de la densité vient donc du vertical et de la mise en colonnes, jamais d'un
     allongement de la ligne. */
  --rayon:12px; --large:900px;

  /* ── L'échelle typographique, reprise de Mon Espace ────────────────────
     ✏️ David, 2026-08-27 : « les plus petits formats de police sont trop petits.
     Regarde ce qu'on fait dans Mon Espace pour t'y fier. »

     🔴 Le défaut n'était pas une taille, c'était leur NOMBRE. La page portait
     huit valeurs fixes (12, 13, 14, 15, 16, 17, 18, 26) plus huit clamps.
     Personne ne distingue 13 px de 14 px : ce sont des crans qui n'existent que
     dans le code. Mon Espace a fait ce ménage le 2026-08-17 et en a tiré la
     règle : LA HIÉRARCHIE SE FAIT PAR LA GRAISSE ET LA COULEUR, pas par des
     demi-pixels. Cinq crans suffisent, et il n'y en aura pas un sixième.

     📄 Et le plancher est MESURÉ, pas jugé à l'œil. Legge et Bigelow, Journal of
     Vision 2011 : la plage de lecture fluente commence à 1,40 mm de hauteur d'x
     à 40 cm. Sur un iPhone 15, avec la hauteur d'x réelle de Montserrat, 14 px
     donnent 1,32 mm et 15 px donnent 1,41 mm. Un pixel, et ça change de camp.
     C'est pourquoi `--t-source` vaut 15 et non 14 : Mon Espace l'a monté le
     2026-08-19 après que David ait demandé « est-ce qu'on est sur la limite ? ».

     🟡 L'étiquette reste à 12 px. Elle ne porte que des attributions de source,
     qu'on lit une fois, jamais pendant la lecture. Ce qui prouvait quelque chose
     (le prix OSEntreprendre) en est sorti et monte d'un cran. */
  --t-titre: 1.625rem;      /* 26 px  le nom d'une section                     */
  --t-section: 1.25rem;     /* 20 px  un intertitre, un titre de bloc          */
  --t-corps: 1.0625rem;     /* 17 px  TOUT le texte qu'on lit                  */
  --t-source: .9375rem;     /* 15 px  une attribution. LE PLANCHER.            */

  /* 🐛 Deuxieme passe, le meme jour. David : « la hierarchie de grosseur de texte
     n'a plus tellement son sens ». Il a raison, et j'avais fait le menage a
     moitie : je gardais DEUX corps de texte, 17 et 15, que rien ne distinguait.
     Un descriptif de carte a 15 px et un paragraphe de bloc a 17 px disent la
     meme sorte de chose ; la taille suggerait une hierarchie qui n'existait pas.

     🔴 Un cran par ROLE, jamais un cran par emplacement. `--t-detail` a disparu :
     son nom meme invitait la derive, puisque « detail » ne dit rien du role et
     accueille donc n'importe quoi. `--t-source` ne peut servir qu'a une chose.

     🔴 C'est la regle de Mon Espace appliquee jusqu'au bout : LA HIERARCHIE SE
     FAIT PAR LA GRAISSE ET LA COULEUR. Ce qui accompagne n'est pas plus petit,
     il est en `--vert2` ; ce qui porte est en `--vert`. Meme corps pour les deux. */
}}
html{{-webkit-text-size-adjust:100%}}
body{{
  margin:0; background:var(--creme); color:var(--vert);
  font-family:Montserrat,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  font-size:var(--t-corps); line-height:1.55; font-weight:400;
}}
.enveloppe{{max-width:var(--large); margin:0 auto; padding:0 20px}}
section{{padding:40px 0}}                    /* etait 56 : 18 px x 2 x 11 sections */
section+section{{border-top:1px solid var(--gris)}}
h1,h2,h3{{line-height:1.15; margin:0; font-weight:700; letter-spacing:-.01em}}
h2{{font-size:clamp(var(--t-titre),4.4vw,1.75rem); margin-bottom:8px}}
h3{{font-size:var(--t-section)}}
p{{margin:0 0 12px}}
p:last-child{{margin-bottom:0}}
/* R9 : la mesure. Une colonne de 900 px à 17 px donne ~85 signes par ligne,
   au-delà des 65-75 confortables. Les cartes gardent la pleine largeur (leur
   texte est court), le texte suivi est bridé. */
.mineur{{color:var(--vert2); max-width:68ch}}
.source{{font-size:var(--t-source); color:var(--vert2); margin-top:6px}}

/* ── En-tête ─────────────────────────────────────────────────────────── */
header{{background:var(--vert); color:var(--blanc); padding:40px 0 36px}}
header .logo{{height:26px; width:auto; display:block; margin-bottom:28px}}
header h1{{font-size:clamp(30px,7vw,46px)}}
header .role{{color:var(--gris); margin-top:10px; font-size:clamp(var(--t-corps),2.6vw,var(--t-section))}}

/* La feuille : elle se pose sur le fond, sans cadre ni ombre. 🔴 Le masque est
   DANS le PNG, decoupe par feuille_momenta.py. Ne JAMAIS lui remettre un
   border-radius par-dessus : la fausse forme abimerait la vraie. */
.bloc{{display:flex; flex-direction:column-reverse; gap:24px}}
.portrait{{width:min(230px,58%); height:auto; display:block; align-self:flex-start}}
@media(min-width:760px){{
  .bloc{{flex-direction:row; align-items:center; justify-content:space-between; gap:36px}}
  .bloc .texte{{flex:1; min-width:0}}
  .portrait{{width:250px; flex:none; align-self:center}}
}}

/* ── Les boutons de contact, le geste le plus important de la page ───── */
.contacts{{display:flex; flex-wrap:wrap; gap:10px; margin-top:24px}}
.contacts a{{
  display:inline-flex; align-items:center; gap:8px;
  padding:12px 20px; border-radius:25px; text-decoration:none;
  font-size:var(--t-corps); font-weight:600; border:2px solid transparent;
  /* R12 : deux propriétés nommées, jamais `all`, et 160 ms en ease-out.
     Un bouton qui répond doit répondre vite ; ce qui entre sort en ease-out. */
  transition:background-color 160ms ease-out, color 160ms ease-out;
}}
/* 🚨 R11. Il n'y avait AUCUN état de focus sur cette page, alors que son geste
   principal est de cliquer un lien de contact. Quiconque navigue au clavier ne
   voyait pas où il était. L'anneau est en corail, décollé de 3 px, et il ne
   s'affiche qu'au clavier grâce à `:focus-visible`. */
.contacts a:focus-visible,footer a:focus-visible{{
  outline:3px solid var(--corail); outline-offset:3px; border-radius:var(--rayon-bouton);
}}
.contacts a:active{{transform:translateY(1px)}}
footer a{{color:inherit; text-decoration:underline; text-underline-offset:2px}}
footer a:hover{{color:var(--blanc)}}
/* R7 : le blanc pur n'existe pas dans le kit. Le blanc cassé, si. */
.principal{{background:var(--corail); color:var(--blanc)}}
.principal:hover{{background:#ff8a86}}
.secondaire{{border-color:var(--gris); color:var(--blanc)}}
.secondaire:hover{{background:rgba(255,255,255,.08)}}
.contacts svg{{width:17px;height:17px;flex:none;fill:currentColor}}

/* ── Le message à retenir ────────────────────────────────────────────── */
.retenir p.phrase{{
  font-size:clamp(26px,5.6vw,38px); font-weight:700; line-height:1.18;
  letter-spacing:-.015em; margin-bottom:16px;
}}
/* ✏️ David, 2026-08-27 : « Marie-Claude Viau, fondatrice de Momenta, c'est trop
   petit ».
   🔴 Il a raison et le defaut etait structurel : `.source` sert partout a
   attribuer un CHIFFRE (« Statistique Canada », « n = 22 »), ou le petit corps
   est juste. Ici la meme classe attribuait la PHRASE de la page. Une signature
   d'auteur n'est pas une note de bas de tableau : elle passe a 17 px, en vert
   nuit et en demi-gras, sous un filet corail qui la rattache a la citation. */
.retenir .source{{
  font-size:var(--t-section); font-weight:600; color:var(--vert); margin-top:20px;
  padding-top:12px; border-top:2px solid var(--corail); display:inline-block;
}}

/* ── Les chiffres ────────────────────────────────────────────────────── */
.chiffres{{display:grid; gap:14px; grid-template-columns:1fr}}
@media(min-width:640px){{.chiffres{{grid-template-columns:1fr 1fr}}}}
.chiffre{{background:var(--blanc); border-radius:var(--rayon); padding:22px}}
.chiffre .n{{font-size:clamp(32px,7vw,42px); font-weight:700; color:var(--corail);
  line-height:1; letter-spacing:-.02em}}
.chiffre p{{margin:12px 0 0; font-size:var(--t-corps)}}
.chiffre.fort{{background:var(--vert); color:var(--blanc)}}
.chiffre.fort .source{{color:var(--gris)}}
@media(min-width:640px){{.chiffre.fort{{grid-column:1/-1}}}}

/* ── Les résultats ───────────────────────────────────────────────────── */
.res{{background:var(--blanc); border-radius:var(--rayon); padding:22px; margin-top:14px}}
.ligne{{display:flex; align-items:baseline; gap:12px; padding:12px 0}}
.ligne+.ligne{{border-top:1px solid var(--gris)}}
.ligne .lib{{flex:1; font-size:var(--t-corps); color:var(--vert2)}}
.ligne .av{{color:var(--vert2); font-size:var(--t-corps)}}
.ligne .fl{{color:var(--gris)}}
.ligne .ap{{font-weight:700; font-size:var(--t-section); min-width:44px; text-align:right}}
.ligne.vedette .lib{{color:var(--vert); font-weight:600}}
.ligne.vedette .ap{{color:var(--corail); font-size:var(--t-titre)}}
.appuis{{display:flex; flex-wrap:wrap; gap:24px; margin-top:18px}}
.appui .n{{font-size:var(--t-titre); font-weight:700; color:var(--corail); line-height:1}}
.appui p{{margin:4px 0 0; font-size:var(--t-corps); color:var(--vert2); max-width:210px}}
/* Les trois jalons de « Qui parle » ouvrent une section : ils portent plus que
   les appuis d'un tableau de résultats, d'où la taille et l'espace au-dessous. */
.jalons{{margin:4px 0 16px}}
.jalons .n{{font-size:clamp(28px,5vw,34px)}}
.jalons p{{font-size:var(--t-corps); max-width:235px}}   /* « dans le milieu de la conférence » sur une ligne */

/* ── Le mur de logos ─────────────────────────────────────────────────────
   Hauteur EGALE pour les trois, marges transparentes deja rognees a la source :
   deux logos a la meme hauteur CSS n'ont pas la meme taille optique si leurs
   marges different.
   🐛 Le carre de Noovo a d'abord ete REDUIT, ce qui etait l'inverse du bon geste :
   son lettrage n'occupe que ~60 % de sa hauteur, alors qu'un mot-symbole l'occupe
   en entier. A hauteur egale son texte fait la moitie des autres. On l'agrandit
   donc pour egaliser la hauteur des LETTRES, pas celle des cadres. */
.logos{{display:flex; flex-wrap:wrap; align-items:center; gap:24px 36px; margin:16px 0 16px}}
.logos img{{height:34px; width:auto; display:block}}
.logos img[width="102"]{{height:52px}}
@media(max-width:520px){{.logos{{gap:22px 26px}} .logos img{{height:27px}}
  .logos img[width="102"]{{height:42px}}}}

/* ── Preuve de scène ─────────────────────────────────────────────────── */
.etiquettes{{display:flex; flex-wrap:wrap; gap:8px; margin:12px 0 16px}}
.etiquettes span{{background:var(--gris); border-radius:25px; padding:8px 16px; font-size:var(--t-corps)}}
.scene{{padding:10px 0}}
.scene+.scene{{border-top:1px solid var(--gris)}}
.scene p{{margin:4px 0 0; font-size:var(--t-corps); color:var(--vert2)}}

/* ── Offre ───────────────────────────────────────────────────────────── */
/* Quatre blocs courts empilés laissaient une colonne de vide à droite sur tout
   écran large. En grille de deux, la section perd la moitié de sa hauteur et
   se lit d'un coup d'œil, ce qu'un catalogue doit faire. */
.grille-offre{{display:grid; gap:14px; grid-template-columns:1fr}}
@media(min-width:700px){{.grille-offre{{grid-template-columns:1fr 1fr}}}}
.offre{{background:var(--blanc); border-radius:var(--rayon); padding:22px; margin:0}}
.offre p{{font-size:var(--t-corps); margin:8px 0 0}}
.offre .modalite{{font-size:var(--t-corps); color:var(--vert2); margin-top:10px}}

/* ── Les trois conférences, réduites au titre et à la case ────────────────
   🐛 Le style de `.case` était accroché à `.theme`, qui n'existe plus depuis
   l'allègement : la case de programmation sortait en gris ordinaire et le titre
   la dominait, alors que c'est elle qui dit à un planificateur où ça rentre. */
.titre-conf h3{{color:var(--corail); line-height:1.3}}
.titre-conf p{{font-size:var(--t-corps); color:var(--vert2); margin:8px 0 0}}

/* ── Les formatrices ─────────────────────────────────────────────────────
   Une liste, pas des cartes : ce sont des noms qu'on parcourt à la verticale
   pour en reconnaître un. Une grille de six cartes ferait un mur à déchiffrer. */
.formatrices{{margin:14px 0 4px}}
.formatrice{{padding:12px 0; display:flex; flex-wrap:wrap; align-items:baseline; gap:4px 12px}}
.formatrice+.formatrice{{border-top:1px solid var(--gris)}}
.preuve{{font-size:var(--t-corps); margin:0}}
.formatrice strong{{font-size:var(--t-corps); min-width:214px}}
.formatrice span{{font-size:var(--t-corps); color:var(--vert2); flex:1}}
/* 🐛 Sur téléphone, le `min-width` du nom laissait au titre un rail d'environ
   130 px : « Ph. D., directrice du Centre d'études sur le stress humain » sortait
   sur six lignes de deux mots. Sous 640 px, le nom prend sa ligne et le titre la
   suivante, en pleine largeur. */
@media(max-width:640px){{
  .formatrice{{display:block}}
  .formatrice strong{{min-width:0; display:block}}
  .formatrice span{{display:block; margin-top:2px}}
}}

/* ── Deux sujets, deux formats ───────────────────────────────────────────
   Les deux sujets côte à côte : la lecture parallèle dit « il y en a deux »
   plus vite qu'une liste, et c'est exactement ce qu'on veut faire comprendre.
   Le bloc panel est en vert nuit parce qu'il doit se voir : c'est la case de
   programmation que la carte oubliait de proposer. */
.sujets{{display:grid; gap:14px; grid-template-columns:1fr; margin:14px 0}}
@media(min-width:640px){{.sujets{{grid-template-columns:1fr 1fr}}}}
.sujet{{background:var(--blanc); border-radius:var(--rayon); padding:20px}}
.sujet h3{{color:var(--corail)}}
.sujet p{{font-size:var(--t-corps); margin:8px 0 0; color:var(--vert2)}}
.panel{{background:var(--vert); color:var(--blanc); border-radius:var(--rayon);
  padding:24px}}
.panel h3{{font-size:var(--t-section)}}
.panel p{{font-size:var(--t-corps); margin:0; color:var(--gris)}}
.panel .source{{color:var(--gris)}}
.cite-clair{{margin:16px 0 0; border-left-color:var(--corail)}}
.cite-clair p{{color:var(--blanc); font-size:clamp(var(--t-corps),3vw,var(--t-section))}}

/* Les trois titres de conférence, réduits au titre et à la case. */
.titres{{display:grid; gap:12px; grid-template-columns:1fr; margin:18px 0 10px}}
@media(min-width:760px){{.titres{{grid-template-columns:repeat(3,1fr)}}}}
.titre-conf{{background:var(--blanc); border-radius:var(--rayon); padding:18px 20px}}
.titre-conf h3{{line-height:1.3}}

/* ── L'appel, la dernière chose qu'on lit ────────────────────────────── */
.appel{{background:var(--vert); color:var(--blanc)}}
.appel h2{{color:var(--blanc)}}
.appel p{{color:var(--gris); max-width:56ch}}

/* ── Citation : un filet à gauche, jamais un cadre. Le kit ne cerne rien ── */
.cite{{margin:0 0 18px; padding:2px 0 2px 20px; border-left:3px solid var(--corail)}}
.cite p{{font-size:clamp(var(--t-section),3.4vw,1.375rem); font-weight:600; margin:0; line-height:1.3}}

/* ── Honnêteté ───────────────────────────────────────────────────────── */
.honnete{{background:var(--vert); color:var(--blanc); border-radius:var(--rayon); padding:24px}}
.honnete p{{font-size:var(--t-corps); margin:0}}

/* ── Pied ────────────────────────────────────────────────────────────── */
footer{{background:var(--vert); color:var(--gris); padding:32px 0; font-size:var(--t-corps)}}
footer a{{color:var(--blanc); text-decoration:none; border-bottom:1px solid var(--vert2)}}
footer .logo{{height:22px; margin-bottom:20px; display:block}}

/* ── Impression : MC veut que la page devienne la pièce jointe ───────── */
@media print{{
  body{{background:#fff; font-size:11pt}}
  header,footer,.honnete,.chiffre.fort{{background:#fff!important; color:{VERT}!important}}
  header .role,footer,.chiffre.fort .source{{color:{VERT_2}!important}}
  .contacts{{display:none}}
  .portrait{{width:150px}}
  section{{padding:16px 0; break-inside:avoid}}
  .chiffre,.res,.offre{{border:1px solid {GRIS_CHAUD}}}
}}
"""

ICONES = {
    "courriel": '<svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 '
                '002-2V6a2 2 0 00-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>',
    "tel": '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 006.6 6.6l2.2-2.2a1 1 0 011-.2 11 '
           '11 0 003.5.6 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11 '
           '11 0 00.6 3.5 1 1 0 01-.3 1l-2.2 2.3z"/></svg>',
    "in": '<svg viewBox="0 0 24 24"><path d="M4.98 3.5a2.5 2.5 0 100 5 2.5 2.5 0 000-5zM3 21h4V9H3v12zM'
          '9 21h4v-6.5c0-1.7 2-1.8 2 0V21h4v-7.9c0-4.5-4.9-4.3-6-2.1V9H9v12z"/></svg>',
    "web": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zm6.9 6h-2.9a15.6 15.6'
           ' 0 00-1.4-3.7A8 8 0 0118.9 8zM12 4c.8 1.1 1.4 2.5 1.8 4h-3.6C10.6 6.5 11.2 5.1 12 4zM4.3 '
           '14a8 8 0 010-4h3.3a17 17 0 000 4H4.3zm.8 2h2.9c.3 1.3.8 2.6 1.4 3.7A8 8 0 015.1 16zm2.9-8'
           'H5.1a8 8 0 014.3-3.7A15.6 15.6 0 008 8zm4 12c-.8-1.1-1.4-2.5-1.8-4h3.6c-.4 1.5-1 2.9-1.8 '
           '4zm2.2-6H9.8a15 15 0 010-4h4.4a15 15 0 010 4zm.4 5.7c.6-1.1 1.1-2.4 1.4-3.7h2.9a8 8 0 01-'
           '4.3 3.7zM16.4 14a17 17 0 000-4h3.3a8 8 0 010 4h-3.3z"/></svg>',
}


def bouton(href, texte, icone, principal=False):
    return (f'<a class="{"principal" if principal else "secondaire"}" href="{href}">'
            f'{ICONES[icone]}{e(texte)}</a>')


def rendre():
    ch = "".join(
        f'<div class="chiffre{" fort" if c.get("fort") else ""}">'
        f'<div class="n">{e(c["n"])}</div><p>{e(c["t"])}</p>'
        f'<div class="source">{e(c["src"])}</div></div>'
        for c in C.CHIFFRES)

    lignes = "".join(
        f'<div class="ligne{" vedette" if v else ""}"><span class="lib">{e(lib)}</span>'
        f'<span class="av">{e(a)}</span><span class="fl">→</span>'
        f'<span class="ap">{e(b)}</span></div>'
        for lib, a, b, v in C.RESULTATS["lignes"])

    appuis = "".join(f'<div class="appui"><div class="n">{e(n)}</div><p>{e(t)}</p></div>'
                     for n, t in C.RESULTATS["appuis"])
    jalons = "".join(f'<div class="appui"><div class="n">{e(n)}</div><p>{e(t)}</p></div>'
                     for n, t in C.QUI_PARLE["jalons"])

    etiq = "".join(
        f'<img src="{src}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy">'
        for src, alt, w, h in C.PRESSE["logos"])
    scenes = "".join(f'<div class="scene"><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                     for t, d in C.PRESSE["scenes"])
    balados = "".join(f"<span>{e(b)}</span>" for b in C.PRESSE["balados"])

    offre = "".join(
        f'<div class="offre"><h3>{e(t)}</h3><p>{e(d)}</p>'
        f'<div class="modalite">{e(m)}</div></div>'
        for t, d, m in C.OFFRE["items"])

    points = "".join(f"<li>{e(p)}</li>" for p in C.CONFERENCE["points"])

    sujets = "".join(f'<div class="sujet"><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                     for t, d in C.FORMATS["sujets"])

    # Les trois conférences perdent leur description : il reste le titre et la case
    # de programmation. Un planificateur a besoin de savoir QUE ça existe et OÙ ça
    # rentre ; le contenu, il le demandera au téléphone. C'est le but de la page.
    demandes = "".join(
        f'<div class="titre-conf"><h3>{e(t)}</h3><p>{e(d)}</p></div>'
        for t, d in C.DEMANDES)

    formatrices = "".join(
        f'<div class="formatrice"><strong>{e(n)}</strong><span>{e(t)}</span></div>'
        for n, t in C.FORMATRICES["liste"])

    return f"""<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(C.MC['nom'])} · {e(C.CONFERENCE['titre'])}</title>
<meta name="description" content="{e(C.CONFERENCE['chapeau'])}">
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/favicon-180.png">
<meta name="theme-color" content="{VERT}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<header>
  <div class="enveloppe">
    <img class="logo" src="assets/logo-light.png" alt="Momenta">
    <div class="bloc">
    <div class="texte">
    <h1>{e(C.MC['nom'])}</h1>
    <div class="role">{e(C.MC['role'])}</div>
    <div class="contacts">
      {bouton("mailto:" + C.MC['courriel'], "Écrire à Marie-Claude", "courriel", True)}
      {bouton("tel:" + C.MC['telephone_lien'], C.MC['telephone'], "tel")}
      {bouton(C.MC['linkedin'], "LinkedIn", "in")}
      {bouton(C.MC['site'], "momentareseau.com", "web")}
    </div>
    </div>
    <img class="portrait" src="assets/mc-feuille.png"
         alt="Portrait de {e(C.MC['nom'])}" width="760" height="760">
    </div>
  </div>
</header>

<section class="retenir"><div class="enveloppe">
  <p class="phrase">{e(C.TAKE_HOME['phrase'])}</p>
  <p class="mineur">{e(C.TAKE_HOME['appui'])}</p>
  <div class="source">{e(C.TAKE_HOME['source'])}</div>
</div></section>

<!-- ✏️ David, 2026-08-27 : « diminue le contenu au strict minimum. Ce qu'on veut
     c'est générer un appel et une demande. Pas booker tout de suite la vente. »

     🔴 La page était un DOSSIER DE VENTE : chiffres sourcés, scores de cohorte
     avant-après, quatre volets d'offre avec le prix. Tout ça répond à des
     questions qu'un acheteur ne se pose qu'APRÈS avoir décidé de parler à
     quelqu'un. Avant, il n'en a qu'une : « est-ce que je l'appelle ? »
     Une page qui répond trop tôt remplace l'appel au lieu de le provoquer.

     Ce qui est sorti, et pourquoi : les quatre chiffres (c'est la matière de la
     conférence, pas un argument d'achat) · le tableau de cohorte et le NPS (ça
     vend le parcours à un DRH, pas une conférence à un planificateur) · les
     quatre volets d'offre avec le prix (c'est la vente elle-même) · « Ce qu'elle
     raconte » (doublait les trois conférences).

     Ce qui reste répond à trois questions et s'arrête : pourquoi la croire, quoi
     lui demander, comment la joindre. -->

<section><div class="enveloppe">
  <h2>Qui parle</h2>
  <div class="appuis jalons">{jalons}</div>
  <p class="mineur">{e(C.QUI_PARLE['parcours'])}</p>
  <p class="mineur">{e(C.QUI_PARLE['certification'])}</p>
  <div class="logos">{etiq}</div>
  <p class="mineur">{e(C.PRESSE['intro'])}</p>
  <div class="etiquettes">{balados}</div>
  <!-- 🔴 Le prix sort de `.source`. Une attribution se lit une fois et peut vivre
       à 12 px ; un prix PROUVE quelque chose et doit se lire du premier coup. -->
  <p class="mineur preuve">{e(C.PRESSE['prix'])}</p>
</div></section>

<section><div class="enveloppe">
  <h2>Ce qu’on peut lui demander</h2>
  <p class="mineur">Deux sujets : la transition parentale, et l’accomplissement.</p>
  <div class="titres">{demandes}</div>
  <div class="panel">
    <p class="dit">{e(C.FORMATS['panel']['texte'])}</p>
    <blockquote class="cite cite-clair"><p>{e(C.FORMATS['panel']['citation'])}</p>
      <div class="source">{e(C.FORMATS['panel']['source'])}</div></blockquote>
  </div>
  <div class="source">{e(C.CONFERENCE['formats'])}</div>
</div></section>

<!-- 🔴 L'idée est de MC : « ils vont voir OK, elle a une crédibilité waouh, elle
     travaille avec des tops ». Nommer des sommités fait plus pour sa crédibilité
     que n'importe quelle phrase qu'elle écrirait sur elle-même, et c'est le
     déclencheur d'appel qu'elle décrit : « Sonia Lupien dans ton parcours,
     est-ce que vous la vendez ? » -->
<section><div class="enveloppe">
  <h2>Avec qui elle travaille</h2>
  <p class="mineur">{e(C.FORMATRICES['intro'])}</p>
  <div class="formatrices">{formatrices}</div>
  <div class="source">{e(C.FORMATRICES['source'])}</div>
</div></section>

<section class="retenir"><div class="enveloppe">
  <p class="phrase">{e(C.FERMETURE['phrase'])}</p>
  <p class="mineur">{e(C.FERMETURE['appui'])}</p>
  <div class="source">{e(C.FERMETURE['source'])}</div>
</div></section>

<!-- 🔴 Le seul appel à l'action de la page, et il est en bas. La règle du
     peak-end vaut ici comme sur scène : ce qu'on lit en dernier pèse le plus.
     Il ne demande pas d'acheter, il demande de parler. -->
<section class="appel"><div class="enveloppe">
  <h2>{e(C.APPEL['titre'])}</h2>
  <p>{e(C.APPEL['texte'])}</p>
  <div class="contacts">
    {bouton("mailto:" + C.MC['courriel'], "Écrire à Marie-Claude", "courriel", True)}
    {bouton("tel:" + C.MC['telephone_lien'], C.MC['telephone'], "tel")}
  </div>
</div></section>

<footer><div class="enveloppe">
  <img class="logo" src="assets/logo-light.png" alt="Momenta">
  <p>{e(C.MC['nom'])} · {e(C.MC['ville'])}<br>
  <a href="mailto:{C.MC['courriel']}">{e(C.MC['courriel'])}</a> ·
  <a href="tel:{C.MC['telephone_lien']}">{e(C.MC['telephone'])}</a></p>
  <p><a href="{C.MC['linkedin']}">LinkedIn</a> · <a href="{C.MC['site']}">momentareseau.com</a></p>
</div></footer>

</body></html>
"""


if __name__ == "__main__":
    page = rendre()
    # Garde-fou : la règle dure du protocole anti-signature IA vaut aussi ici.
    tirets = re.findall(r"[—–]", page)
    if tirets:
        raise SystemExit(f"ARRÊT : {len(tirets)} tiret(s) cadratin dans la page.")
    (RACINE / "index.html").write_text(page, encoding="utf-8")
    print(f"écrit : {RACINE / 'index.html'}  ({len(page):,} octets)".replace(",", " "))
