import turtle
import tkinter.simpledialog as simpledialog
# Define constant for pi
PI = 3.14159
print("whats your name and age")
name = input("name: ")
age = int(input("age: "))






def calculate_birth_year(name, age, answer):    
    if answer == "yes":
        value = 2026-age
    else:
        # to adjust for later birthday in the year
        value = 2026-age-1
    print(age)
    msg = print("Good day "+name+" u were born "+ str(value))
    return msg

def area_calculator():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("The area is " + str(area))
    return area

def make_sentence():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    string3 = input("Enter the third string: ")

    full_sentence = string1 + " " + string2 + " " + string3
    print("Full sentence:")
    print(full_sentence)

def print_table():
    print("Enter 3 column titles:")
    col1 = input("Column 1 title: ")
    col2 = input("Column 2 title: ")
    col3 = input("Column 3 title: ")

    print("\nEnter row data:")
    row1 = input("Row 1 data: ")
    row2 = input("Row 2 data: ")
    row3 = input("Row 3 data: ")

    # Print table header first print below adds a bunch of dashes 60 times for looks
    print("\n" + "-" * 60)
    print(f"{col1:<20}{col2:<20}{col3:<20}")
    print("-" * 60)

    # Print row ":<20" means left align within 20 spaces
    print(f"{row1:<20}{row2:<20}{row3:<20}")
    print("-" * 60)

def circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = PI * (radius ** 2)
    print("The area of the circle is:", area)

def perform_calculations():
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Integer Division:", a // b)
    print("Remainder:", a % b)
    print("Exponent:", a ** b)

def turtle_demo():
    # Set up the window
    window = turtle.Screen()
    window.title("Turtle Graphics Demo")

    # Create a turtle
    t = turtle.Turtle()

    # Pen setup
    t.pensize(3)
    t.color("blue")
    t.speed(5)  # Animation speed

    # Move and draw
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.left(90)

    # Pen up and move
    t.penup()
    t.goto(-100, 100)
    t.pendown()

    # Draw circle and dot
    t.circle(25)
    t.dot(10)

    # Change heading and color
    t.setheading(0)
    t.color("red")

    # Draw filled square
    t.begin_fill()
    for _ in range(4):
        t.forward(60)
        t.left(90)
    t.end_fill()

    # Display text
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.write("Hello Turtle!", align="center", font=("Arial", 16, "bold"))

    # Get user input
    user_name = simpledialog.askstring("Input", "What is your name?")
    if user_name:
        t.clear()
        t.write("Hello " + user_name + "!", align="center", font=("Arial", 16, "bold"))

    # Draw a filled circle
    t.color("green")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    # Hide turtle
    t.hideturtle()

    # Close window on click
    window.exitonclick()
def gross_pay_calculator():
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    gross_pay = hours_worked * hourly_rate
    print("Gross pay is: $" + str(gross_pay))
    






print("what would you like to do?: 1.calculate birth year 2.calculate area of rectangle 3.make sentence 4.print tablev 5.calculate circle area 6.perform calculations 7.turtle demo 8.gross pay calculator")

choice = input("Enter 1, 2, 3, 4, 5, 6, 7, 8: ")
if choice == "1":
    print(name + " Has your birthday happened yet?")
    answer = input("answer yes or no : ").lower()
    calculate_birth_year(name, age, answer)
elif choice == "2":
    area_calculator()
elif choice == "3":
    make_sentence()
elif choice == "4":
    print_table()
elif choice == "5":
    circle_area()
elif choice == "6":
    perform_calculations()
elif choice == "7":
    turtle_demo()
elif choice == "8":
    gross_pay_calculator()




