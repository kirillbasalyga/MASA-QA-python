class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def get_info(self):
        return f'Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}'
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

B = Bus('School Volvo', 180, 12)
print(B.get_info())