"""
sphere.py
author: Samke_g2

This program takes a sphere's diameter as input (in float) and outputs the sphere's:
- diameter
- circumference
- surface area
- volume

1. Significant constants :
    - pi

2. Inputs :
    - The radius of the sphere

3. Outputs:
    - diameter
    - circumference
    - surface area
    - volume
"""
from math import pi

radius = float(input("Enter the radius of a sphere: "))

diameter = radius * 2

circumference = pi * diameter

surface_area = 4 * pi * radius**2

volume = (4/3) * pi * radius**3

print(f"""
For a sphere with a radius of : {radius}

The Diameter is : {round(diameter, 2)}
The Circumference is : {round(circumference, 2)}
The Surface Area is : {round(surface_area, 2)}
The Volume is : {round(volume, 2)}
""")
