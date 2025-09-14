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

### 6 - optimisation de l'image node

Maintenant que nous n'utilisons pas de commandes apt-get, nous pouvons alléger encore plus l'image en utilisant une version **alpine** de node 24. Cette version est beaucoup plus légère que la version slim.

build: 48.3s
taille: 260MB

### 7 - optimisation de la version de node

On peut encore alléger l'image en utilisant une version plus ancienne de node. En effet, la version 24 n'apporte pas d'améliorations significatives pour notre projet. On utilise ici la version 16 qui est largement suffisante pour notre projet.

build: 46.3s
taille 194MB

### 8 - supression des éléments inutiles

Cette amélioration ne change pas la taille de l'image mais rend le dockerfile plus propre. 
- On supprime les ports 4000 et 5000 qui ne sont pas utilisés dans le projet. 
- On supprime également la variable d'environnement NODE_ENV qui n'est pas utilisée dans le projet.
- On supprime l'utilisateur root qui n'est pas nécessaire pour le projet.

build: 22.2s
taille: 194MB

### 9 - suppression de mangoDB

Dans le package.json **mangoDb** est ajouté en dépendance dans le projet mais n'est pas utilisé. Pour alléger le projet il faut donc le supprimer. Pour cela on le supprime du package.json, on supprime les node_modules et on relance la commande `npm install`.

build: 11.0s
taille: 179MB

### Conclusion

Après ces différentes étapes d'optimisation, nous sommes passés d'une image de 1.77GB à une image de 194MB, soit une réduction de plus de 89%. Le temps de build est également passé de 77.8s à 22.2s, soit une réduction de plus de 71%.

**Tableau récapitulatif**

| Etape                             | Temps de build | Taille de l'image | Image node     |
| --------------------------------- | -------------- | ----------------- | -------------- |
| Commit initial                    | 77.8s          | 1.77GB            | Node:latest    |
| Suppression des node_modules      | 77.8s          | 1.77GB            | Node:latest    |
| Image node                        | 127s           | 953MB             | Node:24-slim   |
| Modification des COPY             | 132s           | 919MB             | Node:24-slim   |
| Suppression des RUN inutiles      | 23.8s          | 358MB             | Node:24-slim   |
| Image alpine                      | 48.3s          | 260MB             | Node:24-alpine |
| Version de node                   | 46.3s          | 194MB             | Node:16-alpine |
| Suppression des éléments inutiles | 22.2s          | 194MB             | Node:16-alpine |
| Suppression de mangoDB            | 11.0s          | 179MB             | Node:16-alpine |