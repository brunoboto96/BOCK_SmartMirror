#''' This will be the main script to run, it will call the other scripts from here and do the layout'''
#Import packages
import tkinter
import os

#Import scripts
import Weather, DateTime, Location

# Classes
location = Location.Location()
weather = Weather.Weather()

# tries to get the location, if it can't it'll return None
lat_long = location.location()



weather_currently = weather.get_weather(lat_long[0],lat_long[1])
print(weather_currently)