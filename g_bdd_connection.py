from a_imports import *
import pyodbc

"""
Connects to a SQL database using pyodbc
"""

def insert_data(answer, answertranslated, status_translate, ville, ville_score, datev, datev_score, météo, météo_status):
    # Construct the connection string
    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={sqlvals['SERVER']};DATABASE={sqlvals['DATABASE']};UID={sqlvals['USERNAME']};PWD={sqlvals['PASSWORD']}'
    
    # Connect to the database
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()

    # Define the SQL query
    SQL_QUERY = """
        INSERT INTO dbo.clementtable (
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

    # Execute the query
    cursor.execute(
        SQL_QUERY,
        answer, answertranslated, status_translate, ville, float(ville_score), datev, float(datev_score), météo, météo_status
    )

    # Commit changes and close connection
    conn.commit()
    conn.close()
