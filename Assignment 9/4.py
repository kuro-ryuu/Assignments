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

def race(cars):
    while True:
        for c in cars:
            c.accelerate(random.randint(-10, 15))
            c.drive(1)
        if any(c.traveled_distance >= 10000 for c in cars):
            break





numbers = random.sample(range(1,11), 10)
cars = []
for n in numbers:
    car = Car(f"ABC-{n}", random.randint(100, 200))
    if car.registration not in cars:
        cars.append(car)
    else:
        pass
        
race(cars)

print(f"{'Registration':<16} {'Max Speed':<14} {'Covered Distance':<10}")
for c in cars:
    print(f"{c.registration:<16} {c.max_speed:<14} {c.traveled_distance:<10}")


