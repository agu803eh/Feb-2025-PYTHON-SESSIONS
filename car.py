class Car:
    def __init__(self, color, model, year, mileage):
        self.color = color    # Instance variable
        self.model = model    # Instance variable
        self.year = year      # Instance variable
        self.mileage = mileage

# Creating objects with unique attributes
car1 = Car("blue", "Sedan", 2020, 15000)
car2 = Car("red", "SUV", 2021, 12000)
car3 = Car("green", "Truck", 2019, 20000)



class Bicycle:
    def __init__(self, color, brand, model, year):
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year


bicycle1 = Bicycle("red", "Giant", "Escape 3", 2022)
bicycle2 = Bicycle("blue", "Trek", "FX 3", 2021)
bicycle3 = Bicycle("green", "Specialized", "Sirrus X 4.0", 2023)

class Airplane:
    def __init__(self, color, model, year, capacity):
        self.color = color
        self.model = model
        self.year = year
        self.capacity = capacity

        # Creating objects with unique attributes
airplane1 = Airplane("white", "Boeing 747", 2018, 400)
airplane2 = Airplane("blue", "Airbus A320", 2020, 180)
airplane3 = Airplane("red", "Cessna 172", 2021, 4)



# Demonstrating polymorphism
vehicles = [car1, car2, car3, bicycle1, bicycle2, bicycle3, airplane1, airplane2, airplane3]
for vehicle in vehicles:
    print(f"Vehicle Type: {vehicle.__class__.__name__}")
    print(f"Color: {vehicle.color}")
    print(f"Model: {vehicle.model}")
    print(f"Year: {vehicle.year}")
    if hasattr(vehicle, 'mileage'):
        print(f"Mileage: {vehicle.mileage}")
    if hasattr(vehicle, 'brand'):
        print(f"Brand: {vehicle.brand}")
    if hasattr(vehicle, 'capacity'):
        print(f"Capacity: {vehicle.capacity}")
    print()

    # Adding move methods to each class
    def car_move(self):
        print("Driving")

    def bicycle_move(self):
        print("Pedaling")

    def airplane_move(self):
        print("Flying")

    # Assigning move methods to each class
    Car.move = car_move
    Bicycle.move = bicycle_move
    Airplane.move = airplane_move

    # Printing the move type for all vehicle types
    for vehicle in vehicles:
        print(f"The move type for the {vehicle.__class__.__name__} is: ", end="")
        vehicle.move()
        print()

        