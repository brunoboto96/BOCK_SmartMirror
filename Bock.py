#''' This will be the main script to run, it will call the other scripts from here and do the layout'''
#Import packages
from tkinter import *
import os

#Import scripts
import Weather, DateTime, Location

# Classes
location = Location.Location()
weather = Weather.Weather()
date_time = DateTime.Date_Time()

# tries to get the location, if it can't it'll return [None, None]
lat_long = location.geo_location()

weather_currently = weather.get_weather(lat_long[0],lat_long[1])#if weather can't be fetched, return will be 'unknown'
print(weather_currently)

print(date_time.get_date_time())

# text sizes
xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18

# Colours
background = 'black'

class Full_Screen():
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background=background) # set the back ground to black, this is needed for the reflection to work properly
        self.state = False

        #set up the screens
        self.topFrame = Frame(self.tk, background=background)
        self.bottomFrame = Frame(self.tk, background=background)
        #self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        #self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)

        #fullscreen
        self.toggle_fullscreen()  # start in fullscreen
        self.tk.bind("<Control-f>", self.toggle_fullscreen)  # ctrl+f to toggle fullscreen
        self.tk.bind("<Escape>", self.end_fullscreen)

        #clock
        self.clock()


    def toggle_fullscreen(self, event=None):    # this is called when ctrl+f is pressed, it'll toggle the full screen
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):   # this is called if esc is pressed, this will make the screen smaller
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def clock(self):
        print('stuff needs to go here')

    def weather(self):
        print('stuff needs to go here')

    def calender(self):
        print('stuff needs to go here')
        


w = Full_Screen()
w.tk.mainloop()