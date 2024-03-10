import requests
from dotenv import dotenv_values, load_dotenv
import os
import json
import spacy
import azure.cognitiveservices.speech as speechsdk
from datetime import datetime
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

load_dotenv()

credentials = dotenv_values('envressources/keys.env')
currentdateandtime = datetime.now().strftime("%H_%M_%S")

def save_json(data, filename):
  with open(filename, 'w') as f:
    json.dump(data, f, indent=4)