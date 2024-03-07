import os
import requests
import json
from dotenv import dotenv_values, load_dotenv
import spacy
from speech_recognition import *

nlp = spacy.load("fr_core_news_md")

load_dotenv()
credentials = dotenv_values('envressources/keys.env')

réponse = recognize_from_microphone()

def process_query(query):
    doc = nlp(query)
    for entity in doc.ents:
        if entity.label_ == "GPE" or entity.label_ == "LOC": # Geopolitical entities
            city_name = entity.text
            return city_name.capitalize()  # Retourne le nom de la ville
    return None 

query = réponse
city = None
liste_activation = ["Météo", "temps"]

# Vérifie si l'un des mots de la liste_activation est présent dans la phrase
for word in liste_activation:
    if word in query:
        city = process_query(query)
        break

if city:
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": city, "days": "3"}
    headers = {
        "X-RapidAPI-Key": credentials['METEO_API_KEY'],
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())
else:
    print("Je n'ai pas compris votre demande..")
