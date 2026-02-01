import random
import traceback

# =========================
# Part 1: Functions & Randomness
# =========================

# Activity 1: Customizable Dice Simulator
def roll_dice(num_dice, num_sides):
    """
    Rolls a given number of dice with a given number of sides
    and returns the total value.
    """
    total = 0
    for _ in range(num_dice):
        total += random.randint(1, num_sides)
    return total


# Activity 2: Temperature Converter
def convert_temperature(temp, unit):
    """
    Converts temperature between Celsius and Fahrenheit.
    unit should be 'C' or 'F'
    """
    if unit.upper() == 'C':
        # Celsius to Fahrenheit
        return (temp * 9 / 5) + 32
    elif unit.upper() == 'F':
        # Fahrenheit to Celsius
        return (temp - 32) * 5 / 9
    else:
        return None


# Activity 3: Generate a Single Random Number
def generate_random_number(min_val, max_val):
    """
    Generates a random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)


# Activity 4: Investment Simulator
def simulate_investment(amount, years, rate_min, rate_max):
    """
    Simulates investment growth over a number of years
    using a random annual interest rate.
    """
    current_amount = amount

    for _ in range(years):
        rate = random.uniform(rate_min, rate_max)
        current_amount += current_amount * rate

    return current_amount


# Demonstrating Part 1 Functions
if __name__ == "__main__":

    # Dice Simulation
    print("Rolling 3 dice with 6 sides each:", roll_dice(3, 6))

    # Temperature Conversion
    print("Converting 100F to Celsius:", convert_temperature(100, 'F'))
    print("Converting 0C to Fahrenheit:", convert_temperature(0, 'C'))

    # Generate a Single Random Number
    random_number = generate_random_number(1, 100)
    print(f"The generated random number is: {random_number}")

    # Investment Simulation
    final_amount = simulate_investment(1000, 5, 0.03, 0.08)
    print(f"Final investment value after 5 years: ${final_amount:.2f}")



# =========================
# Part 2: File Operations & Exception Handling
# =========================

# Activity 1: Writing to a File (Provided)
def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except Exception:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()


# Activity 2: Reading from a File
def read_from_file(filename):
    """
    Reads content from a file and returns it.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception:
        print(f"An error occurred while reading the file: {filename}")
        traceback.print_exc()
        return None


# Activity 3: Appending to a File
def append_to_file(filename, data):
    """
    Appends data to an existing file.
    """
    try:
        with open(filename, 'a') as file:
            file.write(data)
    except Exception:
        print(f"An error occurred while appending to the file: {filename}")
        traceback.print_exc()


# Demonstrating File Functions
if __name__ == "__main__":

    # Writing to a file
    write_to_file('sample.txt', 'Hello, World!\n')

    # Reading from a file
    content = read_from_file('sample.txt')
    if content is not None:
        print("File content:")
        print(content)

    # Appending to a file
    append_to_file('sample.txt', 'This line was appended.\n')

    # Reading again after appending
    content = read_from_file('sample.txt')
    if content is not None:
        print("Updated file content:")
        print(content)

    # Demonstrating exception handling
    non_existent_content = read_from_file('non_existent_file.txt')
    if non_existent_content is None:
        print("Could not read the non-existent file.")