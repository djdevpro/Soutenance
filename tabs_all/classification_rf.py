import streamlit as st


title = "Classification avec RandomForest"
sidebar_name = "Classification avec RandomForest"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Description du process :")

    st.markdown(
        """
        Pour prédire le temps de réponse des pompiers avec un modèle de RandomForestClassifier,  on a séparé la variable cible en 5 classes dont les limites correspondent aux valeurs des quintiles de sa distribution. Ainsi, on a des classes dont les populations sont égales pour éviter d’avoir un jeu déséquilibré. Cependant, comme la distribution du temps de réponse n’est pas uniforme et qu’elle présente une queue vers la droite, les intervalles correspondant aux classes ne sont pas de même taille. L’intervalle 4 étant beaucoup plus large que l’intervalle 2 par exemple. 
        """
    )

    st.markdown("### Avant d’entraîner le modèle, un preprocessing a été effectué avec les étapes suivantes :")

    st.markdown(
        """
        - importation des données propres avec les variables d’intérêt
        - séparation des variables explicatives et cible
        - encodage des données catégorielles via un encodage one-hot
        - catégorisation de la variable cible en 5 classes
        - séparation des données en jeu d’entraînement et en jeu de test
        - normalisation MinMax des variables quantitatives
        """
    )

    st.markdown("### A la suite de ce preprocessing, le modèle RandomForestClassifier a été entraîné en utilisant un GridSearchCV et une Validation Croisée à 3 sous-ensembles afin d’optimiser les hyperparamètres du modèle. Les hyperparamètres choisis pour optimiser ce modèle sont : ")

    st.markdown(
        """
        n_estimators : paramètre correspondant aux nombres d’arbres de décisions utilisés dans le modèle avec les valeurs suivantes : 
        [ 100, 200, 300, 400, 500]
        max_depth : paramètre correspondant à la profondeur maximale des arbres de décisions
			           [6, 7,8, 9, 10, 11, 12, 13, 14, 15] 

        Le choix du meilleur modèle suite à l’entraînement via la GridSearchCV se fait à partir de l’évaluation d’un score personnalisé, implémenté à partir d’une fonction custom_score en utilisant la fonction make_scorer de sklearn.metrics.
        """
    )

    st.markdown("###  Interprétation des résultats ")

    st.markdown(
        """
        Suite à l’optimisation des hyperparamètres, les valeurs des hyperparamètres qui ont été gardées, sont :
        - n_estimators : 400
        - max_depth : 10
        
        Le score associé est de :
        - 0.0226 pour le jeu d’entraînement
        - 0.0229 pour le jeu de test

        L’analyse des résultats des différents modèles indique que :
        - Lorsque l’hyperparamètre n_estimators augmente, cela n’a pas un impact significatif sur le score du modèle mais cela permet de diminuer l’overfitting. D’autre part, il y a une relation linéaire entre l’augmentation de cet hyperparamètre et le temps d’entraînement du modèle
        - Lorsque l’hyperparamètre max_depth augmente, cela a un impact positif sur le score du modèle mais cela participe aussi positivement à l’overfitting.

        A partir des matrices de confusion du modèle choisi sur les jeux de test et d’entraînement, on observe que les distributions de prédiction présentent des ratios similaires donc il ne semble pas y avoir d’overfitting.
        """
    )   
    
    st.image("assets/image5.png", width=700 , caption="Matrice de confusion du modèle sur le jeu de test")
    st.image("assets/image39.png", width=700 , caption="Matrice de confusion du modèle sur le jeu d’entraînement")

    st.markdown(
        """
        Concernant les performances, la classe réelle est celle qui est majoritairement prédite sauf pour la classe 2 ( cf. graphique dans le notebook modelisation ) . De ce point de vue, ce modèle apporte une valeur ajoutée par rapport à un modèle aléatoire. Cependant, on voit aussi que les classes 1 et 2 ont un très mauvais recall et f1-score qui ne sont pas satisfaisant.
        """
    )
    st.image("assets/image12.png", width=700 , caption="Rapport de classification du modèle sur le jeu de test :")

    st.markdown(
        """
        Afin d’interpréter ce modèle, nous avons calculé les valeurs de Shapley associées aux différentes variables explicatives. 
        """
    )

    
    st.image("assets/image34.png", width=700 , caption="Valeurs de Shapley associés aux variables explicatives dans un modèle  RandomForestClassifier ( n_estimators : 400, max_depth : 10 ) ")

    st.markdown(
        """
        Suite au calcul de valeurs de Shapley, on observe que les variables explicatives ayant le plus d’impact sont :
        - les variables de distance : long_distance et short_distance
        - le rang du camion mobilisé pour l’incident si plusieurs camion sont mobilisés pour un même incident ( PumpOrder_mob )
        - ensuite, il a plusieurs types de variables ayant des impacts similaires :
            - certains quartiers dans lesquels ont lieu les accidents
            - certains types d’accidents
            - certains  stations à partir desquelles sont mobilisés les pompiers


        Suite à cette première classification, le même modèle a été entraîné avec des classes correspondant à des intervalles différents qui semblaient plus pertinents d’un point de vue métier. Le problème du déséquilibre des classes est apparu. En effet, les classes correspondant à des temps élevés ( > 6min30 et plus ), ne sont pas prédites. Il aurait été possible de travailler sur ce problème via la bibliothèque imblearn pour voir le résultat en rééquilibrant les classes.

        """
    )