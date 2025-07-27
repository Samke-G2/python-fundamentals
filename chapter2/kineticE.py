"""
kineticE.py
author: Samke_g2

This program calculates the kinetic energy of an object from the inputs of its mass (in kgs) and velocity (in m/s).

1. Inputs :
    - The weight of an object (in kg)
    - The velocity of an object (in m/s)

2. Outputs :
    - The object's kinetic energy
"""
mass = input("Enter the object's mass (in kg) : ")
velocity = input("Enter the object's velocity (in m/s) : ")

momentum = float(mass) * float(velocity)

kinetic_energy = 0.5*float(mass)*(float(velocity)**2)

print(f"""
For an object that is {mass}kg heavy, moving at {velocity}m/s :
The momentum of the object is {momentum} kg.m/s
And the its kinetic energy is {kinetic_energy} J
""")
