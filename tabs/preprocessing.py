import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


title= 'Preprocessing'
sidebar_name = 'Preprocessing'

def run():
    st.title(title)
   
    tab1,tab2,tab3 = st.tabs(['Nettoyage des données', 'Nouvelles variables', 'Encodage et normalisation'])

    tab1.header('Suppression des observations :')
    tab1.markdown(
        f"""
        - Avec des valeurs nulles ( 196 347 observations restantes )
        - Avec un délai ( ~ 73.8% des observations restantes : ~ 145000 observations )
        - Avec un temps inférieur au temps minimal de réponse théorique : ( ~ 2% des observations restantes )
        """)
    tab1.latex('y = 10 + (3.6 / 90 ) * dist')
    tab1.header('Suppression des variables :')
    tab1.markdown("""
        - Non pertinentes
        - Redondantes
    """)

    tab2.header('Variables temporelles :')
    tab2.markdown("""
        - Heure
        - Jour de la semaine
        - Jour du mois
        - Mois
        - Année
        - Trimestre
        - Jour de l'année
        - Semaine de l'année
    """)
    tab2.header('Variables de distance :')
    col1, col2 = tab2.columns(2)
    col1.image('assets/short_long_distance.png', width = 300)
    col2.write('\n')
    col2.write('\n')
    col2.latex('short\_distance(x) = \\begin{cases} x & \\text{if } x\\ < 200 \\\\ 0 & \\text{else} \\end{cases}')
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.write("\n")
    col2.latex('long\_distance(x) = \\begin{cases} 0 & \\text{if } x\\ < 200 \\\\ x & \\text{else} \\end{cases}')

    tab3.header('Encodage One Hot')
    tab3.image('assets/encodage_one_hot.png')
    tab3.header('Normalisation')
    tab3.image('assets/normalization.png')
    tab3.header('Catégorisation')
    tab3.image("assets/categorisation.png")