import streamlit as st


title = "Nettoyage et sélection des données "
sidebar_name = "Traitements des données"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Pre-processing et feature engineering :")



    st.markdown(
        """
        
        Parmi les variables utilisées, il y a majoritairement des variables qualitatives. Celles-ci (Heure de l’accident, mois de l’accident , DeployedFromStation_Name, IncGeo_BoroughName, ResourceCode,  PumpOrder, SpecialServiceType ) vont être dichotomisées. 

        **Concernant la variable distance, elle va servir à créer deux variables**. 

        """
    )

    col1, col2 = st.columns([2, 2])
    with col1:
        st.image("assets/image30.png", use_column_width=True, width=300)
    with col2:
        st.markdown(
            """
            En effet, on voit sur ce graphique qui représente la relation entre le temps de réponse moyen, et la distance entre la caserne et le lieu de l’accident pour des distances comprises entre 0 et 1 km, que cette relation peut être modélisée en moyenne par deux régimes linéaires :
            un premier pour les distances comprises entre 0 et 200 m
            un second pour les distances supérieures à 200 m

            C’est pourquoi, on va créer deux variables short_distance et long_distance.
            """
        )

    st.markdown(
        """
        **La variable short_distance va prendre les valeurs suivantes** :

        0 si la distance est supérieure ou égale à 200
        distance si la distance est inférieure à 200

        La variable long_distance va prendre les valeurs suivantes : 
        distance si distance est supéieure ou égale à 200
        0 si distance est inférieure à 200

        Ainsi, ces deux variables permettent de prendre en compte partiellement ces deux régimes.

        """
    )
