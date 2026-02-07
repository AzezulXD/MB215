import math

def kilo_to_miles():
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371
    miles_rounded = round(miles, 2)
    print(f"{kilometers} km is equal to {miles_rounded} miles")

def numeric_grade():
    score = float(input("Enter your numeric grade: "))
    if score >= 90:
        grade = 'A+'
    elif score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Your letter grade is: {grade}")

def cylinder_volume():
    diameter = float(input("Enter the diameter of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
        
    pi = 3.141592
    pi_rounded = round(pi, 2)
        
    radius = diameter / 2
    volume = pi_rounded * (radius ** 2) * height
    
    print(f"The volume of the cylinder is: {volume}")

def activity4_boolean_variables():
    # Step 1: Declare two Boolean variables
    is_sunny = True
    is_raining = False

    print("Boolean variables:")
    print("is_sunny =", is_sunny)
    print("is_raining =", is_raining)
    print()

    # Step 2: Demonstrate logical operations (AND, OR, NOT)

    # Logical AND
    print("Logical AND (is_sunny and is_raining):", is_sunny and is_raining)

    # Logical OR
    print("Logical OR (is_sunny or is_raining):", is_sunny or is_raining)

    # Logical NOT
    print("Logical NOT (not is_sunny):", not is_sunny)
    print()

    # Step 3: Use a Boolean variable in a conditional statement
    if is_sunny:
        print("It's sunny outside.")
    else:
        print("It's not sunny outside.")

    # Conditional statement with logical operation
    if is_sunny and not is_raining:
        print("Perfect weather for a walk!")
    else:
        print("Maybe stay inside today.")


