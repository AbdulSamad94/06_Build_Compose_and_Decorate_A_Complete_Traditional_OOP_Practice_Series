class Engine:
    def __init__(self, fuel_type="gasoline", horsepower=150):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def start(self):
        print(
            f"Engine started. Fuel type: {self.fuel_type}, Horsepower: {self.horsepower}"
        )

    def stop(self):
        print("Engine stopped.")

    def get_fuel_type(self):
        return self.fuel_type

    def get_horsepower(self):
        return self.horsepower


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start(self):
        print(f"Starting the {self.make} {self.model}...")
        self.engine.start()

    def stop(self):
        print(f"Stopping the {self.make} {self.model}...")
        self.engine.stop()

    def get_engine_fuel_type(self):
        return self.engine.get_fuel_type()

    def get_engine_horsepower(self):
        return self.engine.get_horsepower()


if __name__ == "__main__":
    my_engine = Engine("diesel", 200)
    my_car = Car("Ford", "F-150", my_engine)

    my_car.start()
    print(f"Fuel type: {my_car.get_engine_fuel_type()}")
    print(f"Horsepower: {my_car.get_engine_horsepower()}")
    my_car.stop()
