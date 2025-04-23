class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")


my_car = Car("Toyota")
my_car.start()
print(f"Car brand: {my_car.brand}")
