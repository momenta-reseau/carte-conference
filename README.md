# Marie-Claude Viau — conférencière et panéliste

Page remise aux planificateurs d'événements après une présentation.
En ligne : https://momenta-reseau.github.io/conference2026/

## Régénérer

```bash
python3 site.py
```

Un seul fichier. Il porte le contenu, le gabarit et les contrôles. Les contrôles
tournent **avant** l'écriture : si l'un échoue, aucun fichier ne sort et rien ne
peut être publié.

## Ce que la page fait, et ce qu'elle ne fait pas

Elle s'adresse à un planificateur qui vient de voir Marie-Claude parler douze
minutes, debout, sur son téléphone. Elle lui donne trois choses dans cet ordre :
de quoi la joindre, quoi lui demander, pourquoi elle valait le coup.

Elle ne vend rien. Aucun prix, aucun formulaire, aucun catalogue. Marie-Claude,
le 2026-08-27 : « je veux pas vendre de conférence, c'est pas dans mon carré de
sable ». Le but est un appel, pas une transaction.

## Ce qui ne peut jamais y entrer

Le dépôt est public : tout ce qui y entre est lisible pour toujours, historique
git compris. Les interdits vivent dans `site.py` et bloquent la publication.

- Rio Tinto, Desjardins, CGI, Beneva comme clientes (gratuités stratégiques)
- les données du sondage Jeune Chambre / Léger (entente de confidentialité)
- les outcomes du site à provenance non documentée (Signal-012)
- le logo de l'Ordre des CRHA, réservé aux personnes inscrites à son tableau
- un titre d'atelier : le site public et les fiches du wiki divergent, et la
  fiche de la formatrice fait autorité
- un tiret cadratin ou demi-cadratin
- un prix

## Ce qui remplace ce dépôt

Le code a été refait de zéro le 2026-08-27, à cette même adresse. Le dépôt
`momenta-reseau/mcviau`, banc d'essai de cette réécriture, a été supprimé une
fois le contenu ramené ici.
