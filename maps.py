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

#get your api key @ google console -> APIS & Services -> credentials | after -> dashboard enable apis -> Directions, Geocoding, Maps Static API
apikey = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=apikey)

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("31 Upper George Street, Luton",
                                     "Skimpot Road Dunstable",
                                     mode="driving",
                                     departure_time=now)

#directions_result -> list -> len() == 1 | directions_result[0] -> dict | directions_result[0]["json_attr"]
#print(directions_result[0]["overview_polyline"]["points"])

directions_url = "https://maps.googleapis.com/maps/api/staticmap?size=600x400&path=enc%3A"
directions_url = directions_url + directions_result[0]["overview_polyline"]["points"] + "&key=" + apikey
print(directions_url)

#gui
root = tk.Tk()

raw_data = urllib.request.urlopen(directions_url).read()
#print(raw_data)
im = PIL.Image.open(io.BytesIO(raw_data))
image = PIL.ImageTk.PhotoImage(im)
label1 = Label(root, image=image)
label1.grid()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
