🤖 Fastistance

Fastistance est un assistant personnel développé en Python, conçu pour regrouper plusieurs outils utiles dans une seule application.

Le projet a commencé comme une application CLI (terminal) et évolue progressivement vers une interface graphique moderne.

🚧 Projet en développement

✨ Fonctionnalités

Fastistance propose actuellement plusieurs fonctionnalités :

🌤️ Météo

Recherche d'une ville
Température actuelle
Humidité
Vitesse du vent

📊 Performances système

Informations de la machine avec fastfetch

🎮 Discord

Ouverture rapide de Discord

🌐 Google

Ouverture rapide de Google

🤖 Intelligence artificielle

Pose de questions à une IA directement depuis Fastistance
Utilisation de l'API Groq avec une interface compatible OpenAI

🖥️ Interface graphique

Navigation avec une sidebar
Pages dédiées aux différentes fonctionnalités
Interface destinée à remplacer progressivement le terminal
🖥️ Architecture graphique

L'objectif de Fastistance est de proposer une interface similaire à :

┌──────────────────────────────────────────────────────────────┐
│  🤖 FASTISTANCE                              ⚙️              │
├───────────────┬──────────────────────────────────────────────┤
│               │                                              │
│  🏠 Accueil   │       Bienvenue sur Fastistance              │
│               │                                              │
│  🌤️ Météo     │   ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│               │   │ 🌤️       │ │ 📊       │ │ 🤖       │   │
│  📊 Perform.  │   │ Météo    │ │ Système  │ │ IA       │   │
│               │   └──────────┘ └──────────┘ └──────────┘   │
│  🎮 Discord   │                                              │
│               │   ┌──────────┐ ┌──────────┐                 │
│  🌐 Google    │   │ 🎮       │ │ 🌐       │                 │
│               │   │ Discord  │ │ Google   │                 │
│  🤖 IA        │   └──────────┘ └──────────┘                 │
│               │                                              │
│  ⚙️ Paramètres│                                              │
│               │                                              │
└───────────────┴──────────────────────────────────────────────┘

📁 Structure du projet

Le projet est organisé pour séparer l'interface graphique de la logique de chaque fonctionnalité.

fastistance/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── app/
│   ├── __init__.py
│   ├── gui.py
│   ├── ai.py
│   ├── meteo.py
│   ├── system.py
│   └── utils.py
│
└── .venv/

Description
Fichier	Rôle
main.py	Point d'entrée de l'application
app/gui.py	Interface graphique
app/ai.py	Gestion de l'intelligence artificielle
app/meteo.py	Gestion de la météo
app/system.py	Informations système
app/utils.py	Fonctions utilitaires
requirements.txt	Dépendances Python
.gitignore	Fichiers ignorés par Git
🛠️ Technologies

Fastistance utilise principalement :

🐍 Python
🎨 Tkinter pour l'interface graphique
🤖 OpenAI Python SDK
⚡ Groq API
🌤️ Open-Meteo API
🌐 Requests
💻 Fastfetch
📦 Installation
1. Cloner le projet
git clone https://github.com/USERNAME/fastistance.git
cd fastistance


Remplace USERNAME par ton nom d'utilisateur GitHub.

2. Créer un environnement virtuel
python3 -m venv .venv

3. Activer l'environnement virtuel
Linux / macOS
source .venv/bin/activate

Windows
.venv\Scripts\activate

4. Installer les dépendances
python -m pip install -r requirements.txt

🔑 Configuration de l'IA

Fastistance utilise l'API Groq pour les fonctionnalités d'intelligence artificielle.

⚠️ Sécurité

Ne mets jamais ta clé API directement dans ton code.

❌ Mauvais :

api_key = "gsk_xxxxxxxxx"


✅ Recommandé :

api_key = os.environ.get("GROQ_API_KEY")

Linux / macOS

Définis ta clé API :

export GROQ_API_KEY="TA_CLE_API"


Puis lance l'application :

python main.py


