__author__ = 'laurentmeyer'

# Install the wrapper by typing "pip install -U googlemaps"
# Open Key: AIzaSyDIfhg1xoQKqy2b0BheWqgMuVyFGgWJIkQ

import googlemaps
import time

def find_distance_between_two_lats(startLatitude, startLongitude, endLatitude, endLongitude):
    gmaps = googlemaps.Client(key='AIzaSyDIfhg1xoQKqy2b0BheWqgMuVyFGgWJIkQ')
    startaddress = gmaps.reverse_geocode({"lat":startLatitude, "lng":startLongitude})[0]['formatted_address']
    print(startaddress)
    endaddress = gmaps.reverse_geocode({"lat":endLatitude, "lng":endLongitude})[0]['formatted_address']
    print(endaddress)
    directions = gmaps.directions(startaddress, endaddress, mode="walking")
    meters = directions[0]['legs'][0]['distance']['value']
    print meters
    seconds = directions[0]['legs'][0]['duration']['value']
    print seconds


find_distance_between_two_lats(48.127701, 11.666358, 48.123805, 11.649020)