class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.num_doors}")


class Bike(Vehicle):
    def __init__(self, brand, speed, type_bike):
        super().__init__(brand, speed)
        self.type_bike = type_bike

    def display_info(self):
        super().display_info()
        print(f"Type: {self.type_bike}")


# Example usage
car = Car("Toyota", 180, 4)
bike = Bike("Yamaha", 120, "Sport")

car.display_info()
# Brand: Toyota, Speed: 180 km/h
# Doors: 4

bike.display_info()
# Brand: Yamaha, Speed: 120 km/h
# Type: Sport
