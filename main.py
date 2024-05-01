import random
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, model, color, volume, fuel):
        self.model = model
        self.color = color
        self.volume = volume
        self.fuel = fuel
        self._fuel_level = random.randrange(0, 9)
        self.trip_distance = 0

    @property
    def fuel_level(self):
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, value):
        if value < 0:
            self._fuel_level = 0
        elif value > 10:
            self._fuel_level = 10
        else:
            self._fuel_level = value

    @abstractmethod
    def move(self, distance):
        pass

class BMW(Car):
    def __init__(self, model, color):
        super().__init__("X5", "Black", 3.0, "diesel")

    def move(self, distance):
        distance_travelled = random.randrange(0, distance + 1)
        self.trip_distance += distance_travelled
        self.fuel_level -= distance_travelled
        return distance_travelled

class Toyota(Car):
    def __init__(self, model, color):
        super().__init__("Celica", "Silver", 1.8, "petrol")

    def move(self, distance):
        distance_travelled = random.randrange(0, distance + 1)
        self.trip_distance += distance_travelled
        self.fuel_level -= distance_travelled
        return distance_travelled

class Audi(Car):
    def __init__(self, model, color):
        super().__init__("R8", "Black", 3.5, "petrol")

    def move(self, distance):
        distance_travelled = random.randrange(0, distance + 1)
        self.trip_distance += distance_travelled
        self.fuel_level -= distance_travelled
        return distance_travelled

desired_dist = 100
max_distance = 0
winner = None

car1 = BMW("X5", "Black")
car2 = Toyota("Celica", "Silver")
car3 = Audi("R8", "Black")

while not winner:
    for car in [car1, car2, car3]:
        if car.trip_distance >= desired_dist:
            winner = car
            break
        distance = random.randrange(0, 9)
        distance_travelled = car.move(distance)
        if car.trip_distance > max_distance:
            max_distance = car.trip_distance

if winner:
    print(f"Победитель - {winner.model}! Он проехал {winner.trip_distance} расстояния.")
else:
    print("На этот раз победителя нет.")

for car in [car1, car2, car3]:
    print(f"{car.model} проехал {car.trip_distance} расстояния и имеет {car.fuel} топлива.")
