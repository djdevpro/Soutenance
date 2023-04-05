from collections import OrderedDict
import streamlit as st
import pandas as pd
import numpy as np
import datetime

from tabs import cover,introduction, dataset,preprocessing,models_results,conclusion,data_analysis
from tabs_all import intro_,volumetrie,analyse,variable,selection,traitement,visualisation,classification_rf,regression_en,sarimax,rnn,regression_xgboost,conclusion_,classification_month,regression_day


from labs import laboratoire

LABS = OrderedDict(
    [
        (laboratoire.sidebar_name, laboratoire),
    ]
)

st.set_page_config(
    page_title= 'Temps de Réponse de la Brigade des Pompiers de Londres' ,
    page_icon="https://datascientest.com/wp-content/uploads/2020/03/cropped-favicon-datascientest-1-32x32.png",
)

with open("style.css", "r") as f:
    style = f.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)


with open("app_html.txt", "r", encoding="utf-8") as f:
    credentials = f.read()

# TODO: add new and/or renamed tab in this ordered dict by
# passing the name in the sidebar as key and the imported tab
# as value as follow :

TABS = OrderedDict(
    [
        (cover.sidebar_name, cover),
        (introduction.sidebar_name, introduction),
        (dataset.sidebar_name, dataset),  
        (data_analysis.sidebar_name, data_analysis),
        (preprocessing.sidebar_name, preprocessing),
        (models_results.sidebar_name, models_results),
        (conclusion.sidebar_name, conclusion),
    ]
)



TABS_ALL = OrderedDict(
    [
        (intro_.sidebar_name, intro_),
        (volumetrie.sidebar_name, volumetrie),
        (analyse.sidebar_name, analyse),
        (variable.sidebar_name, variable),
        (selection.sidebar_name, selection),
        (traitement.sidebar_name, traitement),
        (visualisation.sidebar_name, visualisation),
        (classification_rf.sidebar_name, classification_rf),
        (regression_en.sidebar_name, regression_en),
        (sarimax.sidebar_name, sarimax),
        (rnn.sidebar_name, rnn),
        (regression_xgboost.sidebar_name, regression_xgboost),
        (conclusion_.sidebar_name, conclusion_),
    ]
)


TABS_REG = OrderedDict(
    [
        (regression_day.sidebar_name, regression_day),
    ]
)
TABS_CLASS = OrderedDict(
    [
        (classification_month.sidebar_name, classification_month),
    ]
)


