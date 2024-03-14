import requests
from dotenv import dotenv_values, load_dotenv
import os
import json
import spacy
import azure.cognitiveservices.speech as speechsdk
from datetime import date, timedelta, datetime
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
import re
import pyodbc
import streamlit as st
import pandas as pd

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

load_dotenv()

credentials = dotenv_values('envressources/keys.env')
sqlvals = dotenv_values('envressources/SQLkeys.env')
key = credentials['SPEECH_KEY']
region = credentials['SPEECH_REGION']

currentime = datetime.now().strftime("%H_%M_%S")

liste_activation = ["température", "temps", "météo", "Température", "Temps", "Météo", "comment", "Comment", "Combien", "combien"]