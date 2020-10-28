import os

class Config:
  WEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
  WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production':ProdConfig
}            