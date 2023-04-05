import streamlit as st


title = "Modélisation des temps d'intervention des pompiers de la London Fire Brigade : une approche prédictive pour améliorer la gestion des situations d'urgence"
sidebar_name = "Classification"


def run():
    
    st.title(title)

    st.markdown("---")

    st.markdown(
        """
          Le projet que nous allons présenter porte sur l'analyse et la modélisation des temps d'intervention des pompiers de la London Fire Brigade. 
          L'objectif est de prédire le temps de réponse à partir d'un certain nombre de variables explicatives telles que la distance parcourue,
          le lieu de l'incident, le type de service spécial, le code de la ressource et le code de la station de déploiement. 
            
          Nous avons utilisé plusieurs méthodes de modélisation telles que la régression, la classification et les séries temporelles afin d'identifier la meilleure approche pour prédire les temps d'intervention. 
          Le projet a également mis en évidence les limites des données disponibles et les difficultés rencontrées lors de la modélisation. Les résultats obtenus ont des implications pratiques importantes
          pour l'amélioration des temps de réponse des pompiers et la gestion des situations d'urgence à Londres.
        """
    )
