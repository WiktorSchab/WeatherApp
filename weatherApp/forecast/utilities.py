# File with functions for data formatting

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
            daily_temps[date] = (temp_c, description)

    return daily_temps
