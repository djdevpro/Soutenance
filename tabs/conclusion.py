import streamlit as st

title = "Conclusion"
sidebar_name = "Conclusion"


def run():
    st.title(title)

    tab1, tab2, tab3 = st.tabs(['Regard critique', 'Perpectives', 'Conclusion'])

    tab1.write("\n")
    tab1.write("\n")
    tab1.markdown(
        """
        - Creuser la compréhension des données
        """
    )
    tab1.write("\n")
    tab1.markdown("""
        - Utiliser un OSRM ( Open Source Routing Machine ) afin d'avoir une mesure plus précise de la distance
        """
    )
    tab1.write("\n")
    tab1.markdown(
        """
        - Approfondir le travail sur la classification en créant des classes pertinentes et en utilisant imblearn
        """
    )


    tab2.write("\n")
    tab2.write("\n")
    tab2.markdown(
        """
        - Entrer en contact avec la LFB pour :
            * Avoir une meilleure compréhension des données
            * Connaître les intervalles de temps les plus pertinents en terme de survie et dégâts selon l'accident
        """
    )
    tab2.write("\n")
    tab2.markdown(
        """
        - Utiliser des APIs payantes pour récupérer d'autres données comme l'évolution du trafic sur le chemin utilisé
        """
    )
    tab2.write("\n")
    tab2.markdown("""
        - Effectuer un RNN multivarié pour incorporer d'autres variables explicatives
        """
    )

    tab3.write("\n")
    tab3.markdown(
        """
        - Analyse, nettoyage et preprocessing des données
        """
    )
    tab3.write("\n")   
    tab3.markdown(
        """
        - Utilisation de différents modèles de Machine Learning :
            * Classification : RandomForest et XGBoost
            * Régression : ElasticNet et XGBoost
            * Séries temporelles : SARIMAX et RNN
        """
    )
    tab3.write("\n")
    tab3.markdown(
        """
        - Résultats :
            * La régression linéaire est pertinente et peut être améliorée
            * La classification est à améliorer en travaillant sur le choix des classes
            * Les séries temporelles (SARIMAX) ne sont pas adaptées
        """
    )

