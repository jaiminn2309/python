# Session 3 Python Practical
# This program demonstrates data types,
# type conversion, functions, input, and boolean values.

# Task 1: Variables and Data Types

age = 20
height_cm = 172.5
name = "Jaimin"
has_netflix_account = True

print("Age:", age)
print("Type:", type(age))

print("Height:", height_cm)
print("Type:", type(height_cm))

print("Name:", name)
print("Type:", type(name))

print("Netflix Account:", has_netflix_account)
print("Type:", type(has_netflix_account))


# Task 2: Calculate Total Cart Amount

def calculate_cart_total(prices):
    total = 0.0

    for price in prices:
        total += float(price)

    return total


cart = ['249.99', '75', '425.50']

print("Total Cart Amount:", calculate_cart_total(cart))


# Task 3: Check Cricket Score

cricket_score = input("Enter your cricket score: ")
cricket_score = int(cricket_score)

if cricket_score >= 50:
    print("You scored a Half-century!")
else:
    print("Keep practicing!")


# Task 4: Convert String to Boolean

premium_status = "True"
premium_status = premium_status == "True"

print("Premium Account:", premium_status)
print("Type:", type(premium_status))