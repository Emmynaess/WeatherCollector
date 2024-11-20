import time
import os
from datetime import datetime, timedelta
from smhi_api import get_data_from_smhi, get_dates, get_timestamp, get_temperatures, get_rain_or_snow
from excel_utils import append_data_to_excel, read_last_24_rows

def show_menu():
    while True:
        print("MENY")
        print("1. Hämta senaste data")
        print("2. Skriv ut prognos")
        print("9. Avsluta")

        val = input("Välj ett alternativ: ")

        if val == '1':
            handle_fetch_data()
        elif val == '2':
            handle_print_forecast()
        elif val == '9':
            print('Avslutar programmet ')
            break
        else:
            print('Ogiltligt val. Välj igen')

def handle_fetch_data():
    created = datetime.now()
    smhi_data = get_data_from_smhi()
    data_to_save = [
        [created, 18.02, 59.30, date, time, temp, rain, 'SMHI']
        for date, time, temp, rain in zip(
            get_dates(smhi_data), 
            get_timestamp(smhi_data), 
            get_temperatures(smhi_data), 
            get_rain_or_snow(smhi_data)
        )
    ]
    append_data_to_excel(data_to_save)
    print('\nPrognosdata har skrivits till Excel-filen.\n')

def handle_print_forecast():
    file_path = 'Väderdata.xlsx'
    if not os.path.isfile(file_path): 
        print("\nDu måste hämta data först genom att välja alternativ 1 i menyn.\n")
        return

    now = datetime.now()
    last_24_rows = read_last_24_rows()

    if len(last_24_rows) == 24:
        print(f'\nPrognos från SMHI {now.strftime("%Y-%m-%d")}:')
        
        header_color = "\033[94m" 
        reset_color = "\033[0m"   
        print(f"{header_color}{'Temperature':<15} {'Hour':<15} {'Rain/Snow':<15}{reset_color}")
        
        for row in last_24_rows:
            temp, hour, rain = row[5], row[4], row[6]
            rain_desc = 'Nederbörd' if rain == 'True' else 'Ingen nederbörd'
            print("{:<15} {:<15} {:<15}".format(temp, hour, rain_desc))
    else:
        print('Det finns inte tillräckligt med data i Excel-filen.')
