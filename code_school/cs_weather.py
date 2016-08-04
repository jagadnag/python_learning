import requests

def get_weather_forecast():
    # Connecting to the weather api
    url = 'http://api.openweathermap.org/data/2.5/weather?id=5391959&units=imperial&APPID=c9a60a2572bcaa2c5fc7edfd1b2bfe42'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # Parsing the JSON output from API
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Printing the weather forecast
    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return (forecast)