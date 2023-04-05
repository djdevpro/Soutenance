import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.graph_objs as go
import json

#data = pd.read_csv("data/clean_data_analyse.csv")

title= 'Statistiques et visualisation des données'
sidebar_name = "Visualisation des données"

def run():
    fig_dict = {}

    st.title(title)
    # Distribution plot
    tab1, tab2, tab3,tab4, tab5, tab6 = st.tabs(
        ["Distribution","Groupe d'incidents","Délai","Année-Mois", 'Rang de déploiement', 'Heure de l\'accident']
    )
    # Tab1 :
    """
    fig = px.histogram(data, x='AttendanceTimeSeconds_mob', nbins=20)
    fig.update_traces(marker_color='red', opacity=0.7)
    fig.update_layout(title_text='Distribution du temps de réponse en seconde')
    fig.write_image("assets/distribution-Chart.png")
    tab1.plotly_chart(fig)
    """
    tab1.image('assets/image_nombre_d_appel.png')
    tab1.image('assets/image_nombre_d_appel_jour.png')
    tab1.image('assets/image24.png')
    tab1.image('assets/distribution-Chart.png')
    


    # Expander pour la description des graphiques
    expander = tab1.expander('Voir description de la distribution')
    expander.write("""
        Le diagramme illustre comment le temps de réponse des pompiers est réparti. Il montre que cette répartition suit une distribution normale avec une légère asymétrie à droite. En moyenne, le temps de réponse est d'environ 6,1 minutes, mais dans un faible pourcentage de cas, le temps de réponse peut dépasser les 10 minutes..
    """)
    
    # Tab2
    """
    fig2 = px.box(data, x='IncidentGroup_inc', y='AttendanceTimeSeconds_mob')
    fig2.update_layout(title_text='Distribution du temps de réponse en fonction du groupe d\'incidents')
    fig2.write_image("assets/incidentGroup-Chart.png")
    tab2.plotly_chart(fig2)
    """
    tab2.image('assets/incidentGroup-Chart.png')

    # Tabs
    tabs = tab3.tabs(["📈 Chart"])
    with tabs[0]:
        # Chart tab
        """
        fig3 = px.box(data, x='DelayCode_Description_mob', y='AttendanceTimeSeconds_mob')
        fig3.update_layout(title_text="Relation entre le temps de réponse en minute et délais d'intervention")
        fig3.update_layout(yaxis=dict(title='Temps de réponse en secondes'))
        fig3.update_layout(xaxis=dict(title=' '))
        
        fig3.write_image("assets/delay-Chart.png")
        st.plotly_chart(fig3)
        """
        st.image('assets/delay-Chart.png')
        
        st.write("### Délais d'intervention")
        exp_delay = st.expander('Explication')
        exp_delay.write('A partir de ce graphique, on comprend que la présence d’un délai exceptionnel impacte de manière significative le temps de réponse des pompiers. Sachant que la présence d’un délai n’est pas connu à l’avance lorsqu’un accident se présente, on ne peut pas utiliser cette variable comme variable explicative dans la modélisation.')
    
    """    
    with tabs[1]:
        # Data tab
        st.subheader("Données")
        
        fig_dict['fig4'] = data[["AttendanceTimeSeconds_mob","DelayCode_Description_mob"]].head(5)
        # save the data in a json file
        with open('data/fig4.json', 'w') as outfile:
            json.dump(fig_dict['fig4'].to_dict(), outfile)

        st.write(fig_dict['fig4'])
    """
    
    
    
    
    #Lines
    tab4_1, tab4_2, tab4_3 = tab4.tabs(['Année-Mois',  "Groupe d\'accidents","Type d\'accidents"])

    tab4_1.header("Évolution du temps de réponse moyen en fonction de l'année et du mois")
    tab4_1.image("assets/image44.png")
    exp1 = tab4_1.expander('Explication')
    exp1.write("Le graphique ci-dessous présente l'évolution du temps de réponse des pompiers entre 2020 et 2023. Bien qu'il y ait une légère tendance à la hausse, on observe une grande variabilité du temps de réponse au fil du temps. Le point le plus marquant de la courbe est observé en mars 2020 avec une nette réduction du temps de réponse. Cette situation pourrait s'expliquer par le début de la pandémie et la réduction des activités humaines durant cette période.")
    
    tab4_2.header("Évolution du temps de réponse en fonction de l'année et du mois pour différents type d'accidents")
    tab4_2.image("assets/image42.png")
    exp2 = tab4_2.expander('Explication')
    exp2.write("Le graphique présenté montre comment le temps de réponse des pompiers varie en fonction du type d'incident. Bien que les trois catégories présentées suivent la même tendance, il est à noter que le temps de réponse est plus court pour la catégorie 'services spéciaux'.")

    tab4_3.header("Évolution du temps de réponse en fonction de l'année et du mois pour différents groupes d'accidents")
    tab4_3.image("assets/image43.png")
    exp3 = tab4_3.expander("Explication")
    exp3.write("Le graphique ci-dessus montre comment le temps de réponse des pompiers varie en fonction du type de service spécial auquel ils sont appelés. Malgré l'intervention des pompiers pour une variété de services spéciaux, on observe une concentration du temps de réponse autour de valeurs centrales, qui se situent entre 300 et 400 secondes, et ceci tout au long de la période étudiée.")

    tab5.header('Évolution du temps de réponse en fonction du rang de déploiement')
    tab5.image("assets/pump_order.png")
    tab6.header('Évolution du temps de réponse en fonction de l\'heure de l\'accident')
    tab6.image("assets/hour_of_call.png")

