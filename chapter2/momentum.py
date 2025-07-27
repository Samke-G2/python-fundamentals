"""
momentum.py
author: Samke_g2

This program calculates the momentum of an object from the inputs of its mass (in kgs) and velocity (in m/s).

1. Inputs :
    - The weight of an object (in kg)
    - The velocity of an object (in m/s)

2. Outputs :
    - The object's momentum
"""
mass = input("Enter the object's mass (in kg) : ")
velocity = input("Enter the object's velocity (in m/s) : ")

momentum = float(mass) * float(velocity)

print(f"""
For an object that is {mass}kg heavy, moving at {velocity}m/s :
The momentum of the object is {momentum} kg.m/s
""")
