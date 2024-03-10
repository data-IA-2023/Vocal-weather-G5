from a_imports import *
from b_speech_recognition import recognize_from_microphone

# Définition de la fonction pour traduire le texte provenant du microphone
def translate_from_microphone():
    # URL de l'API de traduction
    url_translate = "https://translate281.p.rapidapi.com/"
    
    # Appel de la fonction pour reconnaître le texte à partir du microphone
    answer = recognize_from_microphone()

    # Données à envoyer à l'API de traduction
    payload = {
        "text": answer,  # Texte à traduire
        "from": "auto",  # Langue source automatiquement détectée
        "to": "fr"   # Traduction 
    }
    
    # En-têtes pour la requête HTTP
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": credentials['TRANSLATE_API_KEY'],  # Clé d'API pour l'authentification
        "X-RapidAPI-Host": "translate281.p.rapidapi.com"      # Hôte de l'API
    }

    # Envoi de la requête POST à l'API de traduction
    response = requests.post(url_translate, data=payload, headers=headers)

    # Analyse de la réponse JSON
    translation_result = response.json()
    
    # Récupération du texte traduit de la réponse
    translated_text = translation_result.get('response', answer)
    
    # Retourne le texte traduit
    print(f"TEXTE TRADUIT = {translated_text}")
    return translated_text

