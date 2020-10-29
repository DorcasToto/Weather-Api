import urllib.request,json
from flask import jsonify

# Getting api key
api_key = None
# Getting the weather base url
weather_url = None

def configure_request(app):
    global api_key,weather_url
    api_key = app.config['WEATHER_API_KEY']
    weather_url = app.config['WEATHER_BASE_URL']
    

def getWeather(search):
    get_weather_url = weather_url.format(search,api_key)
    with urllib.request.urlopen(get_weather_url) as url:
        getWeatherData = url.read()
        data = json.loads(getWeatherData)
        rewq = json.dumps({"Weather": data})
        # print(data)
        return rewq
