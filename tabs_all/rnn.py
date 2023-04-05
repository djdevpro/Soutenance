import streamlit as st


title = "Série temporelle avec RNN univarié"
sidebar_name = "Série temporelle avec RNN univarié"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Description du process :")

    st.markdown(
        """
        L'idée principale derrière l'utilisation du modèle RNN est de détecter et d'analyser toute saisonnalité qui n'a pas été mise en évidence par SARIMAX. Pour ce faire, nous avons mis en place un réseau de neurones récurrents simple pour l'analyse univariée, en utilisant un ensemble de 40 données pour prédire le temps médian d'une journée. 
        """
    )

    
    st.image("assets/image26.png", use_column_width=True, width=300)

    st.markdown("###   Interprétation des résultats : ")

    st.markdown(
        """
        Le résultat de la modélisation est présenté graphiquement ci-dessous.
        """
    )
    
    st.image("assets/image7.png", use_column_width=True, width=300)

    st.markdown(
        """
        En ce qui concerne les scores, nous avons obtenu un résultat plus intéressant que SARIMAX, bien que ce dernier reste insuffisant : 
        """
    )
    
    st.image("assets/image2.png", use_column_width=True, width=300)

    st.markdown(
        """
        En mettant en œuvre successivement un modèle SARIMAX et un RNN pour prédire une série chronologique complexe telle que celle que nous avons étudiée, nous avons pu constater à la fois les limites et les opportunités d'amélioration de ces méthodes de prédiction. Une autre option consiste à utiliser un modèle RNN multivarié, qui tient compte d'autres variables explicatives pour saisir la saisonnalité des données. Nous sommes convaincus qu'avec une échéance plus longue, nous pourrions mieux comprendre le domaine et affiner notre choix de caractéristiques susceptibles d'influencer le temps de réponse des pompiers, ce qui nous permettrait de faire des prédictions plus précises.
        """
    )
