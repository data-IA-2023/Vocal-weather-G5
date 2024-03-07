from speech_recognition import *
from imports import *

def translate_from_microphone(credentials):
    url_translate = "https://translate281.p.rapidapi.com/"
    answer = recognize_from_microphone()

    payload = {
        "text": answer,
        "from": "auto",
        "to": "en"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": credentials['TRANSLATE_API_KEY'],
        "X-RapidAPI-Host": "translate281.p.rapidapi.com"
    }

    response = requests.post(url_translate, data=payload, headers=headers)

    translation_result = response.json()
    translated_text = translation_result.get('response', None)
    return translated_text

translation_response = translate_from_microphone(credentials)
print(translation_response)
