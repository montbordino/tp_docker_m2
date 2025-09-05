# Tp 2 - Optimisation docker
Lors de ce tp qui consiste à optimiser le serveur nous utiliserons comme mesures le temps de build et la taille de l'image pour déterminer l'optimisation de celle-ci.

### 1 - commit initial
build: 95.5s
taille: 1.73GB

### 2 - suppression des nodes_modules
Lors de cette etape on ajoute un .gitignore et on supprime les nodes modules du cache avec cette commande : `git rm -r --cached .`. Elle n'optimise pas le docker mais cette étape est primordiale pour le dépot github.
build: 95.5s
taille: 1.73GB