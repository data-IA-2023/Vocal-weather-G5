import os
import azure.cognitiveservices.speech as speechsdk
import requests
import json
from dotenv import dotenv_values, load_dotenv
import spacy

nlp = spacy.load("fr_core_news_md")

load_dotenv()

# Environment files
credentials = dotenv_values('envressources/keys.env')
meteoapi = dotenv_values('')

key = credentials['SPEECH_KEY']
region = credentials['SPEECH_REGION']
langue = credentials['AZURE_SPEECH_LANG']

def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
    speech_config.speech_recognition_language=langue

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("PARLE : ")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

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
liste_activation = ["météo", "temps"]

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
