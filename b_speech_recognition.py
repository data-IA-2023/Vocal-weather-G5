from a_imports import *

def recognize_from_microphone():
    # Configuration de la reconnaissance vocale avec la clé d'abonnement et la région spécifiées
    speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
    # Configuration de la détection automatique de la langue source
    auto_detect_source_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["fr-FR","es-ES","it-IT","en-US"])

    # Configuration audio pour utiliser le microphone par défaut
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    # Création du reconnaisseur vocal
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        auto_detect_source_language_config=auto_detect_source_language_config,
        audio_config=audio_config
    )

    # Demande à l'utilisateur de parler
    print("Parlez: ")
    # Reconnaissance vocale d'un seul segment audio
    result = speech_recognizer.recognize_once()
    # Résultat de la détection automatique de la langue source
    auto_detect_source_language_result = speechsdk.AutoDetectSourceLanguageResult(result)
    # Langue détectée
    detected_language = auto_detect_source_language_result.language

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text 
    elif result.reason == speechsdk.ResultReason.NoMatch:
        # Si aucune correspondance n'est trouvée
        print("Non reconnu: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        # Si la détection est annulée
        cancellation_details = result.cancellation_details
        print("Détection annulée: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            # En cas d'erreur
            print("Détails de l'erreur: {}".format(cancellation_details.error_details))
            print("Vérifiez la clé ou la région")

answer = recognize_from_microphone()