
full_name = "Amba Geoffrey"

# Extracting first name and last name using split() method
names = full_name.split()
first_name = names[0]
last_name = names[-1]

# Printing first name and last name
print("First Name:", first_name)
print("Last Name:", last_name)

# Printing initials
initials = first_name[0] + last_name[0]
print("Initials:", initials)



# Get the user's age as an input
user_age = input("40: ")

# Convert the user's input to an integer
user_age_int = int('40')

# Print a message with the user's age
print(f"You are {user_age_int} years old")


# List of product names and prices
products = [
    ("Apple", 10000),
    ("Banana", 5000),
    ("Cherry", 2000),
    ("Date", 1000),
    ("Elderberry", 3000)
]

# Print the header of the table
print(f"{'Product':<15} {'Price':>10}")
print('-' * 25)

# Print each product in the catalog
for product, price in products:
    print(f"{product:<15} Ugs{price:>9.2f}")


import re

# Regular expression pattern for validating an email address
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Ask the user for their email address
user_email = input("Please enter a valid email address: ")

# Check if the email address is valid
if re.match(email_pattern, user_email):
    print("Valid email address.")
else:
    print("Please enter a valid email address.")

# Get two numbers (floats) from the user
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

# Ask the user for the operation they want to perform
operation = input("Please enter the operation (addition, subtraction, multiplication, division): ").strip().lower()


# Get two numbers (floats) from the user
num1 = float(input("10: "))
num2 = float(input("8: "))

# Ask the user for the operation they want to perform
operation = input("Please enter the operation (addition, subtraction, multiplication, division): ").strip().lower()

# Perform the chosen operation and print the result
if operation == "addition":
    result = 10 + 8
    print(f"The result of addition is: {result}")
elif operation == "subtraction":
    result = 10 - 8
    print(f"The result of subtraction is: {result}")
elif operation == "multiplication":
    result = 10 * 8
    print(f"The result of multiplication is: {result}")
elif operation == "division":
    if 8 != 0:
        result = 10 / 8
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation. Please enter addition, subtraction, multiplication, or division.")