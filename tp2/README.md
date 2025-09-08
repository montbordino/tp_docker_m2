# Tp 2 - Optimisation docker
Lors de ce tp qui consiste à optimiser le serveur nous utiliserons comme mesures le **temps de build** et la **taille de l'image** pour déterminer l'optimisation de celle-ci. 

Pour éviter que le **cache** des builds précédents fausse les résultats, nous utiliserons la commande `docker system prune --all --force`. Elle permet de supprimer le cache, les builds, containers, env et images sans demander de confirmation.

Le test de chaque version du projet se fera de la manière suivant:
- suppression du cache
- build de l'image: `docker build -t tp2_v1 .`
- verification de la taille de l'image `docker images`

### 1 - commit initial

Pour le moment le projet n'as pas été modifié, le build est long et l'image est lourde. On remarque que les étapes les plus longues sont :
- recupération node &nbsp;→ 37s
- commandes run &nbsp;&nbsp;&nbsp; → 25s
- export en image &nbsp;&nbsp;&nbsp; → 10s

build: 77.8s
taille: 1.77GB

### 2 - suppression des nodes_modules
Lors de cette etape on ajoute un .gitignore et on supprime les nodes modules du cache avec cette commande : `git rm -r --cached .`
Elle n'optimise pas le docker mais cette étape est primordiale pour le dépot github.

build: 77.8s
taille: 1.77GB
