import streamlit as st


title = "Temps de Réponse de la Brigade des Pompiers de Londres"
sidebar_name = "Volumétrie du jeu de données"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Description de la volumétrie du jeu de données.")
    #image22.png
    st.markdown(
        """
         **Incident** : Ce jeu de données renseigne un nombre total de 333.471 observations en 39 colonnes et couvre une période de trois ans soit de janvier 2020 à Décembre 2022. Les informations contenues dans cette base comprennent tous les appels passés au LFB et incluent des informations sur la date et l'heure de l'appel, le numéro d'incident unique, le type et le lieu de l'incident, etc.
        """
    )
    
    st.markdown(
        """
         **Mobilisation** : Cette base de données contient 489.562 observations en 22 colonnes. Elle couvre la même période que précédemment. Les enregistrements de mobilisation contiennent les informations sur tous les appareils d'incendie envoyés à chaque incident, y compris le numéro de l’incident, les identifiants de mobilisation uniques, la station à partir de laquelle l'appareil a été envoyé, le nombre d’appareil, les heures de mobilisation et d'arrivée sur les lieux de l'incident, le temps de trajet, le temps de mobilisation, le temps de réponse, etc.
         """
    )
    
    st.markdown(
        """
        Aucun des deux jeux de données n'avait de métafichier. Même si la plupart des colonnes étaient explicites, des recherches supplémentaires ont été nécessaires. 
        Nous avons également complété nos données avec la position géographique des différentes stations des brigades. 
        
        Elles nous proviennent du lien suivant : 'https://london-fire.labs.theodi.org/data/stations.csv'
        """
    )
    
    