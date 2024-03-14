from a_imports import *
from c_speech_translation import answertranslated
from d_speech_processing import ville, datev
from f_current_date import soustraire_dates


def get_weather_forecast():
    days = "1"
    if not ville:
        return {"message": "Je n'ai pas compris votre demande."}
    
    if datev is None:
        if "demain" in answertranslated.lower():
            days = "2"
        if "après demain" in answertranslated.lower():
            days = "3"
    else:
        days = str(soustraire_dates(datev))

    # URL de l'API pour les prévisions météorologiques
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": ville, "days": days}
    print(days)
    headers = { 
        "X-RapidAPI-Key": credentials['RAPIDAPIKEY'],  # Clé d'API pour l'authentification
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"  # Hôte de l'API
    }
    # Envoi de la requête GET à l'API de prévisions météorologiques
    response = requests.get(url, headers=headers, params=querystring)
    httpstatus = int(response.status_code)

    save_json(response.json(), f"meteos/{currentime}_{ville}.json")
    if "current" in response.json():
        current_data = response.json()["current"]
        if "last_updated" in current_data:
            print("ok")
            return current_data["last_updated"], httpstatus
    else:
        print("Les données actuelles ne sont pas disponibles.")

météo, météo_status = get_weather_forecast()