def run():
    
    
    #v_custom = st_labs('Hello world', 0, 100, 50, key="slider1")
    #st.sidebar.write(v_custom)

    st.sidebar.markdown(
        """
        <div class="logo">
            <svg xmlns="http://www.w3.org/2000/svg" width="279.644" height="85"><g data-name="Group 48" transform="translate(-161 -54)"><circle data-name="Ellipse 14" cx="42.5" cy="42.5" r="42.5" transform="translate(161 54)" fill="#1c1c1c"/><g data-name="Group 41"><path data-name="Path 14" d="M208.193 87.702c.5-1.339-6.572-3.789-6.434-7.371.172-4.464 9.744-7.877 17.763-.913l2.672-7.395c-4.864-4.184-10.724-6.6-17.331-6.093-10.56.8-16.937 8.529-12.658 16.034 1.429 2.5 4.7 4.236 8.423 4.855 3.459.575 6.124.523 7.565.883z" fill="#973737"/></g><path data-name="Path 15" d="M219.584 98.166c-7.5-2.624-13.841 1.936-18.262 3.44-6 2.043-9.572 2.789-14.034 1.09a17.384 17.384 0 01-3.689-2.1 13.411 13.411 0 01-3.237-3.977 15.884 15.884 0 01-1.685-3.884l-.838-3.673 1.922 3.076a19.039 19.039 0 004.8 5.269 13.676 13.676 0 006.532 2.466 19.294 19.294 0 005.679-.366 35.313 35.313 0 01-5.161-.835 15.707 15.707 0 01-6.062-2.964 12.21 12.21 0 01-2.663-3.058 13.489 13.489 0 01-1.407-3.079 12.33 12.33 0 01-.559-3.54 12.339 12.339 0 01.557-3.92 12.882 12.882 0 011.919-3.766 16.159 16.159 0 00.92 9.916 11.023 11.023 0 005.042 4.947 18.788 18.788 0 005.852 1.639 21.615 21.615 0 004.3.145 33.287 33.287 0 01-8.859-3.546 9.7 9.7 0 01-3.841-4.8 7.849 7.849 0 01-.3-4.691 12.427 12.427 0 011.513-3.863l1.264-1.949a20.982 20.982 0 00.7 7.108 10.24 10.24 0 003.963 4.569 12.559 12.559 0 005.6 1.894c2.2.207 10.042.6 12.873 1.3 4.112.964 7.63 3.163 8.865 5.02 1.074 1.614 1.662 3.622 1.225 3.665-.871.087-1.165-.916-2.929-1.533z" fill="#973737"/><path data-name="Path 16" d="M213.934 100.365c-5.455-.035-6.9 1.245-8.362 2.132 11.405.037 10.542 19.845-13.916 9.552l-2.428 8.467c7.095 3.466 15.749 5.222 23.461 3.238 10.411-2.68 13.506-11.952 9.807-19.213-.831-1.628-3.106-4.141-8.562-4.176z" fill="#973737"/><text data-name="Le Studio" transform="translate(256.644 98.668)" font-size="39" font-family="" font-weight="700"><tspan x="0" y="0">Le Studio</tspan></text><text transform="translate(256.644 124.534)" font-size="27" font-family="" font-weight="600"><tspan x="0" y="0">DataScientest</tspan></text></g></svg>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.session_state.radio = 0


    option = st.sidebar.selectbox(
        'Performance  d\'interventions choix de la méthode : ',
        ('Accueil - Compte Rendu', 'Temps de Réponse - Régression', 'Temps de Réponse - Classification','Laboratoire - Générateur de modèles'),
        key='selectbox'
    )
    
    if option == 'Temps de Réponse - Régression':      
        st.session_state.radio = 0
        tab_name = st.sidebar.radio("", list(TABS_REG.keys()), st.session_state.radio, key='radioreg')
        tab = TABS_REG[tab_name]   
        if tab_name == 'Temps de réponse - Régression':
            st.sidebar.write(
                """
                
                <div style="border: dashed 1px #ccc;padding: 10px;font-size: 13px;font-style: italic;">
                Note:
                <p>Ce formulaire est destiné à la prédiction du temps de réponse des pompiers pour un incident donné, 
                en utilisant un modèle de régression entraîné sur des données du 2021-01-01 au 2022-11-01.</p>

                <p>Le modèle de régression peut être utilisé pour prédire le temps de réponse des pompiers pour un incident spécifique.
                 Il convient de noter que le modèle a été entraîné sur des données antérieures,
                  donc la précision de la prédiction peut varier en fonction des changements dans les tendances et les conditions depuis lors.</p>
                
                </div>
                """
                , unsafe_allow_html=True)

    elif option == 'Temps de Réponse - Classification':     
        st.session_state.radio = 0
        tab_name = st.sidebar.radio("", list(TABS_CLASS.keys()), st.session_state.radio, key='radioreg')
        tab = TABS_CLASS[tab_name] 
        
        st.sidebar.write(
            """
            
            <div style="border: dashed 1px #ccc;padding: 10px;font-size: 13px;font-style: italic;">
            Note:
            <p>Ce formulaire est destiné à la prédiction du temps de réponse des pompiers pour un incident donné, 
            en utilisant un modèle de régression entraîné sur des données du 2021-01-01 au 2022-11-01.</p>

            <p>La classification peut être utilisée pour regrouper les temps de réponse des pompiers en classes spécifiques et aider à identifier les délais d'intervention les plus courants. Cependant, il est important de noter que pour cet exemple particulier, la classification peut ne pas être la méthode la plus appropriée pour détecter la classe 4, car l'écart entre les valeurs de cette classe est très important (allant de 346 à 1197 secondes). Ainsi, l'utilisation d'une classification pourrait conduire à une interprétation erronée des résultats.</p>
            
            </div>
            """
            , unsafe_allow_html=True)
    elif option == 'Laboratoire - Générateur de modèles':        
        tab_name = st.sidebar.radio("", list(LABS.keys()), st.session_state.radio, key='radiok')

        tab = LABS[tab_name]    
        
        
    else:  
        tab_name = st.sidebar.radio("", list(TABS.keys()), st.session_state.radio, key='radiok')

        tab = TABS[tab_name]    
            
        bottom_sidebar_container = st.sidebar.container()
        bottom_sidebar_container.write(credentials, unsafe_allow_html = True)
    tab.run()



    
    

if __name__ == "__main__":
    run()
