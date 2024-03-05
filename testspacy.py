import spacy

nlp = spacy.load("fr_core_news_md")

# Process whole documents
text = ("Quel temps fera-t-il demain à Blois ?")
doc = nlp(text)

# Analyze syntax
print("Props:", [token.lemma_ for token in doc if token.pos_ == "PROPS"])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "AUX"])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "ADP"])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "PROPN"])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "NOUN"])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "ADP"])
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)