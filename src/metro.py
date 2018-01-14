# python3

class Metro:

    class Builder:

        def __init__(self):
            self.obj = Metro()

        def name(self, name):
            self.obj.name = name
            self.obj.line = name[7:][:2]
            self.obj.stop = name[13:][:-1]
            return self

        def lat(self, lat):
            self.obj.lat = lat
            return self

        def lon(self, lon):
            self.obj.lon = lon
            return self

        def build(self):
            return self.obj