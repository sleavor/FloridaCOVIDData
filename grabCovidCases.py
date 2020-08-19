# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:01:18 2020

@author: Shawn Leavor
"""

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from csv import writer
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot



headers = {'Content-type': 'application/json'}
p = requests.get('https://covidtracking.com/api/us/daily')
x=p.json()
df = pd.read_json(json.dumps(x))
df['date']=pd.to_datetime(df['date'], format='%Y%m%d')

deathRate = df['death']/df['positive']
hospRate = df['hospitalized']/df['positive']

xaxis=df['date']
yaxis=df['death']
yaxis2=df['positive']
yaxis3=deathRate
yaxis4=hospRate

#plt.scatter(xaxis,yaxis, s=1.5)
#plt.scatter(xaxis,yaxis2, color='red', s=1.5)
plt.scatter(xaxis,yaxis3, color='green', label='death rate', s=1.5)
plt.scatter(xaxis,yaxis4, color='black', label='hospitilization rate', s=1.5)


plt.title('Rates per Case')
plt.xlabel('Date')
plt.ylabel('Rate')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


#This is for daily county data
headers = {'Content-type':'application/json'}
counties = ['Alachua',
'Baker',
'Bay',
'Bradford',
'Brevard',
'Broward',
'Calhoun',
'Charlotte',
'Citrus',
'Clay',
'Collier',
'Columbia',
'DeSoto',
'Dixie',
'Duval',
'Escambia',
'Flagler',
'Franklin',
'Gadsden',
'Gilchrist',
'Glades',
'Gulf',
'Hamilton',
'Hardee',
'Hendry',
'Hernando',
'Highlands',
'Hillsborough',
'Holmes',
'Indian River',
'Jackson',
'Jefferson',
'Lafayette',
'Lake',
'Lee',
'Leon',
'Levy',
'Liberty',
'Madison',
'Manatee',
'Marion',
'Martin',
'Miami-Dade',
'Monroe',
'Nassau',
'Okaloosa',
'Okeechobee',
'Orange',
'Osceola',
'Palm Beach',
'Pasco',
'Pinellas',
'Polk',
'Putnam',
'Santa Rosa',
'Sarasota',
'Seminole',
'St. Johns',
'St. Lucie',
'Sumter',
'Suwannee',
'Taylor',
'Union',
'Volusia',
'Wakulla',
'Walton',
'Washington']
state = 'FL'
date = datetime.date.today().strftime('%Y/%m/%d')
    
countyData = pd.read_csv('countyData.csv')

for county in counties:
    countysData = countyData[countyData['county_name'].str.contains(county)]
    countysData['SMA_3'] = countysData.iloc[:,3].rolling(window=3).mean()
    y = countysData['new']
    y2 = countysData['SMA_3']
    x = countysData['date']
    plt.scatter(x,y,label='Daily Cases')
    plt.plot(x,y2, label='3-day MA')
    plt.title(county)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

#Plot on state map
#Plot on state map
init_notebook_mode()

florida_data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/florida_county_data.geojson'
florida_data = pd.read_json(florida_data_url)

county_list = []
counties_aligned = []

for county in florida_data['features']:
    county_list.append(county)
    counties_aligned.append(county['properties']['name'][0:-11])

growCounties = {"type": "FeatureCollection"}
growCounties['features'] = []

fallCounties = {"type": "FeatureCollection"}
fallCounties['features'] = []

neutralCounties={"type": "FeatureCollection"}
neutralCounties['features'] = []

for i in range(len(county_list)):
    countysData = countyData[countyData['county_name'].str.contains(counties_aligned[i])]
    countysData['SMA_3'] = countysData.iloc[:,3].rolling(window=3).mean()
    s=countysData['SMA_3']
    if s.iloc[-1]>s.iloc[-3]:
        growCounties['features'].append(florida_data['features'][i])
    elif s.iloc[-1]<s.iloc[-4]:
        fallCounties['features'].append(florida_data['features'][i])
    else:
        neutralCounties['features'].append(florida_data['features'][i])
        

mapbox_access_token = "pk.eyJ1Ijoic2xlYXZvciIsImEiOiJja2R2enQyb2swcXlkMndub252MmNiamxqIn0.BMf_fuTYk-97vdtYNd0j0A"

data = go.Scattermapbox(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
    )

layout = go.Layout(
    height=600,
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        layers=[
            dict(
                sourcetype = 'geojson',
                source = growCounties,
                type = 'fill',
                color = 'rgba(163,22,19,0.8)'
            )
        ],
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=27.8,
            lon=-83
        ),
        pitch=0,
        zoom=5.2,
        style='light'
    ),
)

fig = dict(data=data, layout=layout)
iplot(fig, filename='county-level-choropleths-python')

