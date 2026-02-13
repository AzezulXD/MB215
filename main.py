from car import Car

# Activity 7: Compare function
def compare_car_years(car1, car2):
    return car1.year < car2.year


def main():

    # Create two instances
    car1 = Car("Toyota", "Camry", 2018)
    car2 = Car("Honda", "Civic", 2022)

    # Display info
    car1.display_info()
    car2.display_info()

    # Show __str__ usage
    print(car1)
    print(car2)

    # Update model using public wrapper
    car1.change_model("Corolla")
    print("After model update:")
    car1.display_info()

    # Compare years
    result = compare_car_years(car1, car2)

    if result:
        print("Car1 is older than Car2")
    else:
        print("Car1 is newer or same age as Car2")


if __name__ == "__main__":
    main()