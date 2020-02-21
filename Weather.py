#''' This is the weather script, bock will pull this '''

import pyowm
import logging

class Weather():

    def get_weather(self,latitude,longitude):
        try:
            owm = pyowm.OWM('6892fc37f53067a561bbac518117974d')
            observation = owm.weather_at_coords(latitude, longitude)
            w = observation.get_weather()
            temp = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
            temp = temp['temp']
            degree_sign = u'\N{DEGREE SIGN}'
            temperature = "{0},{1}".format(temp, degree_sign)
            current_weather = w.get_detailed_status()
            print('weather')
        except Exception as e:
            logging.error(e)
            temp = 'unknown'
            current_weather = 'unknown'
            temperature = 'unknown'

        dict = {'tempurature': temperature, "current_weather": current_weather, "temp_no_symbol": temp}
        return dict
