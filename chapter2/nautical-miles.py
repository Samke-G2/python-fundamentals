"""
nautical-miles.py
author: Samke_g2

This program converts kilometers to nautical miles.

1. Important constants :
    - 1km = 0.54 nautical miles (according to my calculations, subject to better info)

2. inputs :
    - The value of km to be converted

3. outputs :
    - The nautivcal miles equivalent of the km
"""
print("\nThis program converts km to nautical miles. \n")

km = input("How many kilometers would you like to convert: ")
km = float(km)

nautical_miles = 1.8518518518518519 * km

print(f"\n{km} km is equal to: {nautical_miles} nautical miles\n")
