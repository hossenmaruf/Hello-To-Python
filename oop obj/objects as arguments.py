class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle,color):

    vehicle.color = color



bike_1 = Motorcycle()

change_color(bike_1,"black")

print(bike_1.color)