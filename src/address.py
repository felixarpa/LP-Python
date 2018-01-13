# python3

class Address:

    class Builder:

        def __init__(self):
            self.obj = Address()

        def name(self, name):
            self.obj.name = name
            return self

        def street(self, street):
            self.obj.street = street
            return self

        def number(self, number):
            self.obj.number = number
            return self

        def zip_code(self, zip_code):
            self.obj.zip_code = zip_code
            return self

        def district(self, district):
            self.obj.district = district
            return self

        def city(self, city):
            self.obj.city = city
            return self

        def build(self):
            return self.obj