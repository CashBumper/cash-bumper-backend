# Install the wrapper by typing 'pip install -U googlemaps'
# Open Key: AIzaSyDIfhg1xoQKqy2b0BheWqgMuVyFGgWJIkQ

import googlemaps
import time

def address_from_geocode(latitude, longitude):
    return gmaps.reverse_geocode({
        'lat':latitude,
        'lng':longitude
    })[0]['formatted_address']

def find_distance_between_two_lats(start_lat, startlng, end_lat, end_lng):
    gmaps = googlemaps.Client(key='AIzaSyDIfhg1xoQKqy2b0BheWqgMuVyFGgWJIkQ')

    start_address = address_from_geocode(start_lat, start_lng)
    end_address = address_from_geocode(end_lat, end_lng)

    directions = gmaps.directions(start_address, end_address, mode='walking')
    meters = directions[0]['legs'][0]['distance']['value']
    seconds = directions[0]['legs'][0]['duration']['value']

    return {'meters': meters, 'seconds': seconds}
