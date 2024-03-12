from a_imports import *
from c_speech_translation import translate_from_microphone
from d_speech_processing import process_query_and_transform_dates
from f_current_date import soustraire_dates

query = translate_from_microphone()

def get_weather_forecast():
    city, datev = process_query_and_transform_dates(query)
    print(datev)
    days = "1"
    if not city:
        return {"message": "Je n'ai pas compris votre demande."}
    
    if datev is None:
        if "demain" in query.lower():
            days = "2"
        if "après-demain" in query.lower():
            days = "3"
    else:
        days = str(soustraire_dates(date))

    # URL de l'API pour les prévisions météorologiques
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": city, "days": days}
    print(days)
    headers = { 
        "X-RapidAPI-Key": credentials['RAPIDAPIKEY'],  # Clé d'API pour l'authentification
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"  # Hôte de l'API
    }
    # Envoi de la requête GET à l'API de prévisions météorologiques
    response = requests.get(url, headers=headers, params=querystring)
    save_json(response.json(), f"meteos/{currentime}_{city}.json")
    if "current" in response.json():
        current_data = response.json()["current"]
        if "temp_c" in current_data and "last_updated" in current_data:
            print("Température en Celsius: ", current_data["temp_c"])
            print("Date précise du relevé météo:", current_data["last_updated"])
    if "location" in response.json():
        location_data = response.json()["location"]
        if "name" in location_data and "lat" in location_data and "lon" in location_data:
            print("Ville : ", location_data["name"])
            print("Latitude : ", location_data["lat"])
            print("Longitude : ", location_data["lon"])
    else:
        print("Les données actuelles ne sont pas disponibles.")