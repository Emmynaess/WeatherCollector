# Weather Collector
A Python-based project to fetch weather forecasts from SMHI, save the data in an Excel file, and display forecasts in the terminal.

## Features
Fetch weather data from SMHI’s API.
Save weather data to an Excel file.
Display a weather forecast in the terminal with clear headings and colors.

## Installation
Follow these steps to install and run the project.

1. Clone or Download the Project
bash

```git clone https://github.com/Emmynaess/WeatherCollector.git```

cd weather-collector

3. Create and Activate a Virtual Environment
 
```python -m venv venv```

Activate by:

```source venv/bin/activate```

or

```venv\Scripts\activate```

5. Install Required Packages
Install the necessary Python packages by running:

```pip install -r requirements.txt```

### Required Packages:
requests: For making HTTP calls to SMHI’s API.

openpyxl: For creating and managing Excel files.

### Usage
Run the Program
Use the following command to run the program:

python main.py

### Menu Options
After starting the program, you’ll see the following options in the terminal:


MENU
1. Fetch latest data
2. Print forecast
9. Exit

Fetch Latest Data
Retrieves data from SMHI’s API and saves it in a file named 'Väderdata.xlsx.'

Print Forecast
Displays the latest 24-hour weather forecast in the terminal. The headers are color-coded in blue for better readability.

Exit
Closes the program.

Example Output
When you select option 2 (Print forecast), you’ll see something like this in your terminal:

Forecast from SMHI 2024-11-20:
Temperature      Hour            Rain/Snow      
1                10:00:00        No precipitation
15               11:00:00        Precipitation
-5               12:00:00        No precipitation
30               13:00:00        Precipitation
Temperature, Hour, and Rain/Snow are displayed in blue, while the rest of the output is in standard colors.

File Structure
The project files are organized as follows:

├── main.py                # Main file to run the program
├── smhi_api.py            # Functions to fetch and process data from SMHI
├── excel_utils.py         # Functions to create and manage Excel files
├── menu.py                # Menu handling and user interaction
├── requirements.txt       # List of required Python packages
└── Väderdata.xlsx         # Automatically generated to store weather data

### Requirements
Python 3.8 or later
Packages listed in requirements.txt (install using pip)


### Error Handling
Common Issues
File Väderdata.xlsx Not Found
If you try to print a forecast without first fetching data, the program will show this message:

You need to fetch data first by selecting option 1 from the menu.
Colors Not Displayed in the Terminal
If the text color doesn’t display as expected:

Ensure your terminal supports ANSI colors (most modern terminals do).
If you’re using a Windows terminal, PowerShell typically supports ANSI colors.


### Future Improvements
Add more API calls to include additional weather parameters, such as:
Wind speed
Humidity
Air pressure

Include graphical representations of weather forecasts in the Excel file.
Add an option to choose different coordinates directly from the menu.


### License
This project is free to use and modify. If you share it, please credit the source. 😊
