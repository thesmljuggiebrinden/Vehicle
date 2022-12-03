from typing import Tuple


class Vehicles:
    def __init__(self, make, model, body_styles, trim_lines,
                 drive_wheels, seating, engines, transmissions,
                 length, width, height, wheelbase, weight,
                 max_load, cargo_volume, towing_capacity, front_shoulderroom,
                 front_legroom, front_headroom, rear_shoulderroom, rear_legroom,
                 rear_headroom, thirdrow_shoulderroom, thirdrow_legroom, thirdrow_headroom,
                 fuel_type, mpg):
        self.make = make
        self.model = model
        self.body_styles = body_styles
        self.trim_lines = trim_lines
        self.drive_wheels = drive_wheels
        self.seating = seating
        self.engines = engines
        self.transmissions = transmissions
        self.length = length
        self.width = width
        self.height = height
        self.wheelbase = wheelbase
        self.weight = weight
        self.max_load = max_load
        self.cargo_volume = cargo_volume
        self.towing_capacity = towing_capacity
        self.front_shoulderroom = front_shoulderroom
        self.front_legroom = front_legroom
        self.front_headroom = front_headroom
        self.rear_shoulderroom = rear_shoulderroom
        self.rear_legroom = rear_legroom
        self.rear_headroom = rear_headroom
        self.thirdrow_shoulderroom = thirdrow_shoulderroom
        self.thirdrow_legroom = thirdrow_legroom
        self.thirdrow_headroom = thirdrow_headroom
        self.fuel_type = fuel_type
        self.mpg = mpg

    def describe(self):
        print('{} {}'.format(self.make, self.model))
        print('------------------------------------')

    def overview(self):
        print('Body Styles: {}'.format(self.body_styles))
        print('Trim Lines: {}'.format(self.trim_lines))
        print('Drive Wheels: {}'.format(self.drive_wheels))
        print('Seating: {}'.format(self.seating))
        print('Engines: {}'.format(self.engines))
        print('Transmissions: {}'.format(self.transmissions))
        print('-----------------------------------------------')

    def exterior_dimensions(self):
        print('Length: {}'.format(self.length))
        print('Width: {}'.format(self.width))
        print('Height: {}'.format(self.height))
        print('Wheelbase: {}'.format(self.wheelbase))
        print('Weight: {}'.format(self.weight))
        print('-------------------------------------')

    def cargo(self):
        print('Max Load: {}'.format(self.max_load))
        print('Cargo Volume: {}'.format(self.cargo_volume))
        print('Towing Capacity: {}'.format(self.towing_capacity))
        print('-------------------------------------------------')

    def interior_dimensions(self):
        print('Front Shoulder Room: {}'.format(self.front_shoulderroom))
        print('Front Leg Room: {}'.format(self.front_legroom))
        print('Front Head Room: {}'.format(self.front_headroom))
        print('Rear Shoulder Room: {}'.format(self.rear_shoulderroom))
        print('Rear Leg Room: {}'.format(self.rear_legroom))
        print('Rear Head Room: {}'.format(self.rear_headroom))
        print('Third Row Shoulder Room: {}'.format(self.thirdrow_shoulderroom))
        print('Third Row Leg Room: {}'.format(self.thirdrow_legroom))
        print('Third Row Head Room: {}'.format(self.thirdrow_headroom))
        print('---------------------------------------------------------------')

    def fuel(self):
        print('{}'.format(self.fuel_type))
        print('{}'.format(self.mpg))
        print('-------------------------')













class Smart(Vehicles):
    pass

class Acura(Vehicles):
    pass

class Audi(Vehicles):
    pass

class BMW(Vehicles):
    pass

class Buick(Vehicles):
    pass

class Cadillac(Vehicles):
    pass

class Chevrolet(Vehicles):
    pass

class Chrysler(Vehicles):
    pass

class Dodge(Vehicles):
    pass

class Ford(Vehicles):
    pass

class GMC(Vehicles):
    pass

class Honda(Vehicles):
    pass

class Hyundai(Vehicles):
    pass

class Infiniti(Vehicles):
    pass

class Jeep(Vehicles):
    pass

class Kia(Vehicles):
    pass

class Lexus(Vehicles):
    pass

class Lincoln(Vehicles):
    pass

class Mazda(Vehicles):
    pass

class Mercedes_Benz(Vehicles):
    pass

class Mitsubishi(Vehicles):
    pass

class Nissan(Vehicles):
    pass

class Subaru(Vehicles):
    pass

class Tesla(Vehicles):
    pass

class Toyota(Vehicles):
    pass

class Volkswagen(Vehicles):
    pass

class Volvo(Vehicles):
    pass
