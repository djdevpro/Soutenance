import streamlit as st

with open("tabs/html/cover/credentials.html", "r", encoding="utf-8") as f:
    intro_credentials = f.read()

title = "Temps de Réponse de la Brigade des Pompiers de Londres"
sidebar_name = "Page de garde"

def run():
    
    st.image("./assets/presentation_image.png")
    st.title(title)

    st.markdown(intro_credentials,unsafe_allow_html= True)
