# ============================================
# Python Lab: Activities 1–7
# Chapters 3 & 4 – Decisions, Loops, Turtle
# ============================================

# -------------------------------
# Activity 1: Converting values and rounding
# -------------------------------
print("Activity 1: Kilometers to Miles")

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
miles = round(miles, 2)

print("Distance in miles:", miles)
print("---------------------------------\n")


# -------------------------------
# Activity 2: if and elif (Grade Converter)
# -------------------------------
print("Activity 2: Numeric Grade to Letter Grade")

grade = float(input("Enter numeric grade: "))

if grade >= 90:
    letter = "A+"
elif grade >= 80:
    letter = "A"
elif grade >= 70:
    letter = "B"
elif grade >= 60:
    letter = "C"
elif grade >= 50:
    letter = "D"
else:
    letter = "F"

print("Letter grade:", letter)
print("---------------------------------\n")


# -------------------------------
# Activity 3: Use of math module (Cylinder Volume)
# -------------------------------
import math

print("Activity 3: Volume of a Cylinder")

diameter = float(input("Enter diameter of the cylinder: "))
height = float(input("Enter height of the cylinder: "))

pi = round(3.141592, 2)
radius = diameter / 2
volume = pi * (radius ** 2) * height

print("Volume of the cylinder:", volume)
print("---------------------------------\n")


# -------------------------------
# Activity 4: Use of Boolean variables
# -------------------------------
print("Activity 4: Boolean Variables")

# Step 1: Declare two Boolean variables
bool1 = True
bool2 = False

print("Boolean values:", bool1, bool2)

# Step 2: Demonstrate logical operations
# Logical AND
print("AND:", bool1 and bool2)

# Logical OR
print("OR:", bool1 or bool2)

# Logical NOT
print("NOT bool1:", not bool1)

# Step 3: Conditional statement using Boolean
if bool1:
    print("bool1 is True")
else:
    print("bool1 is False")

# Conditional statement with logical operation
if bool1 and not bool2:
    print("Condition bool1 AND NOT bool2 is True")
    print("---------------------------------\n")


# -------------------------------
# Activity 5: Condition-Controlled while Loop
# -------------------------------
print("Activity 5: While Loop (Sum until 100)")

total_sum = 0
count = 0

while total_sum < 100:
    user_input = input("Enter a number or press space to stop: ")

    if user_input == " ":
        break

    try:
        number = float(user_input)
        total_sum += number
        count += 1
    except ValueError:
        print("Invalid input.")

print("Total sum:", total_sum)
print("Numbers entered:", count)
print("---------------------------------\n")


# -------------------------------
# Activity 6: Count-Controlled for Loops
# -------------------------------
print("Activity 6: For Loops")

# Even numbers from 2 to 20
print("Even numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# Multiplication table (1 to 3)
print("Multiplication table for numbers 1 to 3:")
for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end=" ")
    print()
print()

# Reverse a string using reserved keyword
text = "Hello"
print("Reversing the string 'Hello':")
for char in reversed(text):
    print(char, end=" ")
print("\n---------------------------------\n")


# -------------------------------
# Activity 7: Turtle Graphics – Geometric Art
# -------------------------------
import turtle

print("Activity 7: Turtle Graphics (Geometric Pattern)")

ITERATIONS = 36
ANGLE = 10
SIZE = 100

screen = turtle.Screen()
pattern_turtle = turtle.Turtle()
pattern_turtle.speed(0)

for i in range(ITERATIONS):
    for _ in range(4):
        pattern_turtle.forward(SIZE)
        pattern_turtle.right(90)
    pattern_turtle.right(ANGLE)

turtle.done()