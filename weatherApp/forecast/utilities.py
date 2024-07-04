# File with functions for data formatting
from datetime import datetime, timedelta

import pycountry
from googletrans import Translator


today_date = datetime.now().date()
tomorrow_date = today_date + timedelta(days=1)


def add_weekday_to_weather_data(weather_data):
    updated_weather_data = {}
    for date_str, (temperature, description, icon) in weather_data.items():
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        weekday = date_obj.strftime('%A')
        icon = icon + '.png'
        updated_weather_data[date_str] = (temperature, description, weekday, icon)

    return updated_weather_data


def get_daily_temps(forecast_list):
    """
    The get_daily_temps function extracts and converts the temp at noon from a forecast list in Kelvin to Celsius,
    including the weather description for each date.

    It returns a dictionary with dates as keys and tuples of temperature in Celsius and weather descriptions as values.
    """
    daily_temps = {}

    for forecast in forecast_list:
        dt_txt = forecast['dt_txt']
        date = dt_txt.split(' ')[0]
        time = dt_txt.split(' ')[1]

        if '12:00:00' in time:
            temp_k = forecast['main']['temp']
            temp_c = temp_k - 273.15  # Convert Kelvin to Celsius

            description = forecast['weather'][0]['description']
            icon = forecast['weather'][0]['icon']
            daily_temps[date] = (temp_c, description, icon)

    # Checking if today temps is in dict
    if str(today_date) not in daily_temps:
        forecast = forecast_list[0]
        dt_txt = forecast['dt_txt']
        date = dt_txt.split(' ')[0]

        temp_k = forecast['main']['temp']
        temp_c = temp_k - 273.15  # Convert Kelvin to Celsius

        description = forecast['weather'][0]['description']
        icon = forecast['weather'][0]['icon']

        # Adding today's temp on start of the dict
        today_temp = {date: (temp_c, description, icon)}
        daily_temps = {**today_temp, **daily_temps}

    daily_temps = add_weekday_to_weather_data(daily_temps)
    return daily_temps


def get_hour_weather(data):
    temp_data = {}  # Initialize an empty dictionary to hold the weather data grouped by date
    for i in data:
        # Convert temperatures from Kelvin to Celsius
        temp = i['main']['temp'] - 273.15
        temp_feels = i['main']['feels_like'] - 273.15

        # Extract weather information
        weather = i['weather'][0]['main']
        weather_description = i['weather'][0]['description']

        # Extract date and time from the datetime string
        dt_txt = i['dt_txt']
        date = dt_txt.split(' ')[0]
        time = dt_txt.split(' ')[1][0:5]

        # Create a dictionary with the relevant weather data
        data_to_add = {
            'temp': temp,
            'temp_feels': temp_feels,
            'weather': weather,
            'weather_description': weather_description,
            'time': time
        }

        # If the date is not already in the dictionary, add it with an empty list
        if date not in temp_data:
            temp_data[date] = []

        # Append the weather data to the list for the corresponding date
        temp_data[date].append(data_to_add)

    # Add data for hour 24:00 (copying data from next day's 00:00)
    dates = sorted(temp_data.keys())
    for i in range(len(dates) - 1):
        today = dates[i]
        tomorrow = dates[i + 1]

        # Find the weather data at 00:00 for the next day
        next_day_midnight_data = None
        for data_point in temp_data[tomorrow]:
            if data_point['time'] == '00:00:00':
                next_day_midnight_data = data_point
                break

        # If found, create a new entry with time 24:00 and add it to the current day
        if next_day_midnight_data:
            data_for_24 = next_day_midnight_data.copy()
            data_for_24['time'] = '24:00:00'
            temp_data[today].append(data_for_24)

    # Optional: Print the data for debugging purposes
    # for i in temp_data:
    #     print(i)
    #     for x in temp_data[i]:
    #         print(x['time'], x['temp'])
    #     print('\n------\n')
    return temp_data  # Return the dictionary containing the grouped weather data


# Function to get English name of the country
def get_english_country_name(country_name):
    translator = Translator()
    try:
        # Attempt to translate the country name to English
        result = translator.translate(country_name)

        # Returning value if translation was found and raising error if it was not
        if result is None:
            raise ValueError("Translation result is None")
        return result.text

    except Exception as e:
        print(f"Error: {e}")
        return None


# Function to get ISO 3166-1 alpha-2 country code (required by the OpenWeather API)
def get_iso_country_tag(country_name):
    try:
        # Getting iso tag of the country
        country_info = pycountry.countries.search_fuzzy(country_name)[0]
        country_iso = country_info.alpha_2
        return country_iso

    except LookupError:
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None
