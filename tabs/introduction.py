import streamlit as st

title = "Introduction"
sidebar_name = "Introduction"

def run():

    st.title(title)

    st.header('La brigade de pompiers de Londres :')
    st.markdown(
        """
            - Fondée en 1865
            - 113 casernes réparties sur l'ensemble de la capitale
            - ~ 150 000 appels d'urgence par année
            - Type d'interventions : incendies, inondations, collisions routières
        """
    )

    st.header('Enjeux du projet :')
    st.markdown(
        """
            - Modéliser le temps de réponse des pompiers
            - Possibilité de proposer des actions pour améliorer le temps de réponse :
                * Ouverture de nouvelles casernes
                * Allocation d'une unité à une autre caserne
        """
    )

    st.header('Méthodes utilisées')
    st.markdown(
        """
            - Analyse de données (Pandas, Matplotlib, Seaborn)
            - Modélisation du temps de réponse via des modèles de machine learning (Scikit-Learn)
        """
    )
