from a_imports import *

# Fonction pour soustraire une date donnée de la date actuelle
def soustraire_dates(date_entree):
    # Convertir la chaîne de date en objet datetime
    date_entree = datetime.strptime(date_entree, "%Y-%m-%d")
    
    # Date actuelle
    date_actuelle = datetime.now()
    
    # Calculer la différence entre les deux dates
    difference = date_entree - date_actuelle
    
    # Afficher la différence en jours
    return difference.days + 2


def add_days_to_date(date_str, days):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date_obj + timedelta(days=days)
    new_date_str = new_date.strftime("%Y-%m-%d")
    return new_date_str
