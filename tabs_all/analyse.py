import streamlit as st


title = "Variable cible et quelques analyses statistiques"
sidebar_name = "Analyses statistiques"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Description de la volumétrie du jeu de données.")
    #image22.png
    st.markdown(
        """
        Pour rappel, le but de notre recherche est d’analyser et de donner une estimation de manière robuste du temps de réponse de la brigade des sapeurs-pompiers de Londres. 
        
        Le temps de réponse total peut être défini comme correspondant aux minutes et aux secondes écoulées entre le moment de l'appel et l'arrivée du premier véhicule à l'incident. 
        """
    )
    
    st.image("assets/image24.png", use_column_width=True, width=300)

    
    st.markdown(
        """
        Afin d’identifier la variable cible de l’étude nous avons ainsi considéré la différence de temps entre l’heure de la mobilisation et l’heure d’arrivée sur les lieux de l’incident. Dans le jeux de données, cette variable est labellisée par “AttendanceTimeSeconds_mob”. Nous l’avons converti en min.

        Après le nettoyage, le traitement des valeurs manquantes et l’ajout de variables externes, la taille de notre nouvelle base de données est à présent d’environ 294.731 observations[2]. Ci-dessous quelques descriptions statistiques de la variable cible.
        """
    )
    
    st.markdown("## Statistique sur la variable Target: temps de réponse en min")

    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.image("assets/image15.png", use_column_width=True, width=300)
    with col2:
        st.markdown(
            """
            |       |  Valeurs             |
            |-------|---------------|
            | count | 294731.000000 |
            | mean  | 6.108498      |
            | std   | 2.470564      |
            | min   | 0.016667      |
            | 25%   | 4.450000      |
            | 50%   | 5.750000      |
            | 75%   | 7.316667      |
            | max   | 20.000000     |

            """
        )
        
    st.markdown(
        """
         Souhaitant effectuer des calculs de distances entre les stations de départs et les lieux d’incident, une autre manipulation supplémentaire nous a conduit à réduire et à enregistrer une autre base de données de taille plus petite (82557 observations) compte tenu de la disponibilité des données.
        """
    )

    st.markdown(
        """
        En ce qui concerne la distribution du temps de réponse des sapeurs-pompiers, on voit que celle-ci suit une loi normale avec un aplatissement de la courbe vers la droite. Le temps moyen de réponse d’environ 6,1 minutes et dans des proportions faibles, le temps de réponse fait plus de 10 minutes.
        Le graphique suivant représente exactement le temps de mobilisation des troupes, c’est-à-dire le temps écoulé entre la fin du signalement de l’incident et le départ des troupes de la caserne. En moyenne il faut environ 1,23 minutes pour la mobilisation des troupes et dans de rares situations, le temps écoulé va jusqu’à 18 minutes.
        """
    )
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.image("assets/image41.png", width=400)
    with col2:
        st.markdown(
            """
            |       |  Valeurs             |
            |-------|---------------|
            | count | 294731.000000 |
            | mean  | 1.232282      |
            | std   | 0.638779      |
            | min   | 0.000000      |
            | 25%   | 0.883333      |
            | 50%   | 1.166667      |
            | 75%   | 1.483333      |
            | max   | 18.483333     |
            """
        )

    st.markdown(
        """
        Dépendamment de la nature de l’incident, cela pourrait requérir un temps de mobilisation et/ou un temps de réponse plus ou moins long. Le graphique suivant montre la relation entre le temps de mobilisation, le temps de réponse et le type d’incident.
        """
    )
    #image21.png
    st.image("assets/image21.png", use_column_width=True, width=300)
    st.image("assets/image28.png", use_column_width=True, width=300)
    st.image("assets/image13.png", use_column_width=True, width=300)
    st.markdown(
        """
        Ce résultat est en cohérence avec les analyses contenues dans le récent rapport de la LFB : ce qui 
        https://data.london.gov.uk/download/incident-response-times-fire-facts/13ebd105-9fd2-4b7f-bb99-49c24be761ec/Fire%20Facts%20-%20Incident%20response%20times%202021.pdf
        """
    )

    st.markdown(
        """
        Dans les graphiques ci-dessus nous sommes en présence d’une distribution ayant un nombre important de valeurs extrêmes. Par conséquent, il existe la probabilité d’une très forte variabilité des variances et des résidus au sein de chaque groupe comme l'indiquent les résultats du test de shapiro. 
        """
    )

    st.markdown("---")

    st.markdown(
        """
        Nous avons également étudié la relation entre le temps de réponse et les raisons des éventuels délais de réponses observés par les brigades. Dans 82% des cas, les brigades d'intervention ne rencontrent pas de délai. Les autres raisons enregistrées sont 'not help up', le traffic' ou encore  l'information incomplète sur l'adresse. Toutefois, nous pensons qu'en séparant notre jeu de données sur la base des interventions avec délai et celles sans délai, nous serions à même de pouvoir entraîner un meilleur modèle de prédiction.
        """
    )


    st.markdown("---")
    st.markdown("### Distribution de la variable DelayCode_description")

    st.markdown(
        """
        | No delay registred                    | 0.826411 |
        |---------------------------------------|----------|
        | Not held up                           | 0.110606 |
        | Traffic, roadworks, etc               | 0.033780 |
        | Traffic calming measures              | 0.012723 |
        | Address incomplete/wrong              | 0.007522 |
        | Arrived but held up - Other reason    | 0.002358 |
        | Mob/Radio problems when mobilised     | 0.002307 |
        | On outside duty when mobilised        | 0.001415 |
        | Weather conditions                    | 0.001384 |
        | Appliance/Equipment defect            | 0.000889 |
        | At drills when mobilised              | 0.000604 |
        """
    )
    st.markdown("---")
    st.image("assets/image9.png", use_column_width=True, width=300)

    st.markdown("---")

    st.markdown("### Relation entre le temps de trajet et la zone d’intervention.")
    st.image("assets/image32.png", use_column_width=True, width=300)

    st.markdown("---")
    st.markdown("### Le graphique suivant montre la relation entre le temps de réponse en minutes et les différents mois de l’année en fonction puis un second par type d’incident.")
    st.image("assets/image17.png", use_column_width=True, width=300)
    st.image("assets/image38.png", use_column_width=True, width=300)

    st.markdown(
        """
        Ces deux représentations semblent indiquer une forte variabilité du temps de réponse entre les différents mois de l’année, notamment une forte baisse durant le mois de mars 2020 (ce qui pourrait correspondre à la période de l’entrée en confinement durant le COVID),  des pics durant les mois d’été et aussi en périodes de fin d’année.
        """
    )
    
    st.markdown("---")

    st.image("assets/image35.png", use_column_width=True, width=300)