# Utiliser une image de base Python 3.9
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande par défaut pour exécuter l'application
CMD ["python", "app.py"]
