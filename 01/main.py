class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"The student's name is {self.name} and age is {self.age}.")


student = Student("Abdul Samad", 17)
student.display()
