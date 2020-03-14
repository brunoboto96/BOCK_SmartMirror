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
from tkinter import Label
import io

# get your api key @ google console -> APIS & Services -> credentials | after -> dashboard enable apis -> Directions, Geocoding, Maps Static API
apikey = ''
gmaps = googlemaps.Client(key=apikey)

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("31 Upper George Street, Luton",
                                     "Skimpot Road Dunstable",
                                     mode="driving",
                                     departure_time=now)

# directions_result -> list -> len() == 1 | directions_result[0] -> dict | directions_result[0]["json_attr"]
# print(directions_result[0]["overview_polyline"]["points"])

directions_url = "https://maps.googleapis.com/maps/api/staticmap?size=600x400&path=enc%3A"
directions_url = directions_url + \
    directions_result[0]["overview_polyline"]["points"] + "&key=" + apikey
print(directions_url)

# gui
root = tk.Tk()


Frame1 = tk.Frame(root)
Frame1.place(relheight=0.468, relwidth=1)
Frame1.configure(relief='groove')
Frame1.configure(borderwidth="2")
Frame1.configure(relief="groove")
Frame1.configure(background="#000000")

DrivingButton = tk.Button(Frame1)
DrivingButton.place(relheight=121, relwidth=289)
DrivingButton.configure(activebackground="#0080c0")
DrivingButton.configure(activeforeground="white")
DrivingButton.configure(activeforeground="black")
DrivingButton.configure(background="#000000")
DrivingButton.configure(disabledforeground="#a3a3a3")
DrivingButton.configure(font="-family {Lato} -size 14 -weight bold")
DrivingButton.configure(foreground="#ffffff")
DrivingButton.configure(highlightbackground="#ff8000")
DrivingButton.configure(highlightcolor="#ff0000")
DrivingButton.configure(pady="0")
DrivingButton.configure(relief="groove")
DrivingButton.configure(state='active')
DrivingButton.configure(text='''Driving''')

WalkingButton = tk.Button(Frame1)
WalkingButton.place(relheight=121, relwidth=289)
WalkingButton.configure(activebackground="#0080c0")
WalkingButton.configure(activeforeground="white")
WalkingButton.configure(activeforeground="black")
WalkingButton.configure(background="#000000")
WalkingButton.configure(disabledforeground="#a3a3a3")
WalkingButton.configure(font="-family {Lato} -size 14 -weight bold")
WalkingButton.configure(foreground="#ffffff")
WalkingButton.configure(highlightbackground="#ff8040")
WalkingButton.configure(highlightcolor="black")
WalkingButton.configure(pady="0")
WalkingButton.configure(relief="groove")
WalkingButton.configure(text='''Walking''')

TransportButton = tk.Button(Frame1)
TransportButton.place(relheight=121, relwidth=289)

TransportButton.configure(activebackground="#0080c0")
TransportButton.configure(activeforeground="white")
TransportButton.configure(activeforeground="black")
TransportButton.configure(background="#000000")
TransportButton.configure(disabledforeground="#a3a3a3")
TransportButton.configure(font="-family {Lato} -size 14 -weight bold")
TransportButton.configure(foreground="#ffffff")
TransportButton.configure(highlightbackground="#ff8000")
TransportButton.configure(highlightcolor="black")
TransportButton.configure(pady="0")
TransportButton.configure(relief="groove")
TransportButton.configure(text='''Public Transports''')

BicyclingButton = tk.Button(Frame1)
BicyclingButton.place(relheight=121, relwidth=289)

BicyclingButton.configure(activebackground="#0080c0")
BicyclingButton.configure(activeforeground="white")
BicyclingButton.configure(activeforeground="black")
BicyclingButton.configure(background="#000000")
BicyclingButton.configure(disabledforeground="#a3a3a3")
BicyclingButton.configure(font="-family {Lato} -size 14 -weight bold")
BicyclingButton.configure(foreground="#ffffff")
BicyclingButton.configure(highlightbackground="#ff8000")
BicyclingButton.configure(highlightcolor="black")
BicyclingButton.configure(pady="0")
BicyclingButton.configure(relief="groove")
BicyclingButton.configure(text='''Bicycling''')

DrivingButton.grid(row = 0, column = 0, padx = 20, sticky = "w,e,n,s")
WalkingButton.grid(row = 0, column = 1, padx = 20, sticky = "w,e,n,s")
TransportButton.grid(row = 0, column = 2, padx = 20, sticky = "w,e,n,s")
BicyclingButton.grid(row = 0, column = 3, padx = 20, sticky = "w,e,n,s")
Frame1.grid(sticky = "w,e")

# request data from url -> crawls for the first image and stores it
raw_data = urllib.request.urlopen(directions_url).read()
im = PIL.Image.open(io.BytesIO(raw_data))
image = PIL.ImageTk.PhotoImage(im)

# displays the img
labelMap = Label(root, image=image)
labelMap.grid()

labelTimeToDestination = Label(root, text=directions_result[0]["legs"][0]["duration_in_traffic"]
                               ["text"] + " - " + directions_result[0]["legs"][0]["distance"]["text"])
labelTimeToDestination.grid()
# print(directions_result[0]["legs"][0]["duration"]["text"])
# get optimistic and pessimistic and change color red to green by comparison

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()

#def activateSelection():
