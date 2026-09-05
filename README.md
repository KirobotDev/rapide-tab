# 🤖 Fastistance

 > **Your terminal, but smarter.**

 Fastistance est un assistant personnel développé en **Python** qui regroupe plusieurs outils utiles directement dans une seule application.

 Le projet a commencé comme un assistant **CLI** et évolue progressivement vers une **interface graphique moderne** avec intelligence artificielle.

 > 🚧 **Fastistance est actuellement en développement.**

---

 ## ✨ Features

 - 🌤️ **Weather** — Consulte la météo d'une ville.
- 🤖 **AI Assistant** — Pose des questions à une IA depuis le terminal.
- 📊 **System Info** — Affiche les informations système avec Fastfetch.
- 🎮 **Discord** — Ouvre Discord rapidement.
- 🌐 **Google** — Ouvre Google rapidement.
- 🖥️ **GUI** — Interface graphique actuellement en développement.
- ⚡ **Fast & Lightweight** — Simple, rapide et facilement extensible.

---

 ## 🖥️ Preview

 ### CLI

```
╔══════════════════════════════════╗
║          FASTISTANCE             ║
╠══════════════════════════════════╣
║                                  ║
║  🌤️  meteo                       ║
║  📊  perf                        ║
║  🎮  discord                     ║
║  🌐  google                      ║
║  🤖  ai                          ║
║                                  ║
║  🚪  quit                        ║
║                                  ║
╚══════════════════════════════════╝

FASTISTANCE >
```

 ### 🌤️ Weather

```
FASTISTANCE > meteo

Ville : Paris

🌍 Paris, France
🌡️ Température : 18 °C
💧 Humidité : 70 %
💨 Vent : 12 km/h
```

 ### 🤖 AI

```
FASTISTANCE > ai

Pose-moi ta question : Explique-moi Python

🤖 Python est un langage de programmation...
```

---

 ## 🛠️ Technologies

 Fastistance utilise actuellement :

 - 🐍 **Python 3**
- 🤖 **OpenAI Python SDK**
- ⚡ **Groq API**
- 🌤️ **Open-Meteo API**
- 🌐 **Requests**
- 💻 **Fastfetch**
- 🖥️ **Tkinter** _(GUI en développement)_

---

 ## 📁 Project Structure

```
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
```

 ### 📄 Files

 | File | Description |
| --- | --- |
| `main.py` | Point d'entrée de l'application |
| `app/gui.py` | Interface graphique |
| `app/ai.py` | Gestion de l'intelligence artificielle |
| `app/meteo.py` | Gestion de la météo |
| `app/system.py` | Informations système |
| `app/utils.py` | Fonctions utilitaires |
| `requirements.txt` | Dépendances Python |
| `.gitignore` | Fichiers ignorés par Git |

---

 # 🚀 Installation

 ## Requirements

 Avant de commencer, assure-toi d'avoir :

 - **Python 3.10+**
- **Git**
- **Fastfetch** _(optionnel pour la fonction performances)_

---

 ## 1\. Clone the repository

```
git clone https://github.com/USERNAME/fastistance.git
cd fastistance
```

 Remplace `USERNAME` par ton nom d'utilisateur GitHub.

---

 ## 2\. Create a virtual environment

```
python3 -m venv .venv
```

---

 ## 3\. Activate the virtual environment

 ### Linux / macOS

```
source .venv/bin/activate
```

 ### Windows

```
.venv\Scripts\activate
```

---

 ## 4\. Install dependencies

```
python -m pip install -r requirements.txt
```

---

 # 🔑 API Configuration

 Fastistance utilise **Groq** pour les fonctionnalités d'intelligence artificielle.

 ### ⚠️ Important

 **Ne mets jamais ta clé API directement dans ton code.**

 ❌ Ne fais pas :

```
api_key = "gsk_xxxxxxxxxxxxxxxxx"
```

 Utilise une variable d'environnement :

```
api_key = os.environ.get("GROQ_API_KEY")
```

 ### Linux / macOS

```
export GROQ_API_KEY="YOUR_API_KEY"
```

 ### Windows PowerShell

```
$env:GROQ_API_KEY="YOUR_API_KEY"
```

---

 # ▶️ Run

 Une fois l'installation terminée :

```
python main.py
```

 Fastistance devrait maintenant démarrer.

---

 # 🌤️ Weather

 La fonctionnalité météo utilise l'API **Open-Meteo**.

 Aucune clé API n'est nécessaire.

 Exemple :

```
Ville : Lyon

🌍 Lyon, France
🌡️ Température : 19 °C
💧 Humidité : 65 %
💨 Vent : 10 km/h
```

---

 # 📊 System Information

 Fastistance utilise **Fastfetch** pour afficher les informations de la machine.

 ### Debian / Ubuntu

```
sudo apt install fastfetch
```

 Puis utilise :

```
FASTISTANCE > perf
```

---

 # 🤖 AI Assistant

 Fastistance permet d'utiliser une intelligence artificielle directement depuis le terminal.

 Exemple :

