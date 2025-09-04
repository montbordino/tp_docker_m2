# Utiliser une image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY app.py /app

# Installer Flask
RUN pip install flask

# Exposer le port utilisé par Flask
EXPOSE 5000

# Lancer l’application
CMD ["python", "app.py"]
