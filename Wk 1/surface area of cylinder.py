import math


def this():
    r = float(input('value of radius:'))
    h = float(input('value of height:'))
    pi = math.pi
    surface = 2 * pi * r * h + 2 * pi * r ** 2
    print("Total Surface Area:",str(surface)+"cm^2")


while True:
    this()
