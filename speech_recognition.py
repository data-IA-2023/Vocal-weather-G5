import os
import azure.cognitiveservices.speech as speechsdk
from imports import *

key = credentials['SPEECH_KEY']
region = credentials['SPEECH_REGION']

def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
    auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["fr-FR","es-ES","it-IT","en-US"])

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        auto_detect_source_language_config=auto_detect_source_language_config,
        audio_config=audio_config
    )

    print("Parlez: ")
    result = speech_recognizer.recognize_once()
    auto_detect_source_language_result = speechsdk.AutoDetectSourceLanguageResult(result)
    detected_language = auto_detect_source_language_result.language

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Phrase: {}".format(result.text))
        print("langue detectée: {}".format(detected_language))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("Non reconnu: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Détection annulée: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Détails de l'erreur: {}".format(cancellation_details.error_details))
            print("Vérifiez clé ou région")