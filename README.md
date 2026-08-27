# Carte de conférencière — Marie-Claude Viau

Page remise aux acheteurs de conférence après la présentation de 12 minutes.
Elle sert trois choses, dans cet ordre : rejoindre MC en un geste, retrouver les
chiffres de la présentation avec leurs sources, savoir ce que Momenta vend.

```bash
python3 build.py       # contenu.py + le gabarit -> index.html
python3 verifier.py    # la barrière : refuse la publication si un interdit y figure
```

Le texte et les chiffres vivent dans `contenu.py`, jamais dans `build.py`.

## Ce dépôt est public

Tout ce qui entre dans `index.html` est lisible par n'importe qui, pour toujours,
y compris dans l'historique git. `verifier.py` bloque les interdits connus :
les gratuités stratégiques nommées comme clientes, les outcomes du site dont la
provenance n'est pas documentée, les données sous entente de confidentialité.
Il ne remplace pas la lecture.

## Autorités

| Quoi | Où |
|---|---|
| Les chiffres et leur source | `Ce-que-je-vends/Marketing/Trousse-financement-employeur.md`, table de traçabilité |
| La palette, la typo, le dosage | `Boite-a-outils/Identite-visuelle.md` |
| Le texte sortant | `Boite-a-outils/Protocole-anti-signature-IA.md` |
| Le deck de la conférence | `scripts/deck/presentation-vitrine-12min.js` |
