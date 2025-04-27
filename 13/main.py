class Engine:
    def start(self):
        print("Engine is starting...")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        print("Car is trying to start...")
        self.engine.start()


engine = Engine()

car = Car(engine)

car.start_car()
