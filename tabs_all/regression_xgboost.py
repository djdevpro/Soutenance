import streamlit as st


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, accuracy_score, classification_report, r2_score, f1_score, confusion_matrix
from joblib import dump, load


title = "Explorez la performance d'intervention améliorer votre efficacité opérationnelle  !"
sidebar_name = "Série temporelle régression avec xgBoost"



def run():
       
    df = pd.read_csv("data/preprocessed_data_without_delay.csv",
                    index_col='DateAndTimeMobilised_mob',
                    parse_dates=['DateAndTimeMobilised_mob'])

    start_date_model = '2020-01-01 00:00:00'
    start_date = '2022-11-01 00:00:00'
    end_date = '2022-11-30 00:00:00'

    df_start_date_model = df[df.index >= start_date_model]

    df_model = df_start_date_model[['AttendanceTimeSeconds_mob', 'IncGeo_BoroughName_inc', 'short_distance', 'long_distance',
                                    'SpecialServiceType_inc', 'Resource_Code_mob', 'DeployedFromStation_Code_mob',
                                    'PumpOrder_mob', 'hour', 'dayofweek']].copy()

    target = 'AttendanceTimeSeconds_mob'
    df_model = pd.get_dummies(df_model, columns=['IncGeo_BoroughName_inc', 'SpecialServiceType_inc',
                            'Resource_Code_mob', 'DeployedFromStation_Code_mob'], drop_first=True)
    scaler = StandardScaler()
    df_model['PumpOrder_mob'] = scaler.fit_transform(df_model[['PumpOrder_mob']])
    df_model['hour'] = scaler.fit_transform(df_model[['hour']])
    df_model['dayofweek'] = scaler.fit_transform(df_model[['dayofweek']])

    test = df_model[(df_model.index >= start_date) & (df_model.index <= end_date)]

    X_test = test.drop(target, axis=1)
    model = load('models/model_reg.joblib')
    model_pred = pd.DataFrame(model.predict(X_test), columns=['prediction'])
    test_reset_index = test.reset_index()

    result = pd.concat([model_pred, test_reset_index], axis=1)
    result.set_index('DateAndTimeMobilised_mob', inplace=True)

    st.title(title)

    dates_to_test = result.index.unique()


  
    selected_date = st.selectbox("**Sélectionner une date pour tester une prédiction**", dates_to_test)

    score_table = pd.DataFrame({
        'R2 Score': [0.77],
        'MAE': [42.32],
        'Explained Variance Score': [0.77],
        'Test MSE': [2959.63],
        'Train MSE': [1890.92]
        })
    
    score_table.index = ['SCORES']

    if isinstance(result.loc[selected_date, 'prediction'], pd.Series):
        prediction = result.loc[selected_date, 'prediction'].iloc[0]
    else:
        prediction = result.loc[selected_date, 'prediction']

    if isinstance(result.loc[selected_date, target], pd.Series):
        actual_value = result.loc[selected_date, target].iloc[0]
    else:
        actual_value = result.loc[selected_date, target]


    st.write(f"**Prédiction :** {prediction}")
    st.write(f"**Valeur réelle :** {actual_value}")


    st.markdown(
        """
        <div class="alert danger">En sélectionnant une date, vous pouvez voir la prédiction du modèle pour ce jour spécifique ainsi que la valeur réelle correspondante.</div>
        """, unsafe_allow_html=True
    )
    st.markdown("---")

    # add image assets/reg_1mois.png
    st.markdown(
        """
        ### Prédiction sur une période de 1 mois
        """
    )
    st.image("assets/reg_1mois.png", use_column_width=True)

    st.markdown(
        """
         Voici une démonstration de test de régression pour prédire les temps d'intervention sur une période allant du 1er janvier 2020 au 30 novembre 2022, avec un modèle XGBoost. 
        """
    )

    st.table(score_table)

    st.markdown(
        """
         Bien que le modèle soit entraîné sur une période plus longue, nous avons choisi de tester uniquement sur une période allant du 1er novembre 2022 au 30 novembre 2022 afin de démontrer sa capacité à effectuer des prédictions précises sur des données récentes. 
        """
    )

    st.markdown("---")
