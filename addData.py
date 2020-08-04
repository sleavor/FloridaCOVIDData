# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:49:05 2020

@author: Shawn Leavor
"""

import requests
import json
import pandas as pd
import datetime
from csv import writer
#import schedule
import time

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def addDataCSV():
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
    
    for county in counties:
        data = json.dumps({"state":state,"county":county})
        response = requests.post('https://covid19-us-api.herokuapp.com/county',data=data, headers=headers)
        text=response.json()
        csvList=[
            text['message'][0]['county_name'],
            text['message'][0]['state_name'],
            text['message'][0]['confirmed'],
            text['message'][0]['new'],
            text['message'][0]['death'],
            text['message'][0]['new_death'],
            text['message'][0]['fatality_rate'],
            text['message'][0]['latitude'],
            text['message'][0]['longitude'],
            text['message'][0]['last_update'],
            date
            ]
        append_list_as_row('countyData.csv', csvList)
        
addDataCSV()

'''schedule.every().day.at("10:16").do(addDataCSV)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
    '''