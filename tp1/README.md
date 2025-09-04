## Exercice 4:
l'image nginx par défault accessible à l'url `localhost:8080` affiche **Welcome to nginx!** et un paragraphe.

## Exercice 5:
**déplacement dans le répertoire de l'app:**
cd .\flask-app

**build de l'application:**
docker build -t flask-app .

**run l'application sur le port 5000:**
docker run -d -p 5000:5000 flask-app
