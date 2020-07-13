# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE


class LatLon:
    ''' 
    Class representing coordinates of a location.

    Attributes:
        lat: A floating point number representing latitude coordinates on a map
        long: A floating point number representing longitude coordinates on a map
    '''

    def __init__(self, lat, lon):
        '''Initializes LatLon class with latitude and longitude coordinates'''

        self.lat = lat
        self.lon = lon

    def __str__(self):
        output = f'LatLon: {self.lat}, {self.lon}'
        return output


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# YOUR CODE HERE


class Waypoint(LatLon):
    ''' 
    Class representing a location on a route of travel. 

    Attributes:
        name: A string representing the name of a location
    '''

    def __init__(self, name, lat, lon):
        '''Initializes Waypoint class with the name of a location'''

        self.name = name
        super().__init__(lat, lon)

    def __str__(self):
        output = f'Waypoint: {self.name}, {self.lat}, {self.lon}'
        return output

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# YOUR CODE HERE


class Geocache(Waypoint):
    '''
    Class representing an item placed at a specific location

    Attributes:
        difficulty: A floating point number representing degree of difficutly
        size: Integer representing size of cached/placed object
    '''

    def __init__(self, name, difficulty, size, lat, lon):
        '''Intializes Geocache class with a degree of difficulty and the size of the specified item'''

        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        output = f'Geocache: {self.name}, {self.difficulty}, {self.size}, {self.lat}, {self.lon}'
        return output


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
waypoint = Waypoint('Catacombs', 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE
geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
