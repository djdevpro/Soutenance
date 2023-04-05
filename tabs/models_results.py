import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


title= 'Modèles et résultats'
sidebar_name = 'Modèles et résultats'

def run():
    st.title(title)
    st.write("""
        <style>div[data-baseweb="tab-list"] .css-184tjsw p {
    word-break: break-word;
    font-size: 12px!important;
    letter-spacing: -.5px;
    }</style>
    """, unsafe_allow_html=True)

    tab5, tab6,tab1,tab2, tab3, tab4 = st.tabs(['SARIMAX', 'RNN Univarié', 'Régression ( Elastic Net )', 'Classification ( RandomForest Classifier )','Régression ( XGBoost )', 'Classification ( XGBoost )' ])


    col1, col2 = tab1.columns(2)
    col1.header('ElasticNet')
    col1.markdown("""
        - Hyperparamètres choisis :
        """)
    col1.latex('\\begin{cases} alpha = 0.01 \\\\  l1\_ratio = 1 \\end{cases}')
    col1.markdown("""
        - Scores :
        """)
    col1.latex('\\begin{cases} R2\_score (train) = 0.54 \\\\   R2\_score (test) = 0.55 \\\\ MSE (test) = 5044.87 \\end{cases}')
    col2.header('Résidus')
    col2.image('assets/image23.png')

    tab1.header('Interprétabilité')
    tab1.image('assets/image6.png')

    col1, col2 = tab2.columns(2)
    col1.header('RandomForest')
    col1.markdown("""
        - Hyperparamètres choisis :
    """)
    col1.latex('\\begin{cases} n\_estimators = 400 \\\\  max\_depth = 10 \\end{cases}')
    col1.markdown("""
        - Scores d'erreur :
    """)
    col1.latex('\\begin{cases} Custom\_score (train) = 0.0227 \\\\   Custom\_score (test) = 0.0230 \\end{cases}')
    col2.header('Matrices de confusion')
    col2.markdown("""
        - Train :
    """)
    col2.image('assets/image39.png')
    col2.markdown("""
        - Test :
    """)
    col2.image('assets/image5.png')
    tab2.header('Interprétabilité')
    tab2.image('assets/image34.png')

    #tab3
    col1, col2 = tab3.columns(2)
    col1.header('XGBoost')
    col1.markdown("- Hyperparamètres choisis :")
    col1.latex('\\begin{cases} n\_estimators = 400 \\\\  max\_depth = 10  \\\\  learning\_rate= 0.1 \\end{cases}')
   
    col1.markdown("""
        - Scores :
        """)
    col1.latex('\\begin{cases} R2\_score (test) = 0.77 \\\\   MSE (test) = 2959.63 \\\\ MSE (train) = 1890.92 \\end{cases}')
    col2.header('Résultats')
    col2.markdown("""
        - Test :
    """)
    col2.image('assets/image8.png')
    tab3.header('Description')
    tab3.write("Le modèle XGBoost a été entraîné avec une combinaison de paramètres tels que le taux d'apprentissage, la profondeur maximale et le nombre d'estimateurs, qui ont été ajustés à l'aide d'une recherche sur grille. Les résultats montrent que le modèle a une bonne performance avec un R2 Score de 0,77.")

    #tab4
    col1, col2 = tab4.columns(2)
    col1.header('XGBoost')
    col1.markdown("- Hyperparamètres choisis :")
    col1.latex('\\begin{cases} n\_estimators = 400 \\\\  max\_depth = 10  \\\\  learning\_rate= 0.1 \\end{cases}')
   
    col1.markdown("""
        - Scores :
        """)
    col1.latex('\\begin{cases} F1 Score : 0.48 \\end{cases}')
    col2.header('Matrice de confusion')
    col2.markdown("""
        - Test :
    """)
    col2.image('assets/image27.png')
    tab4.header('Description')

    target_class = pd.DataFrame({'target_class': [0, 1, 2, 3, 4]})
    target_class['max'] = [210, 259, 301, 346, 1197]
    target_class['min'] = [0, 211, 260, 302, 347]
    target_class['mean'] = (target_class['max'] + target_class['min']) / 2
    target_class['min'] = target_class['min'].astype(str)
    target_class['max'] = target_class['max'].astype(str)
    target_class['target_class'] = target_class['target_class'].astype(str)
    target_class['target_class'] = target_class['target_class'].apply(lambda x: 'Class ' + x)
    target_class['min'] = target_class['min'].apply(lambda x: 'min ' + x)
    target_class['max'] = target_class['max'].apply(lambda x: 'max ' + x)
    target_class['min_max'] = target_class['min'] + ' ' + target_class['max']
    target_class = target_class[['target_class', 'min_max','mean']]
    target_class = target_class[['target_class', 'min_max', 'mean']]

    col1, col2 = tab4.columns(2)

    col1.write(target_class)
    col2.write("La classification peut être utilisée pour regrouper les temps de réponse des pompiers en classes spécifiques et aider à identifier les délais d'intervention les plus courants. Cependant, il est important de noter que pour cet exemple particulier, **la classification peut ne pas être la méthode la plus appropriée pour détecter la classe 4**, car l'écart entre les valeurs de cette classe est très important (allant de 347 à 1197 secondes).")

    tab4.write(" Ainsi, l'utilisation d'une classification pourrait conduire à une interprétation erronée des résultats.")

    tab5.header('Dispersion de la variable cible')
    tab5.image('assets/sarimax_dispersion_target.png')
    tab5.header('Temps de réponse médian')
    tab5.image('assets/sarimax_temps_median.png')
    tab5.header('Test de stationnarité')
    tab5.image('assets/sarimax_stationnarite.png')
    tab5.header('Résultats :')
    tab5.image('assets/sarimax_results.png')
    tab5.header('Prédiction :')
    tab5.image('assets/sarimax_predict.png')
    tab5.write("### **Résultats**")
    tab5.latex('\\begin{cases} Mean Squared Error \_score(test) = 244,97 \\\\  Root Mean Squared Error\_score(test) =15.65 \\\\  Mean Absolute Error\_score(test) =12.63 \\end{cases}')
    tab6.header('Structure du RNN :')
    tab6.image('assets/rnn_univarie.png')
    tab6.header('Prédiction du RNN :')
    tab6.image('assets/rnn_predict.png')

    col1,col2,col3 = tab6.columns([1,2,1])
    col2.latex('\\begin{cases} MSE\_score(train) = 226,20 \\\\  MSE\_score(test) = 243,7 \\end{cases}')