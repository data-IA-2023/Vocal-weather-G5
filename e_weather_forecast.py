from a_imports import *
from datetime import datetime
from c_speech_translation import answertranslated
from d_speech_processing import ville, datev
from f_current_date import soustraire_dates, add_days_to_date

def get_weather_forecast():
    days = "1"
    if not ville:
        return {"message": "Je n'ai pas compris votre demande."}
    
    if datev is None:
        if "demain" in answertranslated.lower():
            days = "2"
        if "après demain" in answertranslated.lower() or "après-demain" in answertranslated.lower():
            days = "3"
    else:
        days = str(soustraire_dates(datev))

    # URL de l'API pour les prévisions météorologiques
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": ville, "days": days}
    headers = { 
        "X-RapidAPI-Key": credentials['RAPIDAPIKEY'],  # Clé d'API pour l'authentification
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"  # Hôte de l'API
    }
    # Envoi de la requête GET à l'API de prévisions météorologiques
    response = requests.get(url, headers=headers, params=querystring)
    httpstatus = int(response.status_code)

    if days == "1":
        if "location" in response.json() and "current" in response.json():
            return (response.json()["location"], response.json()["current"]), httpstatus, ville, days
        else:
            return {"message": "Les données de prévision ne sont pas disponibles."}, httpstatus, ville, days
    else :
        if "forecast" in response.json():
            forecast_data = response.json()["forecast"]["forecastday"]
            if len(forecast_data) > 0:
            
                currentdate = datetime.today().strftime('%Y-%m-%d')

                if days == "2":
                    target_date = add_days_to_date(currentdate, 1)
                elif days == "3":
                    target_date = add_days_to_date(currentdate, 2)
                elif days == "4":
                    target_date = add_days_to_date(currentdate, 3)
                else:
                    target_date = currentdate
            
                for day_data in forecast_data:
                    if day_data["date"] == target_date:
                        return day_data, httpstatus, ville, days
            
            return {"message": f"Prévisions météorologiques non disponibles pour {target_date}"}, httpstatus, ville, days
        else:
                print("Les données de prévision ne sont pas disponibles.")

    return {"message": "Les données de prévision ne sont pas disponibles."}, httpstatus, ville, days


prévision, météo_status, météo, days = get_weather_forecast()