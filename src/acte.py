# python3
import math

DRAD = math.pi / 180.0
ERAD = 6371000.0
def deg2rad(deg): return deg * DRAD

def distance(loc1, loc2):
    lat1, lon1 = float(loc1.lat), float(loc1.lon)
    lat2, lon2 = float(loc2.lat), float(loc2.lon)
    phi1, phi2 = deg2rad(90.0 - lat1), deg2rad(90.0 - lat2)
    the1, the2 = deg2rad(lon1), deg2rad(lon2)
    cos = math.sin(phi1) * math.sin(phi2) * math.cos(the1-the2) + math.cos(phi1) * math.cos(phi2)
    return math.acos(cos) * ERAD

class Acte:

    def __init__(self):
        self.train_stations = []

    def add_train_station(self, metro):
        dist = distance(self.coordinates, metro)
        if dist <= 500:
            obj = [metro, dist]
            for i in range(0, len(self.train_stations)):
                if self.train_stations[i][1] > dist:
                    self.train_stations.insert(i, obj)
                    self.train_stations = self.train_stations[:5]
                    return True
            if len(self.train_stations) < 5:
                self.train_stations.append(obj)
                return True
        return False

    class Builder:

        def __init__(self):
            self.obj = Acte()

        def name(self, name):
            self.obj.name = name
            return self

        def address(self, address):
            self.obj.address = address
            return self

        def coordinates(self, coordinates):
            self.obj.coordinates = coordinates
            return self

        def date(self, date):
            self.obj.date = date
            return self

        def build(self):
            return self.obj
