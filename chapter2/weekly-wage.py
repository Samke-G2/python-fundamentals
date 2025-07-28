"""
weekly-wage.py
author: Samke_g2

This program calculates an employee's total weekly pay based on the total regular hours worked and overtime hours worked.

1. Inputs :
    - hourly wage
    - total regular hrs worked
    - total overtime hours

2. Outputs :
    - Total weekly pay
"""
print("\nThis program calculates an employee's total weekly wage, including overtime.")

hourly_wage = float(input("\nEnter the hourly wage: R"))
regular_hrs = float(input("\nEnter the number of REGULAR hrs worked: "))
overtime = float(input("\nEnter the number of OVERTIME hrs worked: "))

regular_pay = hourly_wage * regular_hrs
overtime_pay = overtime * (1.5 * hourly_wage)

total_weekly_pay = regular_pay + overtime_pay

print(f"\nThe total weekly wage is: R{total_weekly_pay}\n")
