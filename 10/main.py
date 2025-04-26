class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")


if __name__ == "__main__":
    my_dog = Dog("Buddy", "Golden Retriever")
    my_dog.bark()

    another_dog = Dog("Lucy", "Poodle")
    another_dog.bark()
