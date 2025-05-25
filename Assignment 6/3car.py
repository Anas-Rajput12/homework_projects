class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started")

my_car = Car("BMW")
print(my_car.brand)
my_car.start()
