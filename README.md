# Optimisation d'Itinéraire

---

## Description
Ce projet vise à développer une application permettant aux utilisateurs de planifier des trajets optimisés en fonction de différents critères tels que la distance, le temps et les points d'intérêt. Le projet utilise Flask pour le backend, SQLAlchemy pour la gestion de la base de données et SQLite comme SGBD.

## Fonctionnalités
- Création et gestion des utilisateurs
- Planification d'itinéraires personnalisés
- Ajout de points d'arrêt (BreakPoints) aux itinéraires
- Optimisation des itinéraires selon des critères spécifiques

## Technologies Utilisées
- Flask
- SQLAlchemy
- SQLite
- Python

## Prérequis
- Python 3.x
- Flask
- SQLAlchemy
- Werkzeug

## Installation

### 1. Clonez le dépôt

        sh
        git clone https://github.com/bechirousmane/Optimization_Itinerary.git

 ### Accédez au répertoire du projet

        sh
        cd Optimisation_Itineraire

## Créez un environnement virtuel

        sh
        python3 -m venv venv

Activez l'environnement virtuel

Sur macOS/Linux

        sh
        source venv/bin/activate

Sur Windows

        sh
        venv\Scripts\activate

## Installez les dépendances

        sh
        pip install -r requirements.txt

## Configuration

Assurez-vous que le fichier config.py contient les configurations appropriées pour votre base de données.

### Definissez vos variables d'environnement 

#### 1. Sur macOS et Linux
Pour une session de terminal (temporaire)

Ouvrez un terminal et exécutez les commandes suivantes :

        sh
        export DATABASE_URL='URL de votre base de donnée'
        export GOOGLE_MAPS_API_KEY='votre clé de l'api google maps'

#### 2. Sur Windows
Pour une session de commande (temporaire)

Ouvrez une invite de commandes et exécutez les commandes suivantes :

        sh
        set DATABASE_URL='URL de votre base de donnée'
        set GOOGLE_MAPS_API_KEY='votre clé de l'api google maps'


## Utilisation
...

---

## Contribution

Les contributions sont les bienvenues. Veuillez soumettre une pull request pour les fonctionnalités majeures ou ouvrir un problème pour discuter des changements que vous souhaitez apporter.

## License
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Auteurs
    Bechir Ousmane

## Contact

    Email: obechir06@gmail.com
    

