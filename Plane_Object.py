__author__ = 'coyle'


class PlaneObject(object):

    transponderCode = 0

    name = ''

    currentLat = 0

    currentLong = 0

    currentAltitude = 0

    currentVelocity = 0

    def __init__(self, transponder_code, name, current_lat, current_long, current_altitude, current_velocity):
        self.currentAltitude = current_altitude
        self.currentLat = current_lat
        self.currentLong = current_long
        self.name = name
        self.transponderCode = transponder_code
        self.currentVelocity = current_velocity


