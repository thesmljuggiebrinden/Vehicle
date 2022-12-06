import random
from typing import Tuple


class Vehicle:
    def __init__(self, make, model, year, color, body_styles, trim_lines,
                 drive_wheels, seating, engines, transmissions,
                 length, width, height, wheelbase, weight,
                 max_load, cargo_volume, towing_capacity, front_shoulderroom,
                 front_legroom, front_headroom, rear_shoulderroom, rear_legroom,
                 rear_headroom, thirdrow_shoulderroom, thirdrow_legroom, thirdrow_headroom,
                 fuel_type, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
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
        print('{} {} {} {}'.format(self.color, self.year, self.make, self.model))
        print('----------------------------------------------------------------')

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

    def distance(self, miles):
        self.gallons = miles/self.mpg
        print("To go {} miles, the {} {} {} {} gets {} gallons.".format(miles, self.color, self.year, self.make, self.model, self.gallons))

vehicles = []
def add_vehicle():
    make = input("Enter the make of the car")
    model = input("Enter the model of the car")
    year = int(input("Enter the year of the car"))
    color = input("Enter the color of the car")
    body_styles = input("Enter the body styles of the car")
    trim_lines = input("Enter the trim lines of the car")
    drive_wheels = input("Enter the drive wheels of the car")
    seating = input("Enter the seating of the car")
    engines = input("Enter the engines of the car")
    transmissions = input("Enter the transmissions of the car")
    length = int(input("Enter the length of the car"))
    width = int(input("Enter the width of the car"))
    height = int(input("Enter the height of the car"))
    wheelbase = int(input("Enter the wheelbase of the car"))
    weight = int(input("Enter the weight of the car"))
    max_load = int(input("Enter the max load of the car"))
    cargo_volume = int(input("Enter the cargo volume of the car"))
    towing_capacity = int(input("Enter the towing capacity of the car"))
    front_shoulderroom = int(input("Enter the front shoulder room of the car"))
    front_legroom = int(input("Enter the front leg room of the car"))
    front_headroom = int(input("Enter the front head room of the car"))
    rear_shoulderroom = int(input("Enter the rear shoulder room of the car"))
    rear_legroom = int(input("Enter the rear leg room of the car"))
    rear_headroom = int(input("Enter the rear head room of the car"))
    thirdrow_shoulderroom = int(input("Enter the third row shoulder room of the car"))
    thirdrow_legroom = int(input("Enter the third row leg room of the car"))
    thirdrow_headroom = int(input("Enter the third row head room of the car"))
    fuel_type = input("Enter the fuel type of the car")
    mpg = int(input("Enter the mpg of the car"))
    vehicle = Vehicle\
            (make, model, year, color, body_styles, trim_lines, drive_wheels, seating,
             engines, transmissions, length, width, height, wheelbase, weight, max_load,
             cargo_volume, towing_capacity, front_shoulderroom, front_legroom, front_headroom,
             rear_shoulderroom, rear_legroom, rear_headroom, thirdrow_shoulderroom,
             thirdrow_legroom, thirdrow_headroom, fuel_type, mpg)
    vehicles.append(vehicle)

done_adding = False
while not done_adding:
    add_vehicle()
    answer = input("Do you want to add another vehicle?")
    if answer == "yes":
        print("New vehicle")
    else:
        answer == "no"
        done_adding = True

miles = int(input("Enter the number of miles"))

number_of_vehicles = len(vehicles)

for number in range(100):
    random_number = random.randint(0, number_of_vehicles - 1)
    vehicles[random_number].describe()

for number in range(100):
    random_number = random.randint(0, number_of_vehicles - 1)
    vehicles[random_number].overview()

for number in range(100):
    random_number = random.randint(0, number_of_vehicles - 1)
    vehicles[random_number].exterior_dimensions()

for number in range(100):
    random_number = random.randint(0, number_of_vehicles - 1)
    vehicles[random_number].cargo()

for number in range(100):
    random_number = random.randint(0, number_of_vehicles - 1)
    vehicles[random_number].interior_dimensions()

for number in range(100):
    random_number = random.randint(0, number_of_vehicles - 1)
    vehicles[random_number].fuel()

for number in range(100):
    random_number = random.randint(0, number_of_vehicles - 1)
    vehicles[random_number].distance(miles)

