import random

class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = 0
        self.traveled_distance = 0
    def accelerate(self, amount):
        new_speed = self.speed + amount
        if new_speed > self.max_speed:
            self.speed = self.max_speed
        elif new_speed < 0:
            self.speed = 0
        else:
            self.speed = new_speed
        
    def drive(self, hours):
        self.traveled_distance += self.speed * hours

class ElectricCar(Car):
    def __init__(self, registration, max_speed, battery_capacity):
        super().__init__(registration, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration, max_speed, tank_volume):
        super().__init__(registration, max_speed)
        self.tank_volume = tank_volume
        

numbers = random.sample(range(1,11), 10)
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = []

        for n in numbers:
            car = Car(f"ABC-{n}", random.randint(100, 200))
            self.cars.append(car)
                
    def hours_passes(self):
        for c in self.cars:
            c.accelerate(random.randint(-10, 15))
            c.drive(1)

    def print_status(self):
        print(f"{'Registration':<16} {'Max Speed':<14} {'Last Recorded Speed':<23} {'Covered Distance'}")
        for c in self.cars:
            print(f"{c.registration:<16} {c.max_speed:<14} {c.speed:<23} {c.traveled_distance}")
    
    def race_finished(self):
        return any(c.traveled_distance >= self.distance for c in self.cars)

r = Race("Grand Demolition Derby", 8000, numbers)
hour = 0
while not r.race_finished():
    r.hours_passes()
    hour += 1
    if hour % 10 == 0:
        r.print_status()

r.print_status()



electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(100)  # set speed to 100 km/h
gasoline_car.accelerate(120)  # set speed to 120 km/h

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car {electric_car.registration} has traveled {electric_car.traveled_distance} km")
print(f"Gasoline car {gasoline_car.registration} has traveled {gasoline_car.traveled_distance} km")
