from a_imports import *
from b_speech_recognition import answer
from c_speech_translation import answertranslated, status_translate
from d_speech_processing import ville, datev, ville_score, datev_score
from e_weather_forecast import météo, météo_status, prévision, days
from g_bdd_connection import insert_data

st.set_page_config(
        page_title= "Vocal - Weather",
        page_icon= "🌈"
)

st.markdown("<h1 style='text-align: center;'>🌦️Prévision météo sur 3 jours !🌦️</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Cliquez sur le bouton ci-dessous et demandez la météo de vive voix !</h2>", unsafe_allow_html=True)
st.write("")
st.markdown("---")

if st.button('Cliquez ici'):
   insert_data(answer, answertranslated, status_translate, ville, ville_score, datev, datev_score, météo, météo_status)

   if days == "1":
      df = pd.DataFrame(prévision)
      st.write(f"Il fait actuellement {df["temp_c"][1]} °C ressentit {df["feelslike_c"][1]} °C")
      st.dataframe(df)
   else:
      df = pd.Series(prévision)
      st.write(f"Voici les prévisions météos pour {ville} le {datev}")
      st.dataframe(df["day"])