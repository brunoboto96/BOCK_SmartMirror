#''' This will attain the location of the pi when it's connected to the internet '''

import requests
import logging
import os
import json

#The url and access code, allowed 10,000 requests a month
access_key = "b125f7b5d89ab88807d503d6971fac6b"
url = "http://api.ipstack.com/check?"

class Location():
    def get_location(self):
        try:
            r = requests.get(
                url=url,
                params={
                "access_key": access_key
                }
            )

            if str(r.status_code) != '200':
                print('request failed {} : {}'.format(r.status_code, r.text))
                return None
            else:
                result = r.json()
                latitude = result['latitude']
                longitude = result['longitude']
                location = result['city']
                country = result['country_name']
                country_code = result['country_code']
                public_ip = result['ip']
                # print(result)             #Uncomment this is you want to see other parameters you can pull
                return [latitude, longitude]
        except Exception as e:
            logging.error(e)
            return None

    def location(self):
        lat_long = Location().get_location()
        if lat_long == None:  # if no location is found, it'll access the last location stored, if no location has ever been found it'll return None
            if os.path.isfile('lat_long_saved.txt'):
                file = eval(open('lat_long_saved.txt', 'r').read())
                print(file)
                lat_long = [file['latitude'], file['longitude']]
                print(lat_long)
            else:
                lat_long = [None, None]
        else:
            latitude_longitude = '{0},{1}'.format(lat_long[0], lat_long[1])
            data = {'latitude': lat_long[0], 'longitude': lat_long[1]}
            print(data)
            with open("lat_long_saved.txt", "w") as f:
                f.write(str(data))

        return lat_long


L = Location()
location = L.get_location()

print(location)