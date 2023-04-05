import streamlit as st


title = "Série temporelle avec SARIMAX"
sidebar_name = "Série temporelle avec SARIMAX"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Description du process :")

    st.markdown(
        """
        Pour prédire le temps de réponse des pompiers en tant que problème de série temporelle, nous avons tout d'abord restructuré la base de données en y intégrant différentes variables temporelles. Le dataFrame initial avait des observations détaillées par date, heure et minute. Pour chaque heure, plusieurs interventions ont été enregistrées avec des temps de réponse très variables en fonction de la nature de l'incident. Lors de l'analyse, nous avons également détecté cette même variabilité en considérant une journée entière, en distinguant le jour et la nuit. Le graphique suivant illustre cette situation. 
        """
    )

    st.image("assets/image19.png", width=700)

    st.markdown(
        """
        Pour une meilleure lisibilité, nous avons agrégé les observations, d’abord au niveau de l’heure puis à la journée en considérant à chaque étape la médiane du temps de réponse des pompiers. Ci-dessous la distribution de temps de réponse médian par jour entre le 1 janvier 2020  et le 28 février 2023.
        """
    )

    st.image("assets/image11.png", width=700)

    st.markdown(
        """
        Nous avons employé le module "seasonal_decompose" de Statsmodels pour identifier la saisonnalité, la tendance et les résidus, mais les résultats n'étaient pas satisfaisants. Nous pensons que cet outil n'a pas réussi à saisir la saisonnalité dans nos données, ce qui nous a poussés à mettre en place un test de stationnarité.
        """
    )

    
    st.image("assets/image18.png", width=700)
    

    st.markdown(
        """
        L'ADF statistique de test est -6.38 Cette valeur est inférieure aux valeurs critiques pour tous les niveaux de signification, ce qui suggère que la série chronologique est stationnaire, ce qui est confirmé par la p-valeur est 2,23050e-08. Ceci nous permet de conclure que la série n’a pas besoin d’être différencier avant de l’ajuster à un modèle SARIMAX. Pour le choix des paramètres nous nous aidons de AFC et du PACF, du calcul de la fréquence. Nous choisissons de considérer une périodicité de 8 jours et une tendance additive. Les paramètres choisis du modèle sont : SARIMAX(7, 0, 1)x(1, 0, 1, 8)
        """
    )

    
    st.image("assets/image14.png", width=700)

    st.markdown("### Nous obtenons les résultats suivants pour le SARIMA : ")
    st.image("assets/image1.png", width=700)

    st.markdown(
        """
        En termes de performance :

        - Mean Squared Error: 244.97000374233173
        - Root Mean Squared Error: 15.651517617864783
        - Mean Absolute Error: 12.629298150081139
        """
    )

    st.image("assets/image40.png", width=700)

    st.markdown("### Interprétation des résultats : ")

    st.markdown(
        """
        Avec un MSE de 244 et un MAE de 12, nous interprétons que le modèle n'a pas réussi à prédire de manière robuste le temps de réponse des pompiers. 

        Cette faiblesse du modèle peut être due à une limitation de l'algorithme utilisé. Bien que l'algorithme puisse être performant pour des données présentant une  certaine linéarité, il peut être imprécis face à des données dont la saisonnalité est complexe à déterminer.
        Nous proposons une solution pour améliorer les performances du modèle, à savoir entraîner un modèle de Réseaux de Neurones Récurrents qui pourrait être plus adapté à cette problématique.
        """
    )

