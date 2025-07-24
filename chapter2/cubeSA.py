"""
Cube surface area
author: Samke_g2

This program computes the surface are of a cube, given the length of a single side.

1. The inputs are :
  - The length of a side of the cube (sLen)

2. The Output is :
  - The Total surface area of the cube (assuming it is closed)
"""
# imports pow function from the math module
from math import pow

# asks user for value of side length
# then converts input from string to int
sLen = input("Enter the length of side of the cube : ")
sLen = int(sLen)

# computes surfce area from given side
tsa = pow(sLen, 2) * 6

# displays surface area as output
print(f"The total surface area of the cube is : {tsa}\n")
