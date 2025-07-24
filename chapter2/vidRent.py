"""
vidRent
author: Samke_g2

Program is for a hypothetical video rental place.
It computes the total charger of vid rentals based on different pricing fpr different types of movies.

1. Significant constants :
    - newer = $3.00
    - oldies = $2.00

2. The inouts are :
    - Number of old movies rented
    - Number of new movies rented

3. The output is :
    - the total cost after multiplying inputs with constants.
"""
# constants
newer = 3.00
oldies = 2.00

# ask user for the inputs
numNew = int(input("Enter the number of newer movies: "))
numOld = int(input("Enter the number of older movies: "))

# compute total cost
result = (float(numNew) * newer) + (float(numOld) * oldies)

# display result as price
print(f"\nThe total cost is : ${result} per night\n")
