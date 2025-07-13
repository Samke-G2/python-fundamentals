# Case Study 1 - Income tax calculator
# by Samke G2


# Compute a person's income tax

# 1. Significant constants
#   tax rate
#   standard deduction
#   deduction per dependent

# 2. The inputs are:
#   gross Income
#   number of dependants

# 3. Computations:
#   taxable income = gross income - the standard deduction - (a deduction for each dependent)
#   income tax = a fixed percentage of taxble Income

# 4. The outputs are:
#   the income taxble


# Initialize the constants
tax_rate = 0.20
standard_deduction = 10000.00
dependent_deduction = 3000

# Request the inputs
gross_income = input("Enter the gross income: ")
numDependents = input("Enter the number of dependents: ")

# Compute income tax
taxable_income = float(gross_income) - standard_deduction - (dependent_deduction * int(numDependents))
incomeTax = taxable_income * tax_rate

# Display the income tax
print("The income tax is: R" + str(incomeTax))
