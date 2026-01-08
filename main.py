# Day 2 – Tip Calculator
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Converting user input from strings to numbers (float and int)
# - Performing basic arithmetic operations in Python
# - Using variables to store intermediate results
# - Rounding numbers for currency formatting
# - Using f-strings to format output
#
# This project reflects my early understanding of:
# - Data types
# - Type casting (float(), int())
# - Sequential program execution

print("Welcome to the tip calculator!")

# Get the total bill amount and convert it to a float
total_bill = float(input("What was the total bill? $"))

# Ask for the tip percentage and convert it to an integer
tip = int(input("How much would you like to give? 10, 12, or 15? "))

# Ask how many people will split the bill
split = int(input("How many people to split the bill? "))

# Calculate the total bill including the tip
bill_with_tip = total_bill + total_bill * (tip / 100)

# Calculate each person's share and round to 2 decimal places
each_share = round(bill_with_tip / split, 2)

# Display the final amount each person should pay
print(f"Each person should pay: ${each_share}")
