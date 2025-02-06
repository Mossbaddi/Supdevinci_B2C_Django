FROM python:3.8

WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Installer default-mysql-client
RUN apt update && apt install -y default-mysql-client


# Copier notre projet dans le conteneur
COPY . .

# Exposer le port 8000 ( à titre indicatif )
EXPOSE 8000

# Lancer notre application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]