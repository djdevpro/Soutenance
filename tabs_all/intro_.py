import streamlit as st


title = "Temps de Réponse de la Brigade des Pompiers de Londres"
sidebar_name = "Introduction"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Introduction au projet")
    #image22.png
    st.markdown(
        """
         Fondée en 1865,  London Fire Brigade (LFB) est le service légal d'incendie et de sauvetage de Londres. Il est le second plus grand service d’incendie au Royaume-Uni après celui du service national d'incendie et de sauvetage écossais. Ce service compte environ 113 stations réparties sur l’ensemble de la capitale. D’après le récent rapport de la LFB (2021), le service des pompiers de Londres reçoit et traite chaque année pas moins de 100 000 appels d’urgence.
        """
    )
    
    st.image("assets/image22.png",  width=500)
    
    st.markdown("---")
    
    st.markdown(
        """
         Les interventions pour lesquelles la brigade est très souvent mobilisée sont les incendies, les services spéciaux et dans de nombreux cas pour des fausses alarmes.  De plus, le LFB répond également aux collisions routières, aux inondations, aux dégagements d'ascenseurs coincés et à d'autres incidents tels que ceux impliquant des matières dangereuses ou des accidents de transport majeurs. 
        """
    )
    
    st.markdown(
        """
         Étant donné le très grand nombre d’appels et la diversité des incidents, la précision et la rapidité du déploiement de la brigade est un enjeu crucial à la garantie d’un service de qualité pour la population londonienne. 
         """
    )
    
    
    st.markdown(
        """
         A cet effet, l’objectif de ce projet sera d’analyser et/ou d’estimer les temps de réponse et de mobilisation de la Brigade des Pompiers de Londres. Dans cette analyse, nous allons à l’aide de méthodes poussées de machine learning, construire un (ou des) modèle(s) d’apprentissage capable(s) d’estimer de façon robuste le temps de réponse de la LFB sur les lieux d’incident.
        
         1 https://data.london.gov.uk/download/incident-response-times-fire-facts/13ebd105-9fd2-4b7f-bb99-49c24be761ec/Fire%20Facts%20-%20Incident%20response%20times%202021.pdf

        """
    )
    

    st.markdown("---")

    st.markdown("### Compréhension et manipulation des données")
    st.markdown("#### Cadre")
    st.markdown(
        """
        Pour mener ce projet nous avons eu accès à un deux ensembles de jeux de données couvrant la période 2020 – 2022 et disponibles en libre accès ici
        - https://data.london.gov.uk/dataset/london-fire-brigade-incident-records
        - https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records
        """
    )