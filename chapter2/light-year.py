"""
light-year.py
author: Samke_g2

This program computes the value of a light year, using the a function from the math module and a variable from a previous project.

1. Important constants:
    - The spped of light : 3*10**8
"""
from math import pow
# from minutes import year

light_speed = 3*pow(10,8)

seconds_in_year = 31536000

light_year = light_speed * seconds_in_year

print(f"""
The speed of light is: {light_speed} m/s
and there are {seconds_in_year} seconds in a year.

A light-year is the distance that a light beam travels in a year.
That distance is: {int(light_year)}m or {int(light_year/1000)}km
""")
