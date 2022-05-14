import math

radius_sphere = float(input("Enter radius of the sphere: "))
height_cone = float(input("Enter height of the cone: "))
width_cube = float(input("Enter width of the cube: "))
volume_sphere = (4 * math.pi * math.pow(radius_sphere, 3)) / 3
volume_cone = (math.pi * ((radius_sphere/2) ** 2) * height_cone)/ 3
volume_cube = math.pow(width_cube, 3)
total_volume = volume_sphere + volume_cone + volume_cube
print("Total volume is {:0.2f}".format(total_volume))
