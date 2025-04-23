class Person:
    def __init__(self, name: str):
        self.name = name


class Teacher(Person):
    def __init__(self, name: str, sub: str):
        super().__init__(name)
        self.sub = sub


my_teacher = Teacher("Afzal Ali", "Maths")
print(f"Teacher's Name: {my_teacher.name}, Subject: {my_teacher.sub}")
