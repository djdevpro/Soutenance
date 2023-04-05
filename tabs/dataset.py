import streamlit as st
import pandas as pd
import numpy as np

"""
data = pd.read_csv('data/merged_data.csv', index_col = 'IncidentNumber')
num_observations = data.shape[0]
num_features = data.shape[1]
ratio_null_values = round(100 * data.isna().sum().sum() / (data.shape[0]*data.shape[1]),2)


not_selected_features = ['PerformanceReporting_mob', 'DateAndTimeLeft_mob','DeployedFromLocation_mob', "PumpHoursRoundUp_inc", 'PumpCount_inc', 'NumPumpsAttending_inc', 'NumStationsWithPumpsAttending_inc',
                         'SecondPumpArriving_DeployedFromStation_inc','SecondPumpArriving_AttendanceTime_inc', 'IncidentStationGround_inc', 'FRS_inc', 'Northing_rounded_inc',
                         'Easting_rounded_inc', 'Northing_m_inc','Easting_m_inc', 'IncGeo_WardNameNew_inc', 'IncGeo_WardName_inc', 'IncGeo_WardCode_inc',
                         'ProperCase_inc', 'IncGeo_BoroughCode_inc', "USRN_inc","UPRN_inc",'Postcode_full_inc', 'AddressQualifier_inc', 
                         'DateAndTimeReturned_mob','Notional Cost (£)_inc', 'NumCalls_inc', 'PropertyType_inc' ,'Postcode_district_inc', 'PropertyCategory_inc', 
                         'FirstPumpArriving_DeployedFromStation_inc', 'FirstPumpArriving_AttendanceTime_inc','severerisk', 'windgust', 'preciptype']

clean_data = data.drop(columns = not_selected_features)

specialServiceTypeValues = clean_data['SpecialServiceType_inc'].value_counts().index

def addingSpecialServiceTypeIfNotExist(X):
  if X['SpecialServiceType_inc'] in specialServiceTypeValues:
    return X
  else :
    X['SpecialServiceType_inc'] = X['StopCodeDescription_inc']
    return X

clean_data = clean_data.apply(addingSpecialServiceTypeIfNotExist,axis = 1)
clean_data = clean_data.drop(columns = ['StopCodeDescription_inc'])
clean_data['DelayCodeId_mob'] = clean_data['DelayCodeId_mob'].fillna(value = 0)
clean_data["DelayCode_Description_mob"].fillna("No delay registred", inplace = True)

ratio_null_values_clean_data = round(100 * clean_data.isna().sum().sum() / (clean_data.shape[0]*data.shape[1]),2)
ratio_obs_without_null_values_clean_data = round(100 * (np.where(clean_data.isna().sum(axis = 1) != 0, 0, 1).sum() / clean_data.shape[0]),2)
num_obs_without_null_values_clean_data = round(( ratio_obs_without_null_values_clean_data / 100 ) * clean_data.shape[0])



flash_data_values = pd.DataFrame({
    'num_features': [num_features],
    'num_observations': [num_observations],
    'ratio_null_values': [ratio_null_values],
    'ratio_null_values_clean_data': [ratio_null_values_clean_data],
    'ratio_obs_without_null_values_clean_data': [ratio_obs_without_null_values_clean_data],
    'num_obs_without_null_values_clean_data': [num_obs_without_null_values_clean_data]
})
flash_data_values.to_csv('data/flash_data_values.csv', index=True)

flash_data_head = data.head(50)
flash_data_head.to_csv('data/flash_data_head.csv', index=True)


"""
"""
Chargement des données
"""

flash_data_head = pd.read_csv('data/flash_data_head.csv', index_col=0)
flash_data_values = pd.read_csv('data/flash_data_values.csv', index_col=0)

num_observations = flash_data_values['num_observations'][0]
num_features = flash_data_values['num_features'][0]
ratio_null_values_clean_data = flash_data_values['ratio_null_values_clean_data'][0]
ratio_null_values = flash_data_values['ratio_null_values'][0]
ratio_obs_without_null_values_clean_data = flash_data_values['ratio_obs_without_null_values_clean_data'][0]
num_obs_without_null_values_clean_data = flash_data_values['num_obs_without_null_values_clean_data'][0]



title = "Jeux de données"
sidebar_name = "Jeux de données"

def run():
    st.title(title)

    tab1, tab2 = st.tabs(['Architecture & Volumétrie', 'Valeurs nulles'])

    with tab1:
        col1, col2 = st.columns(2, gap = 'large')

        with col1 :
            st.dataframe(flash_data_head, height = 490)

        with col2:
            st.header('Architecture :')
            st.markdown(
                """
                - 4 sources de données :
                    * Données de mobilisation : Actualisées chaque mois
                    * Données d'accidents : Actualisées chaque mois
                    * Données de longitude et latitude des casernes de pompiers
                    * Données météorologiques 
                """)   

            st.header("Volumétrie :")
            st.markdown(
                f"""
                - {num_observations} observations
                - {num_features} features
                """)

    with tab2 :
        st.header('Intialement :')
        st.markdown(
            f"""
            - {ratio_null_values}% de valeurs nulles
            - Chaque observation a au moins une valeur nulle
            """
        )

        st.header('Après traitement :')
        st.markdown(
            f"""
            - {ratio_null_values_clean_data}% de valeurs nulles
            - {ratio_obs_without_null_values_clean_data}% des observations n'ont pas de valeur nulle ( {num_obs_without_null_values_clean_data} observations )
            """
        )