import requests
from datetime import datetime, timedelta

# Koordinater
LAT = 59.30
LON = 18.02
URL = f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{LON}/lat/{LAT}/data.json'

def get_data_from_smhi():
    response = requests.get(URL)
    response.raise_for_status()  # För att hantera API-fel
    return response.json()

def get_dates(smhi_data):
    return [datetime.strptime(item['validTime'].replace('T', ' ')[:-1], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            for item in smhi_data['timeSeries'][:24]]

def get_timestamp(smhi_data):
    return [(datetime.strptime(item['validTime'].replace('T', ' ')[:-1], '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%H:%M:%S')
            for item in smhi_data['timeSeries'][:24]]

def get_temperatures(smhi_data):
    return [float(param['values'][0]) 
            for item in smhi_data['timeSeries'][:24]
            for param in item['parameters'] if param['unit'] == 'Cel']

def get_rain_or_snow(smhi_data):
    return ['True' if param['values'][0] != 0 else 'False'
            for item in smhi_data['timeSeries'][:24]
            for param in item['parameters'] if param['name'] == 'pcat']
