from a_imports import *

city = None

def process_query_and_transform_dates(query):
    doc = nlp(query)
    city_name = None
    date_name = None
    for entity in doc:
        if entity.get("entity_group") == "LOC":
            city_name = entity.get("word").capitalize()
        if entity.get("entity_group") == "DATE":
            date_name = entity.get("word").capitalize()

    def format_date(match):
        jour = match.group(1)
        mois = match.group(2)
        annee = match.group(3)

        mois_dict = {
            'janvier': '01',
            'février': '02',
            'mars': '03',
            'avril': '04',
            'mai': '05',
            'juin': '06',
            'juillet': '07',
            'août': '08',
            'septembre': '09',
            'octobre': '10',
            'novembre': '11',
            'décembre': '12'
        }

        mois_num = mois_dict[mois.lower()]
        formatted_date = f"{annee}-{mois_num}-{jour}"
        return formatted_date

    def transformer_dates(chaine):
        regex_date = re.compile(r'Le (\d{1,2})\s+(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s+(\d{4}) à')
        dates_trouvees = regex_date.findall(chaine)

        if not dates_trouvees:
            return None

        chaine_formatee = regex_date.sub(format_date, chaine)
        return chaine_formatee

    return city_name, transformer_dates(query)