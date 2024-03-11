from a_imports import *

city = None

# Fonction pour traiter la requête et extraire la ville mentionnée
def process_query(query):
    doc = nlp(query)
    for entity in doc:
        if entity.get("entity_group") == "LOC":
            city_name = entity.get("word")
            return city_name.capitalize()
    return None