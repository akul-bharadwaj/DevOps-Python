"""
This module deals with logistics and calculates distances between two points
and the time it takes to travel between them and other logistics related stuff
for a given speed.

"""

from geopy import distance

# build a list of 10 cities in India and their coordinates
CITIES = [
    ("Mumbai", (19.0760, 72.8777)),
    ("Delhi", (28.7041, 77.1025)),
    ("Bengaluru", (12.9716, 77.5946)),
    ("Hyderabad", (17.3850, 78.4867)),
    ("Ahmedabad", (23.0225, 72.5714)),
    ("Chennai", (13.0827, 80.2707)),
    ("Kolkata", (22.5726, 88.3639)),
    ("Surat", (21.1702, 72.8311)),
    ("Pune", (18.5204, 73.8567)),
    ("Jaipur", (26.9124, 75.7873)),
]


def distance_between_two_points(point1, point2):
    """
    Calculate the distance between two points
    """
    return distance.distance(point1, point2).miles


# return the coordinates of a city
def get_coordinates(city):
    """
    Return the coordinates of a city
    """
    for city_name, coordinates in CITIES:
        if city_name == city:
            return coordinates


def cities_list():
    """
    Return the list of cities
    """

    return [city[0] for city in CITIES]


# estimate the travel time between two cities by car.
# assume the speed is 60 miles per hour
def travel_time(city1, city2, speed=60):
    """
    Estimate the travel time between two cities by car.
    Assume the default speed is 120 km per hour
    """

    point1 = get_coordinates(city1)
    point2 = get_coordinates(city2)
    total_distance = distance_between_two_points(point1, point2)
    hours = round(total_distance / speed)
    return hours
