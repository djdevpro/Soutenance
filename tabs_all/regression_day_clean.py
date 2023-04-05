import streamlit as st
import datetime


title = "Temps de réponse - Journalier"
sidebar_name = "Temps de réponse - Journalier"


def run():
    
    st.title(title)
    
    
    placeholder = st.empty()

    with placeholder.form(key ='Form1'):
        
        ordre = 0
        service = 0
        # if empty valid
        col1, col2 =  st.columns([1,1])
        with col1:
            st.date_input('Date de l\'incident', datetime.date(2021, 1, 1), key='date_input')
        with col2:
            st.time_input('Heure de l\'incident', datetime.time(8, 45), key='time_input')
        
        col1, col2 =  st.columns([1,1])
        with col1:    
            ordre = st.selectbox(
                'Ordre de déploiement',
                ('Premier', 'Second', 'Troisième'),
                key='ordre'
            )
        with col2:
            service = st.selectbox(
                'Type de service',
                ('Incident', 'Special Service', 'Other'),
                key='service'
            )
            
        valid = st.form_submit_button('Valider')  
    if valid:
        
        placeholder.empty()
        st.write("ordre", ordre, "service", service)
        # input bouton retour
        if st.button('Retour'):
            st.session_state.retour = False
            st.experimental_rerun()