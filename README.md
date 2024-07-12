
# WeatherApp

Simple weather forecast application built with Django using the OpenWeather API.




## Tech used

- Python
- Django (python Framework)
- Openweathermap API
- Bootstrap Icons
## Requirements
- Python 3.10.11 or newer
- Openweathermap API key

## Installation

- Clone the repository from GitHub

    ```bash
    git clone https://github.com/WiktorSchab/WeatherApp.git
    cd WeatherApp
    ```
- Create a virtual environment

    ```bash
    python -m venv venv
    ```
- Activate the virtual environment

    ```bash
    source venv/bin/activate  # For Linux
    venv/Scripts/activate   # For Windows
    ```
- Install all required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration
- Navigate to the settings directory:
    ```bash
    cd weatherApp/settings
    ```
- Copy '.env.example' to '.env':

    ```bash
    cp .env.example .env
    ```
- Set data in '.env' to suit your needs:

- Navigate back to the 'weatherApp' directory
    ```bash
    cd ../
    ```
- Create a file named 'api_key' and paste your OpenWeatherMap API key:
    ```bash
    echo 'API key' > api_key
    ```

## Running App (locally)
##### Ensure you are in the same location as 'manage.py'
- Make migrations **(only on first run)**:
    ```bash
    python manage.py migrate
    ```
- Run the local server:

    ```bash
    python manage.py runserver
    ```
- Open your browser and go to the address 'http://127.0.0.1:8000/'
 
## Usage
- Enter city name in the input field. To specify the city better, you can enter the country name after a comma (the country name doesn't have to be in English).
![searchingField](https://github.com/WiktorSchab/WeatherApp/assets/73139165/6f51d5b7-cdb1-4cc2-a114-8607f1c6300f)
*<div align="center">Screenshot 1: Input form for entering the city name.</div><br/><br/>*


- Read the weather conditions for a specific hour by moving the cursor over a dot on the chart.
![chart2](https://github.com/WiktorSchab/WeatherApp/assets/73139165/8314221b-77ed-4d08-9e76-3d2865fd06a7)
*<div align="center">Screenshot 2: Chart showing temperature and weather condition on 6:00.</div><br/><br/>*


- To check the weather on another day, click on the small boxes below the chart. Each box has a short name for the weekday (Mon - Monday, Wed - Wednesday, etc.).
![otherDay](https://github.com/WiktorSchab/WeatherApp/assets/73139165/945acd5b-69a9-47fb-b7e4-849df7e81df6)
*<div align="center">Screenshot 3: Chart showing data after clicking box with 'Tue' inscription above it.</div><br/><br/>*

## Notes
- Ensure you have an active internet connection, as the application fetches data from an external API.
- If you encounter issues connecting to the API, check your API key and ensure it is correct and active.
