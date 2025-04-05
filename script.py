class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.brand} {self.model} is starting")

    def stop(self):
        print(f"The {self.brand} {self.model} is stopping")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

    def start(self):
        print(f"Car: The {self.brand} {self.model} is starting")


class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

    def start(self):
        print(f"Bike: The {self.brand} {self.model} is starting")


# car = Car("Toyota", "Camry", 2015, 4, 4)
# bike = Bike("Honda", "Civic", 2018, 2)

vehicles = [
    Car("Toyota", "Camry", 2015, 4, 4),
    Bike("Honda", "Civic", 2018, 2),
    Car("Ford", "Mustang", 2020, 4, 4),
    Bike("Suzuki", "GSX-R", 2019, 2),
]
for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(type(vehicle).__name__)
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Not a vehicle")
