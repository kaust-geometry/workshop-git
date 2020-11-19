from math import pi, cos

degrees = float(input("Please provide an angle (in degrees): "))
radians = degrees * pi / 180

print("The cosine of the user-provided angle is ", cos(radians), sep = '')
