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


    def details(self):
        print("{} {}".format(self.make, self.model))
        print("Exterior Dimensions + Weight :{} in. {} in. {} in. {} in. {} lb.".format
              (self.length, self.width, self.height,self.wheelbase, self.weight))
        print("Cargo: {} lb. {} cu.Ft {} lb.".format
              (self.max_load, self.cargo_volume, self.towing_capacity))
        print("Interior Dimensions: "
              "{} in. {} in. {} in. {} in. {} in. {} in. {} in. {} in. {} in.".format
              (self.front_shoulderroom, self.front_legroom, self.front_headroom,
               self.rear_shoulderroom, self.rear_legroom, self.rear_headroom,
               self.thirdrow_shoulderroom, self.thirdrow_legroom, self.thirdrow_headroom))



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

smart = Smart('Smart', 'EQ Fortwo', 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
smart.details()
















