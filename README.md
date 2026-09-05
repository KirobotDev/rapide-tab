🤖 Fastistance

Fastistance est un assistant personnel développé en Python.

Le projet a commencé comme un assistant CLI et évolue progressivement vers une interface graphique moderne.

🚧 Projet actuellement en développement

✨ Fonctionnalités

🌤️ Météo

Consulte la météo actuelle d'une ville :

Température
Humidité
Vitesse du vent

📊 Performances système

Affiche les informations de la machine avec fastfetch.

🎮 Discord

Ouvre rapidement Discord dans le navigateur.

🌐 Google

Ouvre rapidement Google.

🤖 Intelligence artificielle

Pose des questions à une IA directement depuis Fastistance.

🖥️ Interface graphique

Une interface graphique est actuellement en développement.

🛠️ Technologies
🐍 Python
🎨 Tkinter
🤖 OpenAI SDK
⚡ Groq API
🌤️ Open-Meteo API
🌐 Requests
💻 Fastfetch

📁 Architecture
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

🚀 Installation
1️⃣ Cloner le projet
git clone https://github.com/USERNAME/fastistance.git
cd fastistance

2️⃣ Créer l'environnement virtuel
python3 -m venv .venv

3️⃣ Activer l'environnement

Linux / macOS :

source .venv/bin/activate


Windows :

.venv\Scripts\activate

4️⃣ Installer les dépendances
python -m pip install -r requirements.txt

🔑 Configuration de l'IA

Fastistance utilise Groq pour ses fonctionnalités d'intelligence artificielle.

⚠️ Ne mets jamais ta clé API directement dans le code.

❌ À ne pas faire :

api_key = "gsk_xxxxxxxxx"


✅ Utilise plutôt une variable d'environnement :

api_key = os.environ.get("GROQ_API_KEY")


Sous Linux / macOS :

export GROQ_API_KEY="TA_CLE_API"

▶️ Lancer Fastistance

Une fois l'installation terminée :

source .venv/bin/activate
python main.py

🌤️ Météo

Fastistance utilise Open-Meteo pour récupérer les données météorologiques.

Exemple :

FASTISTANCE > meteo

Ville : Paris

🌍 Paris, France
🌡️ Température : 18 °C
💧 Humidité : 70 %
💨 Vent : 12 km/h

🤖 Intelligence artificielle

La commande IA permet de discuter avec le modèle directement depuis Fastistance.

FASTISTANCE > ai

Pose-moi ta question :

> Explique-moi Python

🤖 Python est un langage de programmation...

🗺️ Roadmap
✅ Disponible
 🌤️ Météo
 📊 Informations système
 🎮 Discord
 🌐 Google
 🤖 Intelligence artificielle
 ⌨️ Interface CLI
🔨 En développement
 🖥️ Interface graphique
 🏠 Dashboard
 📱 Sidebar
 💬 Chat IA
 ⚙️ Paramètres
 🌙 Mode sombre
 🎨 Interface moderne
🔮 Prévu
 🧠 Tool Calling
 🗣️ Assistant vocal
 🔍 Recherche Internet
 📁 Gestion des fichiers
 💻 Commandes système
 ⏱️ Timer
 📋 Historique des conversations
 🔌 Système de plugins
 🎵 Contrôle multimédia
 🔔 Notifications
🧠 Objectif

L'objectif de Fastistance est de devenir un véritable assistant personnel.

À terme, l'IA pourra comprendre les demandes de l'utilisateur et utiliser automatiquement les outils disponibles.

Utilisateur
     │
     ▼
🤖 IA
     │
     ├── 🌤️ Météo
     ├── 💻 Système
     ├── 🌐 Web
     ├── 🎮 Discord
     └── 📁 Fichiers

🔒 Sécurité

⚠️ Ne partage jamais tes clés API.

Si une clé API est publiée accidentellement :

Révoque immédiatement la clé.
Génère une nouvelle clé.
Utilise une variable d'environnement.
Ajoute .env à ton .gitignore.
.venv/
.env
__pycache__/
*.pyc

🤝 Contribution

Les contributions sont les bienvenues !

git checkout -b feature/ma-fonctionnalite


Puis :

git add .
git commit -m "Add: ma fonctionnalité"
git push origin feature/ma-fonctionnalite


Ensuite, ouvre une Pull Request.

⭐ Fastistance

Your terminal, but smarter. 🤖

🚧 Fastistance est encore en développement.

De nombreuses fonctionnalités sont prévues pour transformer progressivement le projet en un assistant personnel complet.
