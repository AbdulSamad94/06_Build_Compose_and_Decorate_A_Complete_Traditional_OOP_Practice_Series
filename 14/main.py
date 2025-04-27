class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")


class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

    def display(self):
        print(f"Department Name: {self.name}")
        self.employee.display()


emp1 = Employee("Ali", 1)
dept1 = Department("IT Department", emp1)

dept1.display()

print("\nEmployee object abhi bhi exist karta hai:")
emp1.display()
