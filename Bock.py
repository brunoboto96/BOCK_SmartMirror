#''' This will be the main script to run, it will call the other scripts from here and do the layout'''
#Import packages
from tkinter import *
from PIL import Image, ImageTk
import os

#Import scripts
import Weather, DateTime, Location

# Classes
location = Location.Location()
weather = Weather.Weather()
date_time = DateTime.Date_Time()

# tries to get the location, if it can't it'll return [None, None]
lat_long = location.geo_location()

#weather_currently = weather.get_weather(lat_long[0], lat_long[1])#if weather can't be fetched, return will be 'unknown'
#print(weather_currently)

print(date_time.get_date_time())

# text sizes
xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18

# Colours
background = 'black'
textcolour = 'white'

class Clock_frame(Frame):
    def __init__(self, parent, *args, **kwargs):
        #Initialise
        Frame.__init__(self, parent, bg=background)
        #setting time label
        self.time_previous = ''
        self.time_Lbl = Label(self, font=('Helvetica', large_text_size), fg=textcolour, bg=background)
        self.time_Lbl.pack(side=TOP, anchor=E)
        #setting day of the week label
        self.day_of_week_previous = ''
        self.day_of_week_Lbl = Label(self, text=self.day_of_week_previous, font=('Helvetica', small_text_size), fg=textcolour, bg=background)
        self.day_of_week_Lbl.pack(side=TOP, anchor=E)
        #setting date label
        self.date_previous = ''
        self.date_Lbl = Label(self, text=self.date_previous, font=('Helvetica', small_text_size), fg=textcolour, bg=background)
        self.date_Lbl.pack(side=TOP, anchor=E)
        self.push_time()

    def push_time(self):
        date_time_data = date_time.get_date_time()
        time_now = date_time_data['time']
        date_now = date_time_data['date']
        day_of_week_now = date_time_data['day']
        if time_now != self.time_previous:
            self.time_previous = time_now
            self.time_Lbl.config(text=time_now)
        if day_of_week_now != self.day_of_week_previous:
            self.day_of_week_previous = day_of_week_now
            self.day_of_week_Lbl.config(text=day_of_week_now)
        if date_now != self.date_previous:
            self.date_previous = date_now
            self.date_Lbl.config(text=date_now)
        self.time_Lbl.after(200, self.push_time)

class Weather_frame(Frame):
    def __init__(self, parent, *args, **kwargs):
        #Initialise
        Frame.__init__(self, parent, bg=background)
        #setting weather label
        self.temperature_previous = ''
        self.currently_previous = ''
        #self.icon = ''
        print("init")

        self.temperatureLbl = Label(self, font=('Helvetica', large_text_size), fg=textcolour, bg=background)
        self.temperatureLbl.pack(side=TOP, anchor=E)

        #self.iconLbl = Label(self, bg=background)
        #self.iconLbl.pack(side=TOP, anchor=E, padx=50)

        self.currentlyLbl = Label(self, font=('Helvetica', medium_text_size), fg=textcolour, bg=background)
        self.currentlyLbl.pack(side=TOP, anchor=E)
        self.push_weather()

    def push_weather(self):
        print("getting weather")
        weather_data = weather.get_weather(lat_long[0], lat_long[1])
        print(weather_data)
        temperature_now = weather_data['tempurature']
        currently_now = weather_data['current_weather']

        if self.currently_previous != currently_now:
            self.currently_previous = currently_now
            self.currentlyLbl.config(text=currently_now)

        if self.temperature_previous != temperature_now:
            self.temperature_previous = temperature_now
            self.temperatureLbl.config(text=temperature_now)

        self.after(60000, self.push_weather)

class Greeting_Frame(Frame):
    def __init__(self, parent, *args, **kwargs):
        #Initialise
        print("init")
        Frame.__init__(self, parent, bg=background)
        #text label
        self.greetingLbl = Label(self, font=('Helvetica', large_text_size), fg=textcolour, bg=background)
        self.greetingLbl.pack(side=TOP)
        self.greetingLbl.config(text='Greetings, human')

class Picture_Frame(Frame):
    def __init__(self, parent, *args, **kwargs):
        #Initialise
        print("init")
        Frame.__init__(self, parent, bg=background)

        image = Image.open("assets/Cute_doggo.jpg")
        image = image.resize((200, 200), Image.ANTIALIAS)
        image = image.convert('RGB')
        photo = ImageTk.PhotoImage(image)

        self.iconLbl = Label(self, bg='black', image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=N)

class Full_Screen():
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background=background) # set the back ground to black, this is needed for the reflection to work properly
        self.state = False

        # set up the frames
        self.topFrame = Frame(self.tk, background=background)
        self.bottomFrame = Frame(self.tk, background=background)
        #self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        #self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.topFrame.grid(row=0,column=0,sticky="ew")
        self.bottomFrame.grid(row=3,column=0,sticky="nsew")


        # fullscreen
        self.toggle_fullscreen()  # start in fullscreen
        self.tk.bind("<Control-f>", self.toggle_fullscreen)  # ctrl+f to toggle fullscreen
        self.tk.bind("<Escape>", self.end_fullscreen)

        self.greetings_frame = Greeting_Frame(self.topFrame)
        self.greetings_frame.grid(row=0, column=1, sticky="nsew")

        self.picture_frame = Picture_Frame(self.topFrame)
        self.picture_frame.grid(row=0,column=0,sticky="nsew")

        # clock
        self.clock_frame = Clock_frame(self.topFrame)
        #self.clock_frame.pack(side=RIGHT, anchor=NE, padx=50, pady=50)
        self.clock_frame.grid(row=0, column=2, sticky="e")
        # weather
        self.weather_frame = Weather_frame(self.topFrame)
        #self.weather_frame.pack(side=RIGHT, anchor=E, padx=50, pady=50)
        self.weather_frame.grid(row=1, column=2, sticky="e")



    def toggle_fullscreen(self, event=None):    # this is called when ctrl+f is pressed, it'll toggle the full screen
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):   # this is called if esc is pressed, this will make the screen smaller
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def calender(self):
        print('stuff needs to go here')



w = Full_Screen()
w.tk.mainloop()