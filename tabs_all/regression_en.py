import streamlit as st


title = "Régression avec ElasticNet"
sidebar_name = "Régression avec ElasticNet"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Description du process :")

    st.markdown(
        """
        Pour prédire le temps de réponses des pompiers avec un modèle ElasticNet, un preprocessing similaire à celui effectué pour le modèle de classification RandomForestClassifier, a été réalisé, à la différence que la variable cible n’ a pas été catégorisée.

        A la suite du preprocessing, le modèle ElasticNet a été entraîné en utilisant un ElasticNetCV afin de trouver les hyperparamètres alpha et l1_ratio les plus pertinents.

        La grille de paramètres choisie dans ce cas, est la suivante :
        -  l1_ratio : [ 0.1, 0.25, 0.5, 0., 0.75, 0.8, 0.85, 0.9, 0. 99, 1 ]
        - alpha : [0.0001, 0.0005, 0.001, 0.01, 0.02, 0.025, 0.05, 0.1, 0.25, 0.5, 0.8, 1.0]

        Le choix du meilleur modèle suite à l’entraînement via l’ElasticNetCV se fait à partir de l’évaluation d’un score R2.
        """
    )
    
    st.markdown("## Interprétation des résultats :")

    st.markdown(
        """
        Suite à l’optimisation des hyperparamètres, on se retrouve avec les valeurs suivantes :

        l1-ratio : 1
        alpha : 0.001

        Le R2-score pour ce modèle est le suivant :

        pour le jeu de test : 0.549
        pour le jeu d’entraînement : 0.537

        Ainsi, le modèle ne présente pas d’overfitting.
        """
    )

    
    st.image("assets/image23.png", width=700 , caption="Distributions des résidus pour l’algorithme choisi et un algorithme prédisant la moyenne :")

    st.markdown(
        """
        On observe que l’algorithme choisi, performe mieux qu’un simple algorithme prédisant la moyenne.
        
        Sur le graphique suivant, on observe les 30 coefficients les plus importants en valeurs absolues, associés à différentes variables explicatives. Il y a quelques coefficients très forts au début avec une décroissance importante des coefficients puis des coefficients plus faibles qui se stabilisent.

        Parmi les premiers coefficients, on observe majoritairement le rang de mobilisation du camion de pompiers. On a aussi la variable short_distance avec un coefficient fort associé tandis que long_distance est présente mais avec un coefficient bien plus faible. Ceci s’explique par la différence de pente qu’on avait observé dans le graphique lors du preprocessing ( cf. notebook preprocessing ).

        On observe aussi en première position l’heure de l’accident avec pour valeur 1h du matin. Il est compliqué d’expliquer la raison de cette présence en première position.
        """
    )

    
    st.image("assets/image6.png", width=700 , caption="Valeurs absolues des coefficients associés aux variables explicatives dans le cadre de la régression ( les 30 les plus importantes ) ;")
