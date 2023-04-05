import streamlit as st


title = "Conclusion"
sidebar_name = "Conclusion"


def run():
    
    st.title(title)

    st.markdown("---")
    

    st.markdown(
        """
        Lors de ce projet, nous avons analysé les données afin de comprendre quelles seraient les variables les plus pertinentes pour déterminer la variable cible. Nous avons aussi supprimé des données afin d’avoir les observations les plus propres possibles et en même temps, représentatives. Enfin, nous avons effectué des transformations sur les variables afin de créer de nouvelles variables permettant d’optimiser les performances de nos modèles. 

        Concernant la modélisation, plusieurs approches ont été réalisées comme la régression, la classification,et  les séries temporelles via SARIMAX et via RNN. Cela nous a permis de comprendre que l’approche par série temporelle n’était pas adaptée pour modéliser ce problème, que la régression présente des performances intéressantes ( R2-score : 0.537 sur un ensemble de test entier) et que la classification pourrait être améliorée en améliorant le choix des intervalles pour les classes et en faisant un travail sur les jeux déséquilibrés via des bibliothèques comme imblearn.

        Les difficultées rencontrées concernent différents aspects du projet :
        les données : le temps de réponse présente une dispersion importante pour une même distance caserne-accident. De ce fait, on peut se demander si toutes les observations correspondent à des interventions depuis la caserne ou si pour certaines interventions, les pompiers étaient déjà dehors. Nous n’avons pas la réponse à cette question et cela pourrait avoir un impact sur la distance de trajet estimée qui est fortement corrélée au temps de réponse
        l’accès à des données supplémentaires : certaines données comme le trafic ou bien, la distance exacte via le réseau routier nécessite de passer par des APIs payantes. L’accès à ces données aurait permis d’améliorer les performances.
        le matériel informatique : l’entraînement de certains modèles de machine learning couplé avec de la validation croisée et une optimisation d'hyper paramètres via un GridSearchCV peut vite augmenter les temps de calcul, et perturber le travail de modélisation. De même pour l’interprétabilité, avec le calcul des valeurs de Shapley qui peut prendre beaucoup de temps. 

        Pour aller plus loin, nous aurions pu creuser les pistes suivantes :
        série temporelle : effectuer un RNN multivarié pour incorporer d’autres variables explicatives 
        données : apporter d’autres données via des API comme GoogleMaps pour avoir par exemple les distances exactes entre les casernes et les lieux des accidents en fonction du réseau routier, ou bien, avoir l’évolution du trafic en fonction des heures pour affiner la prédiction.
        classification : optimiser la classification sur les intervalles ayant moins d’observations lorsqu’on ne découpe pas les classes en s’appuyant sur des quintiles, en utilisant la bibliothèque imblearn

        Rq: Les résultats présentés dépendent de l’état de la base de données de la London Fire Brigade qui est actualisée régulièrement. 
        
        ### Auteurs du projet :
        - Djidjelli Youcef
        - Ouaro Estelle
        - Szleper Jean
        """
    )
