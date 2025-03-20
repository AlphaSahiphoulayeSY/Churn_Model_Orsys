# Utilise l'image Python officielle comme image de base
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt requirements.txt

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code de l'application Flask dans le conteneur
COPY . .

# Expose le port sur lequel l'application Flask sera exécutée
EXPOSE 5012

# Définit la commande pour exécuter l'application Flask
CMD ["python", "app.py"]
