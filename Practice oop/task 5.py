class Vehicle:
    color = 'white'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

B = Bus('School Volvo', 180, 12)
A = Car('Audi Q5', 240, 18)

print(f'Color: {B.color}, Vehicle name: {B.name}, Speed: {B.max_speed}, Mileage: {B.mileage}')
print(f'Color: {A.color}, Vehicle name: {A.name}, Speed: {A.max_speed}, Mileage: {A.mileage}')