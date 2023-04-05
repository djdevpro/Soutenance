import streamlit as st
import json
import networkx as nx
from streamlit_ace import st_ace
from labs import st_labs




title = "Laboratoire"
sidebar_name = "Laboratoire"

class CodeGenerator:
    def __init__(self, json_data):
        self.json_data = json_data
        self.imports = []
        self.code_blocks = []
    
    def generate_code(self):
        for node in self.json_data:
            if 'elm' in node:

                if node['elm'] == 'DataSource':
                    self.imports.append('import pandas as pd')
                    self.imports.append('import numpy as np')
                    self.code_blocks.append(' ')     
                    self.code_blocks.append('df = pd.read_csv("preprocessed_data_without_delay2.csv")')
                
                if node['elm'] == 'Time Series Split': 
                    self.code_blocks.append(' ')     
                    self.code_blocks.append('df.index = pd.to_datetime(df["DateAndTimeMobilised_mob"])')
                    self.code_blocks.append('df = df.drop(columns=["DateAndTimeMobilised_mob"])')  
                    self.code_blocks.append(' ')                    
                    self.code_blocks.append('start_date_model = "2020-01-01 00:00:00"')
                    self.code_blocks.append('start_date = "2022-12-04 00:00:00"')
                    self.code_blocks.append('end_date = "2022-12-05 00:00:00"')
                    self.code_blocks.append('df_start_date_model = df[df.index >= start_date_model]') 
                    self.code_blocks.append(' ')     
                
                if node['elm'] == 'Target Encoding':
                    self.code_blocks.append('target = "AttendanceTimeSeconds_mob"')
                    self.code_blocks.append(' ')    

                if node['elm'] == 'Features':
                    self.code_blocks.append('df_model = df_start_date_model[["AttendanceTimeSeconds_mob", "IncGeo_BoroughName_inc", "short_distance", "long_distance", "SpecialServiceType_inc", "Resource_Code_mob", "DeployedFromStation_Code_mob", "PumpOrder_mob", "hour", "dayofweek"]].copy()')
                    self.code_blocks.append(' ')
                
                if node['elm'] == 'Dummies':
                    self.code_blocks.append('df_model = pd.get_dummies(df_model, columns=["IncGeo_BoroughName_inc", "SpecialServiceType_inc","Resource_Code_mob", "DeployedFromStation_Code_mob"], drop_first=True)')
                
                if node['elm'] == 'Standard Scaler ':
                    self.code_blocks.append('scaler = StandardScaler()')
                    self.code_blocks.append('df_model["PumpOrder_mob"] = scaler.fit_transform(df_model[["PumpOrder_mob"]])')
                    self.code_blocks.append('df_model["hour"] = scaler.fit_transform(df_model[["hour"]])')
                    self.code_blocks.append('df_model["dayofweek"] = scaler.fit_transform(df_model[["dayofweek"]])')

                if node['elm'] == 'Time Series Split': 
                    self.code_blocks.append('train = df_model[df_model.index <= start_date]')
                    self.code_blocks.append('test = df_model[(df_model.index >= start_date) & (df_model.index <= end_date)]')
                    self.code_blocks.append('X_train = train.drop(target, axis=1)')
                    self.code_blocks.append('y_train = train[target]')
                    self.code_blocks.append('X_test = test.drop(target, axis=1)')
                    self.code_blocks.append('y_test = test[target]')
                    self.code_blocks.append(' ')
                
                if node['elm'] == 'xgBoost':
                    self.imports.append('import xgboost as xgb')

                    self.code_blocks.append('reg = xgb.XGBRegressor(n_estimators=400, max_depth=10, learning_rate=0.1, objective="reg:squarederror")')
                    self.code_blocks.append('reg.fit(X_train, y_train)')
                    self.code_blocks.append(' ')
                    self.code_blocks.append('y_train_pred = reg.predict(X_train)')
                    self.code_blocks.append('y_test_pred = reg.predict(X_test)')
                    self.code_blocks.append(' ')
                    self.code_blocks.append('test_mse = mean_squared_error(y_test, y_test_pred)')
                    self.code_blocks.append('train_mse = mean_squared_error(y_train, y_train_pred)')
                
                if node['elm'] == 'Scores':
                    
                    self.imports.append('import matplotlib.pyplot as plt')
                    self.imports.append('import seaborn as sns')
                    self.imports.append('from sklearn.metrics import r2_score, f1_score, confusion_matrix,explained_variance_score')
                    self.imports.append('from joblib import dump, load')
                    self.imports.append('from sklearn.metrics import mean_squared_error, explained_variance_score')
                    
                    self.code_blocks.append(' ')
                    self.code_blocks.append('r2 = r2_score(y_test, y_test_pred)')
                    self.code_blocks.append('print(f"R2 Score: {r2:.2f}")')
                    self.code_blocks.append('evs = explained_variance_score(y_test, y_test_pred)')
                    self.code_blocks.append('print(f"Explained Variance Score: {evs:.2f}")')
                    self.code_blocks.append(' ')


        return {'import': self.imports, 'code': self.code_blocks}
    def code(self):
        code = self.generate_code()
        code_import = "\n".join(code['import'])
        code_code = "\n".join(code['code'])
        return f"{code_import}\n\n{code_code}"
    

        

def run():

    
    st.write("""<style>
        div[data-baseweb="tab-list"] {
            gap: 1rem;
        }
        div[data-baseweb="tab-list"] p {
        font-size: 14px;
        letter-spacing: inherit;
        }</style>
    """, unsafe_allow_html=True)
    
    # Open and read the JSON file
    with open("data/clientData2.json", "r") as f:
        data = json.load(f)

    # Serialize the JSON data
    json_data = json.dumps(data)

    tab1,tab2 = st.tabs(['Diagramme', 'Générateur de code'])
    with tab1:
        
        labs = st_labs(json_data,'test', 0, 10, 5)
        
        if labs[0] != 5:
            labs = json.loads(labs)
            with open("data/clientData2.json", "w") as f:
                json.dump(labs, f)
    with tab2:

        data = json.loads(json_data)
        # Créer un graphe à partir des données
        G = nx.Graph()
        for node in data:
            if isinstance(node, dict):
                # Add node with attributes if the node is a dictionary
                G.add_node(node['id'], **node)
            else:
                # Add node without attributes if the node is a string or integer
                G.add_node(node)

        # Tri des noeuds par ordre alphabétique des IDs
        node_ids = sorted(list(G.nodes()))
        sorted_nodes = []
        for node_id in node_ids:
            node_data = G.nodes[node_id]
            sorted_nodes.append((node_id, node_data))

        # Tri des arêtes par ordre alphabétique des IDs des noeuds de départ
        sorted_edges = sorted(list(G.edges()), key=lambda x: (x[0], x[1]))

        # Créer un dictionnaire de noeuds trié
        nodes = {}
        for node in sorted_nodes:
            nodes[node[0]] = node[1]

        # Créer un tableau final avec les noeuds et les arêtes triés
        final_table = []
        for node_id in node_ids:
            final_table.append(nodes[node_id])
        for edge in sorted_edges:
            final_table.append({"source": edge[0], "target": edge[1]})

        c = CodeGenerator(final_table)
        code = c.code()



        # add json_data to the editor
        # Spawn a new Ace editor
        content = st_ace(
            value=code,
            language="python",
            )

        content
        