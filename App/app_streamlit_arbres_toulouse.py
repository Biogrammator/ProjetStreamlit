import streamlit as st
from supabase import create_client
import pandas as pd

@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

st.title("Test Supabase")

try:
    response = (
        supabase
        .table("data_original")
        .select("*")
        .execute()
    )

    st.write("Réponse Supabase :")
    st.write(response)

    st.write("Données reçues :")
    st.write(response.data)

    df = pd.DataFrame(response.data)

    st.write("Nombre de lignes :", len(df))
    st.write("Nombre de colonnes :", len(df.columns))

    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("Erreur Supabase")
    st.exception(e)