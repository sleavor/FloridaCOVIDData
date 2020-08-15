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
    
    
