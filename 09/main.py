from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, name: str, width: float, height: float) -> None:
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


if __name__ == "__main__":
    rectangle = Rectangle("My Rectangle", 5, 10)
    print(f"The area of {rectangle.name} is: {rectangle.area()}")
