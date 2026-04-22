
# 3-m
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def check_pass(self):
        if self.grade >= 60:
            print(f"{self.name} o'tdi")
        else:
            print(f"{self.name} yiqildi")

    def info(self):
        print(f"Ism: {self.name}")
        print(f"Baho: {self.grade}")


s = Student("Ali", 70)

s.info()
s.check_pass()


# 4-m
class CarFuel:
    def __init__(self, model, fuel):
        self.model = model
        self.fuel = fuel

    def drive(self, km):
        self.fuel -= km
        print(f"{km} km yurildi, yoqilg‘i: {self.fuel}L")

    def refuel(self, amount):
        self.fuel += amount
        print(f"Yoqilg‘i to‘ldirildi: {self.fuel}L")


car = CarFuel("Cobalt", 30)
car.drive(10)
car.refuel(10)
