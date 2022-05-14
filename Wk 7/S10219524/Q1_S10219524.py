# Yong Zi Ren (S10219524)-P07
import math  # importing math

a = float(input('Enter x coordinate of point 1:'))  # Get x coordinate of point 1
b = float(input('Enter y coordinate of point 1:'))  # Get y coordinate of point 1
c = float(input('Enter x coordinate of point 2:'))  # Get x coordinate of point 2
d = float(input('Enter y coordinate of point 2:'))  # Get y coordinate of point 2
e = math.sqrt((a - c) ** 2 + (b - d) ** 2)  # Given formula
print('The distance is {:0.2f}'.format(e))  # display final result in 2 decimal place
