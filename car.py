# car.py

class Car:

    # Activity 1 + 3: Initialize attributes (model is private)
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model     # private attribute
        self.year = year

    # Activity 2: Public method
    def display_info(self):
        print(f"Car Info -> Make: {self.make}, Model: {self.__model}, Year: {self.year}")

    # Activity 2: Private method
    def __update_model(self, new_model):
        self.__model = new_model

    # Public wrapper so we can demonstrate update (optional but useful)
    def change_model(self, new_model):
        self.__update_model(new_model)

    # Activity 4: __str__ method
    def __str__(self):
        return f"{self.year} {self.make} {self.__model}"