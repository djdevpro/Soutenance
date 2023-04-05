import streamlit as st


title = "Choix des variables pertinentes pour l’étude"
sidebar_name = "Choix des variables"


def run():
    
    st.title(title)

    st.markdown("---")    

    st.markdown(
        """
        L'objectif étant d'estimer le temps de réponse de la Brigade des Pompiers de Londres lors d'un incident, le choix des variables est le suivant :
        """
    )
    # creer un tableau markdow avec les variables explicatives

    st.markdown(
        """
        | Variables explicatives | Description |
        | --- | --- |
        | DeployedFromStation_Name | Nom de la station de pompiers à partir de laquelle est partie l'équipe sollicitée |
        | IncGeo_BoroughName | Le quartier dans lequel a lieu l'incident |
        | Distance | Calculée à partir de plusieurs variables grâce au package haversine |
        | ResourceCode | Le type de ressources ( équipes, camions, ... ) mobilisé pour l'incident |
        | PumpOrder | Le rang du camion mobilisé pour l'incident si plusieurs camion sont mobilisés pour un même incident |
        | IncidentStationGround | La station de pompiers la plus proche de l'incident |
        | HourOfCall | L'heure de l'incident |
        | MonthOfCall | Le mois de l'incident |
        | SpecialServiceType | Le type d'incident |
        """
    )



    st.markdown("---")

    
    st.markdown(
        """
        - Variables temporelles telles que l'heure de l'accident, le mois de l'accident : Ont une influence sur différents paramètres influençant le temps de réponse tels que le trafic, la disponibilité des pompiers, ...
        - DeployedFromStation_Name ( station de pompiers à partir de laquelle est partie l'équipe sollicitée )  : chaque station a son architecture particulière et une localisation particulière qui peuvent jouer sur le temps de mobilisation et sur le temps de trajet
        - IncGeo_BoroughName ( le quartier dans lequel a lieu l'incident )
        - Distance ( calculée à partir de plusieurs variables grâce au package haversine ) : Moyenne entre les distances de Haversine et de Manhattan entre la station de pompiers et le lieu de l'incident, qui a un impact direct sur le temps de trajet et donc sur le temps de réponse. Elle est arrondie à 5  mètres près.
        - ResourceCode  : le type de ressources ( équipes, camions, ... ) mobilisé pour l'incident
        - PumpOrder : le rang du camion mobilisé pour l'incident si plusieurs camion sont mobilisés pour un même incident
        - SpecialServiceType : le type d'incident
        """
    )

    st.markdown("---")