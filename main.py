from openai import OpenAI
import os
import time
import requests
import webbrowser


def speak() -> str | int:
    while True:
        os.system("clear")
        speak = str(input("Use --help for see all commands\n\n")).lower().strip()

        if speak == "meteo":
            meteo()

        elif speak == "--help":
            help()

        elif speak == "perf":
            perf()

        elif speak == "discord":
            discord()

        elif speak == "google":
            google()

        elif speak == "ai":
            ai()

        elif speak == "quit":
            os.system("clear")
            break


def meteo() -> int | bool:

    ville = input("Ville : ")

    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": ville,
            "count": 1,
            "language": "fr",
            "format": "json"
        }
    ).json()

    lieu = geo["results"][0]

    meteo = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lieu["latitude"],
            "longitude": lieu["longitude"],
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
        }
    ).json()

    current = meteo["current"]

    print(f"\n🌍 {lieu['name']}, {lieu['country']}")
    print(f"🌡️ Température : {current['temperature_2m']} °C")
    print(f"💧 Humidité : {current['relative_humidity_2m']} %")
    print(f"💨 Vent : {current['wind_speed_10m']} km/h")
    time.sleep(3)


def help() -> str | int:
    print("""
    .1 Météo 🌪️      .4 Google 🌐

    .2 Perf 🎀       .5 AI 🤖

    .3 Discord 🔊
    """)
    time.sleep(3)


def perf() -> int | str | bool:
    os.system("fastfetch")
    time.sleep(5)

def discord():
    webbrowser.open("https://discord.com/login")


def google():
    webbrowser.open("https://www.google.com/")


def ai() -> str | int |bool:
    api=""

    question = input("Pose moi ta question ")

    client = OpenAI(
        api_key=api,
        base_url="https://api.groq.com/openai/v1",
    )

    response = client.responses.create(
        input=question,
        model="openai/gpt-oss-20b",
    )
    
    print("🤖", response.output_text)
    input("Appuyer sur entré pour continuer...")


if __name__ == "__main__":
    speak()
