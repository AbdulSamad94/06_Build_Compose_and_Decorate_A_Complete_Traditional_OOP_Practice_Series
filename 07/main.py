class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn


emp = Employee("Hamza", 50000, "123-45-6789")
print(emp.get_ssn())
print("Name (Public):", emp.name)

print("Salary (Protected):", emp._salary)

# print("SSN (Private):", emp.__ssn)
