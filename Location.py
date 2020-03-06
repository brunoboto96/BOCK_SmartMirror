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
                location_dict = {
                    'latitude': latitude,
                    'longitude': longitude,
                    'city': location,
                    'country': country,
                    'country_code': country_code,
                    'public_ip': public_ip
                }

                return location_dict
        except Exception as e:
            logging.error(e)
            return None

    def geo_location(self):
        raw_data = Location().get_location()
        if raw_data == None:  # if no location is found, it'll access the last location stored, if no location has ever been found it'll return None
            if os.path.isfile('lat_long_saved.txt'):
                file = eval(open('lat_long_saved.txt', 'r').read())
                lat_long = [file['latitude'], file['longitude']]
                #print(lat_long)
            else:
                lat_long = [None, None]
        else:
            lat_long = [raw_data['latitude'], raw_data['longitude']]
            latitude_longitude = {'latitude': lat_long[0], 'longitude': lat_long[1]}
            #print(latitude_longitude)
            with open("lat_long_saved.txt", "w") as f:
                f.write(str(latitude_longitude))

        return lat_long