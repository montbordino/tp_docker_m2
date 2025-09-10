# Tp 2 - Optimisation docker
Lors de ce tp qui consiste à optimiser le serveur nous utiliserons comme mesures le **temps de build** et la **taille de l'image** pour déterminer l'optimisation de celle-ci. 

Pour éviter que le **cache** des builds précédents fausse les résultats, nous utiliserons la commande `docker system prune --all --force`. Elle permet de supprimer le cache, les builds, containers, env et images sans demander de confirmation.
On peut également utiliser la commande `--no-cache` lors du build pour éviter d'y accéder.

Le test de chaque version du projet se fera de la manière suivant:
- suppression du cache
- build de l'image `docker build -t tp2_v1 .`
- verification de la taille de l'image `docker images`
- lancement de l'image `docker run -d -p 3000:3000 tp2_v1`
- test du projet sur le port 3000 dans un navigateur

### 1 - commit initial

Pour le moment le projet n'as pas été modifié, le build est long et l'image est lourde. On remarque que les étapes les plus longues sont :
- recupération node &nbsp;→ 37s
- commandes run &nbsp;&nbsp;&nbsp; → 25s
- export en image &nbsp;&nbsp;&nbsp; → 10s

build: 77.8s
taille: 1.77GB

### 2 - suppression des nodes_modules de github
Lors de cette etape on ajoute un .gitignore et on supprime les nodes modules du cache avec cette commande : `git rm -r --cached .`
Elle n'optimise pas le docker mais cette étape est primordiale pour le dépot github.

build: 77.8s
taille: 1.77GB


### 3 - image node
Dans le projet on charge la dernière image de node `FROM node:latest`. La meilleure façon de charger node serai de charger une **version précise de node** car en cas de montée de version de node notre projet pourrait ne plus fonctionner. De plus on peut choisir de télécharger une image lite de node pour réduire la taille de l'image. On choisi ici node:24-slim, cette version est plus légère et réduit la taille de l'image. Cependant elle rallonge certaines taches, notement les méthodes RUN.

build: 127s
taille: 953MB

### 4 - modification des COPY

Il est préférable de ne faire qu'un seul copy de toute l'application plutot que de faire plusieurs copies. En effet chaque COPY crée une nouvelle couche dans l'image et augmente la taille de celle-ci. De plus, en copiant tout le projet on évite d'oublier des fichiers.

build: 132s
taille: 919MB

### 5 - suppression des run inutiles

Lors de cette étape on supprime la commande RUN qui installait les locales. En effet cette commande n'est pas utile pour le projet et alourdit l'image. Cette étape est longue et n'apporte rien au projet.

build: 23.8s
taille: 358MB