Pour une configuration permanente avec zsh, tu peux ajouter la variable dans :

~/.zshrc


Puis :

source ~/.zshrc

🤖 IA

Fastistance utilise le SDK Python compatible avec l'API OpenAI pour communiquer avec Groq.

Exemple :

from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

response = client.responses.create(
    model="openai/gpt-oss-20b",
    input="Bonjour Fastistance !"
)

print(response.output_text)

🌤️ Météo

La fonctionnalité météo utilise Open-Meteo.

L'utilisateur peut entrer une ville :

Ville : Paris


Fastistance récupère ensuite :

🌍 Paris, France
🌡️ Température : 18 °C
💧 Humidité : 70 %
💨 Vent : 12 km/h


Aucune clé API n'est nécessaire pour Open-Meteo.

📊 Performances

Fastistance peut utiliser fastfetch pour afficher les informations système.

Installation sur Debian / Ubuntu :

sudo apt install fastfetch


Puis :

fastfetch

🚀 Lancement

Une fois l'environnement configuré :

source .venv/bin/activate
python main.py

🗺️ Roadmap
✅ Déjà disponible
 🌤️ Météo
 📊 Informations système
 🎮 Ouverture de Discord
 🌐 Ouverture de Google
 🤖 Intelligence artificielle
 ⌨️ Version CLI
🔨 En développement
 🖥️ Interface graphique
 🏠 Dashboard
 📱 Sidebar
 💬 Interface de chat IA
 ⚙️ Page de paramètres
 🌙 Mode sombre
 🎨 Interface plus moderne
🔮 Futures fonctionnalités
 🧠 Tool Calling
 🗣️ Assistant vocal
 🔍 Recherche Internet
 📁 Gestion des fichiers
 💻 Exécution de commandes système
 ⏱️ Timer
 📋 Historique des conversations
 🔌 Système de plugins
 🎵 Contrôle multimédia
 🔔 Notifications
 🧩 Extensions
🧠 Architecture prévue

L'objectif à long terme est de transformer Fastistance en un véritable assistant personnel.

                         ┌─────────────────┐
                         │   FASTISTANCE   │
                         └────────┬────────┘
                                  │
                         ┌────────▼────────┐
                         │   Interface GUI │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
        ┌─────▼─────┐       ┌─────▼─────┐       ┌────▼─────┐
        │  Météo    │       │    IA     │       │ Système  │
        └───────────┘       └─────┬─────┘       └──────────┘
                                  │
                            ┌─────▼─────┐
                            │   Groq    │
                            └───────────┘


À terme, l'IA pourra comprendre une demande et choisir automatiquement l'outil approprié.

Par exemple :

Utilisateur :
"Quelle est la météo à Paris ?"

              ↓

            🤖 IA

              ↓

          🌤️ METEO()

              ↓

       Paris : 18 °C


Ou :

Utilisateur :
"Ouvre Discord"

              ↓

            🤖 IA

              ↓

        🎮 DISCORD()

              ↓

       Discord ouvert

🔒 Sécurité

Les clés API et informations sensibles ne doivent jamais être envoyées sur GitHub.

Le fichier .gitignore doit notamment contenir :

.venv/
.env
__pycache__/
*.pyc


Si une clé API est accidentellement publiée, elle doit être révoquée immédiatement.

🤝 Contribution

Les contributions sont les bienvenues.

1. Fork le projet
2. Crée une branche
git checkout -b feature/ma-fonctionnalite

3. Fais tes modifications
4. Commit
git add .
git commit -m "Add: ma nouvelle fonctionnalité"

5. Push
git push origin feature/ma-fonctionnalite

6. Ouvre une Pull Request
📜 Licence

Ce projet est actuellement en développement.

La licence sera définie ultérieurement.

⭐ Fastistance

Your terminal, but smarter. 🤖

Fastistance a pour objectif de devenir un assistant personnel simple, rapide et personnalisable directement depuis ton ordinateur.