```
FASTISTANCE > ai

Pose-moi ta question : Quelle est la différence entre Python et C++ ?

🤖 ...
```

 L'IA utilise l'API Groq avec le SDK Python compatible OpenAI.

---

 # 🖥️ Graphical Interface

 Une interface graphique est actuellement en développement.

 L'objectif est de remplacer progressivement l'interface CLI par une application avec :

```
┌─────────────────────────────────────────────────────────┐
│ 🤖 FASTISTANCE                              ⚙️          │
├──────────────┬──────────────────────────────────────────┤
│              │                                          │
│ 🏠 Home      │          Welcome to Fastistance          │
│              │                                          │
│ 🌤️ Weather   │   ┌────────┐ ┌────────┐ ┌────────┐     │
│              │   │ 🌤️     │ │ 📊     │ │ 🤖     │     │
│ 📊 System    │   │ Weather│ │ System │ │ AI     │     │
│              │   └────────┘ └────────┘ └────────┘     │
│ 🎮 Discord   │                                          │
│              │   ┌────────┐ ┌────────┐                 │
│ 🌐 Google    │   │ 🎮     │ │ 🌐     │                 │
│              │   │Discord │ │Google  │                 │
│ 🤖 AI        │   └────────┘ └────────┘                 │
│              │                                          │
│ ⚙️ Settings  │                                          │
│              │                                          │
└──────────────┴──────────────────────────────────────────┘
```

---

 # 🗺️ Roadmap

 ## ✅ Completed

 - [x] 🌤️ Weather
- [x] 📊 System information
- [x] 🎮 Discord integration
- [x] 🌐 Google integration
- [x] 🤖 AI assistant
- [x] ⌨️ CLI interface

 ## 🔨 In Progress

 - [ ] 🖥️ Graphical interface
- [ ] 🏠 Dashboard
- [ ] 📱 Sidebar navigation
- [ ] 💬 AI chat interface
- [ ] ⚙️ Settings
- [ ] 🌙 Dark mode
- [ ] 🎨 Modern UI

 ## 🔮 Planned

 - [ ] 🧠 AI Tool Calling
- [ ] 🗣️ Voice assistant
- [ ] 🔍 Internet search
- [ ] 📁 File management
- [ ] 💻 System commands
- [ ] ⏱️ Timer
- [ ] 📋 Conversation history
- [ ] 🔌 Plugin system
- [ ] 🎵 Media controls
- [ ] 🔔 Notifications
- [ ] 🧩 Extensions

---

 # 🧠 Future Architecture

 L'objectif est de faire de Fastistance un véritable assistant personnel capable de comprendre les demandes de l'utilisateur et d'utiliser automatiquement les outils disponibles.

```
                         ┌─────────────────┐
                         │   FASTISTANCE   │
                         └────────┬────────┘
                                  │
                         ┌────────▼────────┐
                         │   GUI / CLI     │
                         └────────┬────────┘
                                  │
                         ┌────────▼────────┐
                         │   AI ENGINE     │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
         ┌────▼────┐         ┌────▼────┐         ┌────▼────┐
         │ Weather │         │ System  │         │   Web   │
         └─────────┘         └─────────┘         └─────────┘
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                           ┌──────▼──────┐
                           │    Tools    │
                           └─────────────┘
```

 À terme, l'utilisateur pourra simplement demander :

```
"Quelle est la météo à Paris ?"
```

 L'IA pourra alors détecter automatiquement qu'elle doit utiliser l'outil météo.

```
User
 │
 ▼
🤖 AI
 │
 ▼
🌤️ Weather Tool
 │
 ▼
Paris → 18°C
```

---

 # 🔒 Security

 **Ne partage jamais tes clés API.**

 Si une clé est accidentellement publiée :

 1. Révoque immédiatement la clé.
2. Génère une nouvelle clé.
3. Utilise une variable d'environnement.
4. Ne commit jamais `.env` ou une clé dans Git.

 Exemple de `.gitignore` :

```
.venv/
.env
__pycache__/
*.pyc
```

---

 # 🤝 Contributing

 Les contributions sont les bienvenues !

 ### 1\. Fork

 Fork le repository sur GitHub.

 ### 2\. Create a branch

```
git checkout -b feature/my-feature
```

 ### 3\. Make your changes

 Développe ta fonctionnalité.

 ### 4\. Commit

```
git add .
git commit -m "Add: my feature"
```

 ### 5\. Push

```
git push origin feature/my-feature
```

 ### 6\. Pull Request

 Ouvre ensuite une **Pull Request** sur GitHub.

---

 # 📜 License

 Ce projet est actuellement en développement.

 La licence sera ajoutée ultérieurement.

---

 # ⭐ Support

 Si tu apprécies le projet, pense à lui laisser une ⭐ sur GitHub !

---

 \<div align="center"\> **Fastistance**

 _Your terminal, but smarter. 🤖_

 Made with ❤️ and Python 🐍

 \</div\>
