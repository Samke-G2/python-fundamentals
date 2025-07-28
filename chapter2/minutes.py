"""
minutes.py
author: Samke_g2

This program calculates the number of minutes in a year.
"""
minute = 1
hour = 60 * minute
day =  hour * 24

year = day * 365
leap_year = day * 366

print(f"""
There are {hour} minutes in an hour and {day} in a day,
Therefore,
A year has {year} minutes, {leap_year} in a leap year.
""")
