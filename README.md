# 🤖 Agent IA Téléphonique — Transcription + Analyse

Ce projet est un assistant vocal simple qui utilise l’intelligence artificielle pour analyser le contenu d’un message vocal.  
Il transcrit un fichier audio (simulant un appel téléphonique) et analyse la demande du client à l’aide de l’API OpenAI (GPT-3.5).

---

## ✨ Fonctionnalités

- Transcription automatique avec [Whisper](https://github.com/openai/whisper)
- Analyse sémantique avec [OpenAI GPT-3.5 Turbo](https://platform.openai.com/)
- Détection de l’intention (support, facturation, commercial…)
- Préparation au routage automatisé (email / API / CRM)

---

## 🛠 Technologies utilisées

- Python 3.11
- Whisper (OpenAI)
- OpenAI GPT-3.5
- python-dotenv

---

## 📦 Installation

```bash
git clone https://github.com/zelermehdi/agent-ai-phone.git
cd agent-ai-phone
python -m venv venv
venv\Scripts\activate         # sous Windows
pip install -r requirements.txt
