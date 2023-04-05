import streamlit as st
import datetime
from streamlit.components.v1 import html
import haversine as hs

title = "Temps de réponse"
sidebar_name = "Temps de réponse - Régression"



from streamlit_folium import st_folium
import folium

from folium.plugins import Draw

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, accuracy_score, classification_report, r2_score, f1_score, confusion_matrix
from joblib import dump, load


def distance_haversine(x):
    loc1 = (x['Latitude_inc'], x['Longitude_inc'])
    loc2 = (x['station_latitude'], x['station_longitude'])
    return hs.haversine(loc1, loc2, unit = 'm')

def distance_manhattan(x):
    loc1 = (x['Latitude_inc'], x['Longitude_inc'])
    loc_int = (x['Latitude_inc'], x['station_longitude'])
    loc2 = (x['station_latitude'], x['station_longitude'])
    return hs.haversine(loc1, loc_int, unit = 'm') + hs.haversine(loc_int, loc2, unit = 'm')

def generate_short_distance(x):
    if x < 200:
      return x
    else:
      return 0

def generate_long_distance(x):
    if x < 200:
      return 0
    else:
      return x

def run():
    
    st.session_state.valid = False
    
    placeholder = st.empty()

    
    import json

    """

    df = pd.read_csv("data/preprocessed_data_without_delay.csv",
                    index_col='DateAndTimeMobilised_mob',
                    parse_dates=['DateAndTimeMobilised_mob'])
    #unique df_pumpOrder_mob                    

    df = df[df.index >= "2022-01-01 00:00:00"]
    df_pumpOrder_mob =  df['PumpOrder_mob'].unique()
    df_pumpOrder_mob = df_pumpOrder_mob.tolist()
    df_pumpOrder_mob.sort()    
    
    list_unique_date_ymd = df.index.strftime('%Y-%m-%d').unique()
    list_unique_date_ymd = list_unique_date_ymd.tolist()
    list_unique_date_ymd.sort()


    list_unique_date_ym = df.index.strftime('%Y-%m').unique()
    list_unique_date_ym = list_unique_date_ym.tolist()
    list_unique_date_ym.sort()

    IncGeo_BoroughName_inc = df['IncGeo_BoroughName_inc'].unique()
    IncGeo_BoroughName_inc = IncGeo_BoroughName_inc.tolist()
    IncGeo_BoroughName_inc.sort()    

    SpecialServiceType_inc = df['SpecialServiceType_inc'].unique()
    SpecialServiceType_inc = SpecialServiceType_inc.tolist()
    SpecialServiceType_inc.sort()

    Resource_Code_mob = df['Resource_Code_mob'].unique()
    Resource_Code_mob = Resource_Code_mob.tolist()
    Resource_Code_mob.sort()

    DeployedFromStation_Code_mob = df['DeployedFromStation_Code_mob'].unique()
    DeployedFromStation_Code_mob = DeployedFromStation_Code_mob.tolist()
    DeployedFromStation_Code_mob.sort()

    PumpOrder_mob = df['PumpOrder_mob'].unique()
    PumpOrder_mob = PumpOrder_mob.tolist()
    PumpOrder_mob.sort()
    
    data = {
        'df_pumpOrder_mob': df_pumpOrder_mob,
        'list_unique_date_ymd': list_unique_date_ymd,
        'list_unique_date_ym': list_unique_date_ym,
        'IncGeo_BoroughName_inc': IncGeo_BoroughName_inc,
        'SpecialServiceType_inc': SpecialServiceType_inc,
        'Resource_Code_mob': Resource_Code_mob,
        'DeployedFromStation_Code_mob': DeployedFromStation_Code_mob,
        'PumpOrder_mob': PumpOrder_mob
    }

    json_data = json.dumps(data)

    with open('data/features.json', 'w') as f:
        f.write(json_data)

    
    st.write(json_data)

    """
    
    with open('data/features_cat.json', 'r') as f:
        data = f.read()
    fcat = pd.DataFrame(json.loads(data))
    fcat = fcat

    stations_url = 'data/stations.csv'
    stations_df = pd.read_csv(stations_url, index_col='borough')    
    
    stations_df.index = stations_df.index.str.replace('<br>','')
    stations_df.index = stations_df.index.str.replace('&nbsp;','')
    # remove html tags
    stations_df.index = stations_df.index.str.replace('<[^<]+?>', '')
    
    stations_df.index = stations_df.index.str.upper()
    

    


    with open('data/features.json', 'r') as f:
        data = f.read()
    df = json.loads(data)

        
    london_stations_url = 'data/stations_lat_long.csv'
    london_stations_df = pd.read_csv(london_stations_url)    
    london_stations_df = london_stations_df.rename(columns = {'latitude': 'station_latitude', 'longitude': 'station_longitude'})
    london_stations_df.sort_values(by=['FirstPumpArriving_DeployedFromStation_inc'], inplace=True)
    
    


    df_pumpOrder_mob = pd.DataFrame(df['df_pumpOrder_mob'])
    list_unique_date_ymd =  pd.DataFrame(df['list_unique_date_ymd'])
    list_unique_date_ym =  pd.DataFrame(df['list_unique_date_ym'])
    IncGeo_BoroughName_inc =  pd.DataFrame(london_stations_df['FirstPumpArriving_DeployedFromStation_inc'])
    SpecialServiceType_inc =  pd.DataFrame(df['SpecialServiceType_inc'])
    Resource_Code_mob =  pd.DataFrame(df['Resource_Code_mob'])
    DeployedFromStation_Code_mob =  pd.DataFrame(df['DeployedFromStation_Code_mob'])
    PumpOrder_mob =  pd.Series(df['PumpOrder_mob'])
    

    #min value 2022-11-01 list_unique_date_ymd 
    list_unique_date_ymd = list_unique_date_ymd[ (list_unique_date_ymd[0] > "2022-11-01" )]

    lat = london_stations_df['station_latitude'][0]
    lon = london_stations_df['station_longitude'][0]
    
    


    with st.container( ):
            
        st.title("⏱️"+title)
        st.write(
            """
            <style>            
            
                h1{
                    margin: 0 0 5px;
                    padding: 0;
                }

                .stButton{    
                    margin: -10px 0 0;
                }
            </style>
            """, unsafe_allow_html=True
        )
        ordre = 0
        service = 0
        
        col1, col2,col3 =  st.columns([1,1,1])
        with col1: 
            date_input = st.selectbox(
                'Date de l\'incident',
                list_unique_date_ymd,
                key='luyld'
            )
        with col2: 
            time_input = st.time_input('Heure de l\'incident', datetime.time(8, 45), key='time_input')        
        with col3: 
            IncGeo_BoroughName_inc_ = st.selectbox(
                'Zone de service des casernes',
                IncGeo_BoroughName_inc,
                key='borough'
            )    
        
        col1, col2,col3,col4 =  st.columns([1,1,1,1])
        
        with col1: 
            
            geoB = stations_df[(stations_df['name'] == IncGeo_BoroughName_inc_)].index
            zone = fcat[geoB]
            zone.dropna(inplace=True)
            zone_list = zone.index
            
            SpecialServiceType_inc_ = st.selectbox(
                'Type de service',
                zone_list,
                key='service'
            )
        with col2:
            Resource_Code = pd.DataFrame(fcat.T[SpecialServiceType_inc_].T[geoB])
            Resource_Code = pd.DataFrame(Resource_Code[SpecialServiceType_inc_])
            Resource_Code_ = Resource_Code.values[0][0]
            Resource_Code_ = [x for x in Resource_Code_]
            
            Resource_Code_mob_ = st.selectbox(
                'Resource',
                Resource_Code_,
                key='resource'
            )
        with col3:
            r = Resource_Code.values[0][0]
            
            
            DeployedFromStation_Code_mob_ = st.selectbox(
                'Station',
                r[Resource_Code_mob_],
                key='station'
            )
        with col4: 
            PumpOrder_mob_   = st.selectbox(
                'Ordre de déploiement',
                PumpOrder_mob,
                key='ordre'
            )
        
        st.write(
            """
            Ajouter un marqueur sur la carte <span><svg style="border: 1px solid #ccc; background: #f2f2f2;" version="1.0" xmlns="http://www.w3.org/2000/svg"
 width="25px" height="25px" viewBox="0 0 1280.000000 1006.000000"
 preserveAspectRatio="xMidYMid meet">
<g transform="translate(350.000000,1006.000000) scale(0.100000,-0.100000)"
fill="#999" stroke="none">
<path d="M2855 10054 c-276 -28 -392 -47 -590 -99 -853 -222 -1563 -798 -1958
-1590 -299 -600 -385 -1335 -232 -1975 76 -316 165 -524 413 -970 269 -484
315 -559 787 -1285 111 -170 256 -395 322 -500 768 -1214 1218 -2270 1474
-3459 15 -68 18 -62 44 64 104 524 325 1206 568 1755 302 682 612 1227 1260
2214 450 688 566 882 791 1331 253 502 304 636 370 960 69 340 65 774 -10
1150 -115 575 -417 1120 -860 1551 -471 457 -1078 743 -1774 834 -118 15 -516
28 -605 19z" stroke-linecap="round"/>
</g>
<circle cx="52%" cy="25%" r="130" fill="#fff"/>
</svg>
</span> autour de la zone de service pour calculer la distance. Par défaut l'incident est situé à Londre [51.528308,-0.3817765].
            """, unsafe_allow_html=True
        )


        london_stations_start = london_stations_df[london_stations_df['FirstPumpArriving_DeployedFromStation_inc'] == IncGeo_BoroughName_inc_]

        lat = london_stations_start['station_latitude']
        lon = london_stations_start['station_longitude']
        
        # center on London
        m = folium.Map(location=[lat,lon], zoom_start=10)
        

        # add marker select to map DeployedFromStation_Code_mob_ default 0
        folium.Marker(
            location=[lat, lon],
            popup= "Station "+london_stations_start['FirstPumpArriving_DeployedFromStation_inc'].values[0],
            icon=folium.Icon(color='red', icon='fire')
        ).add_to(m)
        
        folium.Circle(
            location=[lat, lon],
            radius=5000,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.1
        ).add_to(m)
        

        Draw(draw_options={"circle": False,"circlemarker":False,"rectangle":False,"polygon":False, "polyline": False },edit_options={"poly": {"allowIntersection": False}},).add_to(m)

        output = st_folium(m, width=700, height=200)
        
        valid = st.button('Valider')  
        if  valid == True:
            st.session_state.valid = True
    

    if st.session_state.valid == True:
        st.write("""
        <style>
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main > div > div:nth-child(1) > div > div:nth-child(3) > div{
        display: none;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.session_state.valid = 1   
        try:
            lat_2 = output['all_drawings'][0]['geometry']['coordinates'][1]
            lon_2 = output['all_drawings'][0]['geometry']['coordinates'][0]
        except:
            lat_2 = 51.528308
            lon_2 = -0.3817765
            
        lat = float(lat)
        lon = float(lon)
        lat_2 = float(lat_2)
        lon_2 = float(lon_2)

        lat_lon = pd.DataFrame({'Latitude_inc': [lat_2], 'Longitude_inc': [lon_2], 'station_latitude': [lat], 'station_longitude': [lon]})


        lat_lon['distance_haversine'] = ((lat_lon.apply(distance_haversine, axis = 1) / 10 ).astype(int))*10
        lat_lon['distance_manhattan'] = ((lat_lon.apply(distance_manhattan, axis = 1) / 10 ).astype(int))*10
        lat_lon['distance'] = (lat_lon['distance_haversine'] + lat_lon['distance_manhattan']) / 2
        

        date_input = pd.to_datetime(date_input)
        date_input_old = pd.to_datetime(date_input) - pd.DateOffset(days=1)

        start_date_model = '2020-01-01 00:00:00'
        start_date = date_input_old
        end_date = date_input

        dt = datetime.datetime.combine(date_input, time_input)
        dt = pd.to_datetime(dt)
        dt_hour = dt.hour
                
        lat_lon['short_distance'] = lat_lon['distance'].apply(generate_short_distance)
        lat_lon['long_distance'] = lat_lon['distance'].apply(generate_long_distance)

        df_model = pd.DataFrame({'IncGeo_BoroughName_inc': IncGeo_BoroughName_inc_,
                                    'SpecialServiceType_inc':SpecialServiceType_inc_,    
                                    'Resource_Code_mob': Resource_Code_mob_,
                                    'DeployedFromStation_Code_mob':DeployedFromStation_Code_mob_,
                                    'PumpOrder_mob': PumpOrder_mob_,
                                    'hour': dt.hour,
                                    'dayofweek': dt.dayofweek,
                                    'short_distance': lat_lon['short_distance'].values[0],
                                    'long_distance': lat_lon['long_distance'].values[0]
                                    },
                                    index=[dt])

        selected_data = df_model.copy()
        
        df_model = pd.get_dummies(df_model, columns=['IncGeo_BoroughName_inc', 'SpecialServiceType_inc',
                                'Resource_Code_mob', 'DeployedFromStation_Code_mob'])

        df_model['hour'] = df_model['hour'].apply(lambda x: (x - 0) / (23 - 0) * (1 - (-1)) + (-1))
        df_model['PumpOrder_mob'].apply(lambda x: (x - PumpOrder_mob.min()) / (PumpOrder_mob.max() - PumpOrder_mob.min()) * (1 - (-1)) + (-1))
        df_model['dayofweek'] = df_model['dayofweek'].apply(lambda x: (x - 0) / (6 - 0) * (1 - (-1)) + (-1))

        
        model = load('models/model_reg.joblib')
        model_features = model.get_booster().feature_names
        df_model = df_model.reindex(columns=model_features, fill_value=0)
        missing_features = set(model_features) - set(df_model.columns)
        df_model = df_model.drop(missing_features, axis=1)




        result = model.predict(df_model)



        st.title(title)

        # prediction = result last value
        prediction = result[0]

        prediction_max = prediction
        if prediction > 1000:
            prediction_max = 1000


        my_css = """
        /*GREENS: #4ac4ac, #399988, #0f4534, #0a1a17;*/
        * {
        margin: 0;
        padding: 0;
        }

        body,
        html {
        width: 100%;
        height: 100%;
        margin: 0px auto;
        background-color: #0a1a17;
    background: linear-gradient(180deg,#0a1a17 30%, #000000 100%);
        font-family: Verdana, Geneva, sans-serif;
        font-size: 12px;
        color: #ccc;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        }

        .container {
            position: relative;
            margin: 63px auto 50px auto;
            height: 165px;
            width: 330px;
            transform: scale(.95);
        }
        p{
    text-shadow: 0px 0px 3px #0fc62a;
}
        .output {
        line-height: 35px;
        width: 60px;
        height: 30px;
        background-color: #0f4534;
        border-radius: 60px 60px 0 0;
        position: absolute;
        top: 135px;
        left: 135px;
        text-align: center;
        }

        .initialValue {
        display: none;
        border: none;
        border-bottom: 1px solid #399988;
        color: #399988;
        width: 3em;
        background-color: transparent;
        margin: 1em auto;
        outline: none;
        font-size: 16px;
        text-align: center;
        }
        /*SVG*/

        svg {
        margin: 0px;
        padding: 0;
        cursor: pointer;
        border: 1px solid #0a1a17;
        }

        svg.focusable {
        border: 1px solid #0f4534;
        }

        .outline,
        .fill,
        .center,
        .needle,
        .scale,
        .output {
        pointer-events: none;
        }

        .outline {
        fill: #0f4534;
        }

        .fill {
        fill: #399988;
        }

        .needle {
        fill: #aa0000;
        }

        .scale {
        stroke: #aaa;
        }

        text {
        text-anchor: middle;
        dominant-baseline: alphabetic;
        font: 12px verdana, sans-serif;
        fill: #aaa;
        }
        """
        # Define your javascript
        my_js = """
        var containersRy = document.querySelector(".container");
        var svg = document.querySelector(".typeRange");
        var output = document.querySelector(".output");
        var outline = document.querySelector(".outline");
        var fill = document.querySelector(".fill");
        var center = document.querySelector(".center");
        var needle = document.querySelector(".needle");

        var initialValue = document.querySelector(".initialValue");

        var rad = Math.PI / 180;
        var NS = "http:\/\/www.w3.org/2000/svg";

        var W = parseInt(window.getComputedStyle(svg, null).getPropertyValue("width"));
        var offset = 40;
        var cx = ~~(W / 2);
        var cy = 160;

        var r1 = cx - offset;
        var delta = ~~(r1 / 4);

        var initVal = initialValue.value;

        var isDragging = false;

        var x1 = cx + r1,
        y1 = cy;
        var r2 = r1 - delta;

        var x2 = offset,
        y2 = cy;
        var x3 = x1 - delta,
        y3 = cy;

        function drawScale() {
        sr1 = r1 + 5;
        sr2 = r2 - 5;
        srT = r1 + 20;
        var scale = document.querySelector(".scale");
        clearRect(scale)
        var n = 0;
        for (var sa = -180; sa <= 0; sa += 18) {
            var sx1 = cx + sr1 * Math.cos(sa * rad);
            var sy1 = cy + sr1 * Math.sin(sa * rad);
            var sx2 = cx + sr2 * Math.cos(sa * rad);
            var sy2 = cy + sr2 * Math.sin(sa * rad);
            var sxT = cx + srT * Math.cos(sa * rad);
            var syT = cy + srT * Math.sin(sa * rad);

            var scaleLine = document.createElementNS(NS, "line");
            var scaleLineObj = {
            class: "scale",
            x1: sx1,
            y1: sy1,
            x2: sx2,
            y2: sy2
            };
            setSVGAttributes(scaleLine, scaleLineObj);

            scale.appendChild(scaleLine);

            var scaleText = document.createElementNS(NS, "text");
            var scaleTextObj = {
            class: "scale",
            x: sxT,
            y: syT,
            };
            setSVGAttributes(scaleText, scaleTextObj);
            proportion = n / 1200;
            scaleText.textContent = n * 100;
            scale.appendChild(scaleText);

            n++

        }

        }

        function drawInput(cx, cy, r1, offset, delta, a) {

        var d1 = getD1(cx, cy, r1, offset, delta);
        var d2 = getD2(cx, cy, r1, offset, delta, a);

        drawScale();

        outline.setAttributeNS(null, "d", d1);
        fill.setAttributeNS(null, "d", d2);

        drawNeedle(cx, cy, r1, a);
        }

        function updateInput(p, cx, cy, r1, offset, delta,initialValue=0) {

        var x = p.x;
        var y = p.y;
        var lx = cx - x;
        var ly = cy - y;

        var a = Math.atan2(ly, lx) / rad - 180;

        drawInput(cx, cy, r1, offset, delta, a);
        output.innerHTML = "";
        initialValue.value = Math.round((a + 180) / 1.8,2);
        }

        function getD1(cx, cy, r1, offset, delta) {

        var x1 = cx + r1,
            y1 = cy;
        var x2 = offset,
            y2 = cy;
        var r2 = r1 - delta;
        var x3 = x1 - delta,
            y3 = cy;
        var d1 =
            "M " + x1 + ", " + y1 + " A" + r1 + "," + r1 + " 0 0 0 " + x2 + "," + y2 + " H" + (offset + delta) + " A" + r2 + "," + r2 + " 0 0 1 " + x3 + "," + y3 + " z";
        return d1;
        }

        function getD2(cx, cy, r1, offset, delta, a) {
        a *= rad;
        var r2 = r1 - delta;
        var x4 = cx + r1 * Math.cos(a);
        var y4 = cy + r1 * Math.sin(a);
        var x5 = cx + r2 * Math.cos(a);
        var y5 = cy + r2 * Math.sin(a);

        var d2 =
            "M " + x4 + ", " + y4 + " A" + r1 + "," + r1 + " 0 0 0 " + x2 + "," + y2 + " H" + (offset + delta) + " A" + r2 + "," + r2 + " 0 0 1 " + x5 + "," + y5 + " z";
        return d2;
        }

        function drawNeedle(cx, cy, r1, a) {

        var nx1 = cx + 5 * Math.cos((a - 90) * rad);
        var ny1 = cy + 5 * Math.sin((a - 90) * rad);

        var nx2 = cx + (r1 + 15) * Math.cos(a * rad);
        var ny2 = cy + (r1 + 15) * Math.sin(a * rad);

        var nx3 = cx + 5 * Math.cos((a + 90) * rad);
        var ny3 = cy + 5 * Math.sin((a + 90) * rad);

        var points = nx1 + "," + ny1 + " " + nx2 + "," + ny2 + " " + nx3 + "," + ny3;
        needle.setAttributeNS(null, "points", points);
        }


        function clearRect(node) {
        while (node.firstChild) {
            node.removeChild(node.firstChild);
        }
        }

        function setSVGAttributes(elmt, oAtt) {
        for (var prop in oAtt) {
            elmt.setAttributeNS(null, prop, oAtt[prop]);
        }
        }

        // events
        window.addEventListener("load", function() {
        var pa = (initVal * 1.8) - 180;
        var p = {}
        p.x = cx + r1 * Math.cos(pa * rad);
        p.y = cy + r1 * Math.sin(pa * rad);
        updateInput(p, cx, cy, r1, offset, delta,initVal)
        }, false);

        initialValue.addEventListener("input", function() {
        var val = this.value;
        var newVal = (!isNaN(val) && val >= 0 && val <= 100) ? val : 18;
        var pa = (newVal * 1.8) - 180;
        var p = {}
        p.x = cx + r1 * Math.cos(pa * rad);
        p.y = cy + r1 * Math.sin(pa * rad);
        updateInput(p, cx, cy, r1, offset, delta,newVal)
        }, false);


        var container = document.querySelector(".warp");  
        setTimeout(function(){ container.style.display = "block"; }, 150);



        """

        # Wrapt the javascript as html code
        my_html = f"""
        
        <style>{my_css}</style>
        <div class="warp" style="display:none;">
        <div class="container A"  >
        <svg class="typeRange" height="165" width="330" view-box="0 0 330 165">

            <g class="scale" stroke="red"></g>

            <path class="outline" d="" />
            <path class="fill" d="" />
            <polygon class="needle" points="220,10 300,210 220,250 140,210" />
        </svg>
        <div class="output"></div>
        </div>

        <p>Temps de réponse calculé par le modèle : {round(prediction)}sc        </p>


        
        <input  type="text" class="initialValue" value="{round(prediction_max/10, 2)}" />
        </div>
        <script>{my_js}</script>"""
        col1, col2 = st.columns([2, 1])
        with col1:
            html(my_html, height=350)
            placeholder.empty()
        with col2:
            st.write("""
            <style>
            div[data-testid="stForm"] button[kind="secondaryFormSubmit"]{
                display: none;
            }
            div[data-testid="stForm"] {
                position: relative;
                padding: 0;
                margin: -16px 0 0 0;
                max-height: 353px;

            }
            </style>
            """,unsafe_allow_html=True)
            # add form
            form = st.form(key='my_form')
            with form:
                # center on London
                m2 = folium.Map(location=[lat,lon], zoom_start=9)
                

                # add marker select to map DeployedFromStation_Code_mob_ default 0
                folium.Marker(
                    location=[lat, lon],
                    popup= "Station "+london_stations_start['FirstPumpArriving_DeployedFromStation_inc'].values[0],
                    icon=folium.Icon(color='red', icon='fire')
                ).add_to(m2)
                
                folium.Circle(
                    location=[lat, lon],
                    radius=5000,
                    color='red',
                    fill=True,
                    fill_color='red',
                    fill_opacity=0.1
                ).add_to(m2)

                # add marker select to map DeployedFromStation_Code_mob_ default 0
                folium.Marker(
                    location=[lat_2, lon_2]
                ).add_to(m2)
                

                output2 = st_folium(m2, width=295, height=350)
            
                st.form_submit_button() 
                
        # input bouton retour
        if st.button('Retour'):
            st.session_state.retour = False
            st.session_state.valid = False
            st.experimental_rerun()

        # reprendre les variables IncGeo_BoroughName_inc_ etc

        st.write('**Valeurs de la zone sélectionnée**')
        st.write(selected_data)
        
        st.write('**Géolocalisation de la zone sélectionnée**')
        st.write(lat_lon)

        st.write('**Valeurs transmises au modèle**')
        st.write(df_model)
        st.write('**Valeurs prédites par le modèle**')
        st.write(f"**Prédiction :** {prediction}")
        # no decimal precision prediction

    else:
        
        st.write(
            """
            """
        )
        