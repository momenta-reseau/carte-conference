# Passer à info.momentareseau.com

Aujourd'hui la page vit à `momenta-reseau.github.io/carte-conference/`. Le mot
« github » y est visible, et l'adresse fait cinquante caractères.

Un sous-domaine de `momentareseau.com` règle les deux. C'est gratuit, GitHub le
supporte nativement, et le certificat HTTPS s'installe tout seul.

## ⚠️ L'ordre compte, et il n'est pas négociable

Poser le fichier `CNAME` dans ce dépôt **avant** que le DNS réponde rend la page
inaccessible : GitHub Pages arrête de servir l'ancienne adresse et redirige vers
un domaine qui ne pointe encore nulle part. À cinq jours de l'événement, ça se
fait dans cet ordre ou pas du tout.

### 1. Le DNS, en premier

La zone de `momentareseau.com` est chez **Google Cloud DNS** (les serveurs de
noms sont `ns-cloud-c1` à `c4.googledomains.com`). Il faut y ajouter :

```
Type   : CNAME
Nom    : info
Valeur : momenta-reseau.github.io.
TTL    : 3600
```

Ça ne touche ni le domaine racine ni `www` : le site principal, servi par
GoHighLevel derrière Cloudflare, n'est pas affecté.

### 2. Vérifier que ça répond

```bash
dig +short info.momentareseau.com
```

La réponse doit contenir `momenta-reseau.github.io` puis les quatre adresses de
GitHub (185.199.108.153 à 111.153). Compter de quelques minutes à deux heures.

### 3. Seulement ensuite, le dépôt

```bash
echo "info.momentareseau.com" > CNAME
git add CNAME && git commit -m "Domaine : info.momentareseau.com" && git push
gh api -X PUT repos/momenta-reseau/carte-conference/pages \
  -f "cname=info.momentareseau.com" -F "https_enforced=true"
```

Le certificat HTTPS met jusqu'à quinze minutes. Tant qu'il n'est pas prêt, le
navigateur avertit : c'est normal, il ne faut pas revenir en arrière.

### 4. Le code QR, en dernier

```bash
python3 ~/Obsidian/Momenta/scripts/deck/qr_momenta.py \
  "https://info.momentareseau.com" \
  ~/Obsidian/Momenta/Boite-a-outils/Ressources/QR_Carte_Conference.png
```

Puis régénérer et repousser le deck. **Ne pas le faire avant que le domaine
réponde** : un QR qui mène à une erreur est pire qu'un QR long.

## Ce que le changement rapporte

| | aujourd'hui | après |
|---|---|---|
| Adresse | momenta-reseau.github.io/carte-conference | **info.momentareseau.com** |
| Longueur | 50 caractères | **30** |
| Code QR | version 6, 49 × 49 modules | **version 4, 41 × 41** |

Le code se simplifie de deux versions. Moins de modules veut dire des carrés plus
gros à surface égale, donc un code qui se lit de plus loin dans une salle. C'est
le vrai gain, au-delà du nom.

## Ce qu'il ne faut pas faire

**Acheter un domaine dédié.** Un sous-domaine coûte zéro et rattache la page à la
marque ; un domaine séparé coûte tous les ans et la détache.

**Choisir un nom long.** `conference.momentareseau.com` fait trente-six
caractères et ramène le code à la version 5. `info` se dicte au téléphone, se
tape sans faute, et tient sous un code QR.

**Toucher au domaine racine ou à `www`.** Ils servent le site GoHighLevel. Le
sous-domaine `mc` est indépendant.
