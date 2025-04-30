import whisper
import openai
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

def analyze_text(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Tu es un assistant qui analyse les demandes clients au téléphone et redirige vers le bon service (support, commercial, facturation, etc)."
            },
            {"role": "user", "content": prompt_text}
        ]
    )
    return response.choices[0].message["content"]

AUDIO_FILE = "demo.wav"

if not os.path.exists(AUDIO_FILE):
    print("⚠️  Le fichier audio 'demo.wav' est introuvable.")
else:
    print("🎧 Transcription en cours...")
    text = transcribe_audio(AUDIO_FILE)
    print("\n📝 Texte transcrit :\n", text)

    print("\n🤖 Analyse IA en cours...")
    decision = analyze_text(text)
    print("\n📍 Résultat de l’analyse :\n", decision)
