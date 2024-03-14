from a_imports import *
from b_speech_recognition import answer
from c_speech_translation import answertranslated, status_translate
from d_speech_processing import ville, datev, ville_score, datev_score
from e_weather_forecast import météo, météo_status

"""
Connects to a SQL database using pyodbc
"""

SERVER = sqlvals['SERVER']
DATABASE = sqlvals['DATABASE']
USERNAME = sqlvals['USERNAME']
PASSWORD = sqlvals['PASSWORD']

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString) 
cursor = conn.cursor()


SQL_QUERY = """
    INSERT into dbo.clementtable (
    TIMESTAMP, 
    PROMPT_STT, 
    TRADUCTION,
    STATUT_REQUETE,
    NLP_CITY,
    SCORE_CITY,
    NLP_DATE,
    SCORE_DATE,
    METEO,
    STATUT_REQUETE_METEO    
    ) OUTPUT INSERTED.ID
    VALUES (CURRENT_TIMESTAMP,?,?,?,?,?,?,?,?,?);
    """


cursor.execute(
    SQL_QUERY,
    answer, answertranslated, status_translate, ville, float(ville_score), datev, float(datev_score), météo, météo_status
)

conn.commit()
conn.close()
