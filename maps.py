import googlemaps
from datetime import datetime
import json
import urllib.request
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import PIL.Image
import PIL.ImageTk
from tkinter import Label, Frame, Radiobutton, IntVar
import io
from xml.etree.ElementTree import parse

# get your api key @ google console -> APIS & Services -> credentials | after -> dashboard enable apis -> Directions, Geocoding, Maps Static API
apikey = ''
gmaps = googlemaps.Client(key=apikey)

# Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
tMode = ""

now = datetime.now()
directions_result = gmaps.directions("31 Upper George Street, Luton",
                                     "London",
                                     mode=tMode,
                                     departure_time=now)

# directions_result -> list -> len() == 1 | directions_result[0] -> dict | directions_result[0]["json_attr"]
# print(directions_result[0]["overview_polyline"]["points"])

directions_url = "https://maps.googleapis.com/maps/api/staticmap?size=600x400&path=enc%3A"
directions_url = directions_url + \
    directions_result[0]["overview_polyline"]["points"] + "&key=" + apikey
print(directions_url)


def reqDirections(tMode):
    if(tMode == ""):
        tMode = "driving"
    now = datetime.now()
    directions_result = gmaps.directions("31 Upper George Street, Luton",
                                         "Skimpot Rd Dunstable",
                                         mode=tMode,
                                         departure_time=now)

    # directions_result -> list -> len() == 1 | directions_result[0] -> dict | directions_result[0]["json_attr"]
    # print(directions_result[0]["overview_polyline"]["points"])

    directions_url = "https://maps.googleapis.com/maps/api/staticmap?size=600x400&path=enc%3A"
    directions_url = directions_url + \
        directions_result[0]["overview_polyline"]["points"] + "&key=" + apikey
    print(directions_url)

    # request data from url -> crawls for the first image and stores it
    raw_data = urllib.request.urlopen(directions_url).read()
    im = PIL.Image.open(io.BytesIO(raw_data))
    image = PIL.ImageTk.PhotoImage(im)

    # displays the img
    global labelMap
    labelMap.configure(image=image)
    global labelTimeToDestination
    if(tmode == "driving"):      
        labelTimeToDestination.configure(text=directions_result[0]["legs"][0]["duration_in_traffic"]["text"] + " - " + directions_result[0]["legs"][0]["distance"]["text"])
     
    labelTimeToDestination.configure(text=directions_result[0]["legs"][0]["duration_in_traffic"]["text"] + " - " + directions_result[0]["legs"][0]["distance"]["text"])
    root.update()


def go():
    print("goooooo")


# gui
root = tk.Tk()


# request data from url -> crawls for the first image and stores it
raw_data = urllib.request.urlopen(directions_url).read()
im = PIL.Image.open(io.BytesIO(raw_data))
image = PIL.ImageTk.PhotoImage(im)
labelMap = Label(root, image=image)

# displays the img
t = directions_result[0]["legs"][0]["duration_in_traffic"]["text"] + \
    " - " + directions_result[0]["legs"][0]["distance"]["text"]
labelTimeToDestination = Label(root, text=t)
Frame1 = Frame(root)
Frame1.place(relheight=0.468, relwidth=1)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#000000")
v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

tmodes = [
    ("Driving"),
    ("Walking"),
    ("Bicycling"),
    ("Transit")
]


def ShowMode():
    tvalue = v.get()
    print("v: ", tvalue)
    if tvalue == 0:
        reqDirections("driving")
    elif tvalue == 1:
        reqDirections("walking")
    elif tvalue == 2:
        reqDirections("bicycling")
    elif tvalue == 3:
        reqDirections("transit")

    
    


for val, tmode in enumerate(tmodes):
    tk.Radiobutton(Frame1,
                   text=tmode,
                   padx=20,
                   variable=v,
                   indicatoron=0,
                   command=ShowMode,
                   # background="black",
                   selectcolor="blue",
                   highlightcolor="yellow",
                   highlightthickness=10,
                   value=val).grid(row=0, column=val, padx=20, sticky="w,e,n,s")

Frame1.grid(sticky="w,e")
labelMap.grid()
labelTimeToDestination.grid()
# print(directions_result[0]["legs"][0]["duration"]["text"])
# get optimistic and pessimistic and change color red to green by comparison

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
