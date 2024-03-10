import requests
from dotenv import dotenv_values, load_dotenv
import os
import json
import spacy
import azure.cognitiveservices.speech as speechsdk

nlp = spacy.load("en_core_web_md")

load_dotenv()

credentials = dotenv_values('envressources/keys.env')