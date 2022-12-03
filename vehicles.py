from typing import Tuple


class Vehicles:
    def __init__(self, make, model, length, width, height, wheelbase, weight,
                 max_load, cargo_volume, towing_capacity, front_shoulderroom,
                 front_legroom, front_headroom, rear_shoulderroom, rear_legroom,
                 rear_headroom, thirdrow_shoulderroom, thirdrow_legroom, thirdrow_headroom):
        self.make = make
        self.model = model
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


    def dimensions(self):
        print("{} {}".format(self.make, self.model))
        print("Length: {} in.".format(self.length))
        print("Width: {} in.".format(self.width))
        print("Height: {} in.".format(self.height))
        print("Wheelbase: {} in.".format(self.wheelbase))
        print("Weight: {} lb.".format(self.weight))
        print("Max load: {} lb.".format(self.max_load))
        print("Cargo volume: {} cu.Ft".format(self.cargo_volume))
        print("Towing capacity: {} lb.".format(self.towing_capacity))
        print("Front shoulder room: {} in.".format(self.front_shoulderroom))
        print("Front leg room: {} in.".format(self.front_legroom))
        print("Front head room: {} in.".format(self.front_headroom))
        print("Rear shoulder room: {} in.".format(self.rear_shoulderroom))
        print("Rear leg room: {} in.".format(self.rear_legroom))
        print("Rear head room: {} in.".format(self.rear_headroom))
        print("Third row shoulder room: {} in.".format(self.thirdrow_shoulderroom))
        print("Third row leg room: {} in.".format(self.thirdrow_legroom))
        print("Third row head room: {} in.".format(self.thirdrow_headroom))





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

smart = Smart('Smart', 'EQ Fortwo', 106.1, 74.5, 61.1, 73.7, 2363, 635, 8.9, 635,
              None, None, None, None, None, None, None, None, None)
smart.dimensions()

















