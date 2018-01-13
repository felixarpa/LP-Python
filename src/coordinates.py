# python3

class Coordinates:

    class Builder:

        def __init__(self):
            self.obj = Coordinates()

        def lat(self, lat):
            self.obj.lat = lat
            return self

        def lon(self, lon):
            self.obj.lon = lon
            return self

        def build(self):
            if self.obj.lat == '': self.obj.lat = '0'
            if self.obj.lon == '': self.obj.lon = '0'
            return self.obj