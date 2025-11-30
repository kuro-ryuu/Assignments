class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = 0
        self.traveled_distance = 0          #2000 for Ex3 check
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
        

if __name__ == "__main__":
    car = Car("ABC-123", 142)
    print(f"Registration: {car.registration}")
    print(f"Max speed: {car.max_speed} km/h")
    print(f"Current speed: {car.speed} km/h")
    print(f"Travelled distance: {car.traveled_distance} km")
    
    car.accelerate(30)
    print(f"Current speed: {car.speed} km/h")

    car.accelerate(70)
    print(f"Current speed: {car.speed} km/h")

    car.accelerate(50)                  #car.accelerate(-40) for Ex3 check
    print(f"Current speed: {car.speed} km/h")
    

    car.drive(1.5)
    print(f"Travelled distance: {car.traveled_distance} km")