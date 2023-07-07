class Car:

    wheels = 4

    def __init__(self):
        self.mileage = 10
        self.company = "Lambo"

car1 = Car()
car2 = Car()

car1.mileage = 7

print(car1.company, car1.mileage, car1.wheels)
print(car2.company, car2.mileage, car2.wheels)