from a_imports import *
from b_speech_recognition import recognize_from_microphone

def translate_from_microphone():
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"
    answer = recognize_from_microphone()

    payload = {
        "from": "auto",
        "to": "fr",
        "text": answer
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": credentials['RAPIDAPIKEY'],
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    
    if response.status_code == 200:
        translation_result = response.json()
        if "trans" in translation_result:
            return translation_result["trans"]
        else:
            return "Erreur lors de la traduction."
    else:
        print("Défaillance générale du merdier")
        return answer