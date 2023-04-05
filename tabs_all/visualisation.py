import streamlit as st


title = "Visualisations et Statistiques "
sidebar_name = "Visualisations et Statistiques"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Relations entre les variables explicatives et la variable cible :")

    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown(
            """
            Hormis les relations mises en évidence précédemment, il est pertinent de présenter le graphique montrant l’influence de la distance entre le station de pompiers et le lieu de l’incident. En raison de la dispersion importante de la variable cible, ce graphique a été créé en groupant les temps de réponse en fonction de la distance puis en moyennant les temps de réponse pour chaque distance. Ainsi, on observe uniquement une tendance moyenne.
            """
        )
    with col2:
        st.image("assets/image31.png",width=300)

    st.markdown(
        """        
        On observe les deux régimes mis en évidence dans la section précédente. D’autre part, pour des valeurs importantes de la distance ( > 3.5 km ), les moyennes sont progressivement de plus en plus dispersées. Cela est dû au fait qu’il y a moins d’observations pour ces distances et les moyennes ne jouent plus le rôle de moyennes car souvent, on a qu’une seule observation pour une distance données ou bien, elles sont calculées sur un très faible nombre d’observations.

        D’autre part, l’influence de l’heure de l’incident est intéressante. En effet, on observe la nuit, une augmentation du temps de mobilisation mais pour le temps de trajet,
        """
    )

    col1, col2 = st.columns([2, 2])
    with col1:
        st.image("assets/image36.png", use_column_width=True, width=300)
    with col2:
        st.markdown(
            """
            c’est l’inverse qui est observé avec une diminution la nuit en raison de l’absence de trafic. De ce fait, lorsqu’on observe le temps de réponse qui est la somme du temps de mobilisation et du temps de trajet, on observe tout de même une augmentation du temps de réponse la nuit mais celle-ci est moins marquée.  Le graphique présenté a été créé en moyennant le temps de mobilisation sur des incidents ayant lieu à des distances comprises entre 850 et 950 mètres en utilisant la distance de Haversine pour chaque heure. 
            """
        )
    
    col1, col2 = st.columns([2, 2])
    with col1:
        st.markdown(
            """
            Ce second graphique a été créé de la même manière que le premier mais en moyennant le temps de trajet. 
            """
        )
    with col2:
        st.image("assets/image33.png", use_column_width=True, width=300)
    

    st.markdown("---")
    st.markdown(
        """
        On voit dans le graphique récapitulatif suivant, l’influence de l’heure de l’accident sur le temps de réponse moyen pour des intervalles de distance de 100 mètres. On observe bien une augmentation moins marquée du temps de réponse la nuit.

        """
    )

    st.image("assets/image16.png", use_column_width=True, width=300)

    st.markdown("---")
    st.markdown(
        """
        La variable PumpOrder correspondant au rang de mobilisation du camion de pompiers a une tendance très marquée comme on peut le voir sur le graphique suivant représentant le temps de réponse pour des intervalles de distances de 100 m : 
        """
    )
    
    st.image("assets/image10.png", use_column_width=True, width=300)

    st.markdown(
        """
        Enfin, on a aussi récupéré des variables météorologiques telles que la quantité de précipitations, afin de comprendre leur influence. En effectuant, une matrice de corrélation pour des observations relativement similaires ( PumpOrder égale 1 et distance comprise entre 850 et 950 mètres ), on observe des scores très proches de 0. Ainsi, on a décidé de ne pas les prendre en compte dans la modélisation. 
        """
    )
    
    st.markdown("---")
