from a_imports import *
from c_speech_translation import translate_from_microphone

query = translate_from_microphone()
city = None
liste_activation = ["weather", "Weather"]

# Fonction pour traiter la requête et extraire la ville mentionnée
def process_query(query):
    doc = nlp(query)
    for entity in doc.ents:
        if entity.label_ == "GPE" or entity.label_ == "LOC": # Entités géopolitiques ou localisations
            city_name = entity.text
            return city_name.capitalize()
    return None

# Fonction pour obtenir les prévisions météorologiques
def get_weather_forecast():
    city = None
    for word in liste_activation:
        if word in query:
            city = process_query(query)
            break

    if city:
        # URL de l'API pour les prévisions météorologiques
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
        querystring = {"q": city, "days": "0"}
        headers = {
            "X-RapidAPI-Key": credentials['METEO_API_KEY'],  # Clé d'API pour l'authentification
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"  # Hôte de l'API
        }

        # Envoi de la requête GET à l'API de prévisions météorologiques
        response = requests.get(url, headers=headers, params=querystring)
        return response.json()
    else:
        # Si la ville n'est pas spécifiée dans la requête
        return {"message": "Je n'ai pas compris votre demande.."}