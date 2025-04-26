# Python OOP Assignments ✅

## 1. Using `self`
Created a class `Student` with attributes `name` and `marks`, initialized using `self` inside a constructor. Added a `display()` method to print student details.

---

## 2. Using `cls`
Created a class `Counter` with a class variable to track the number of objects created, using a class method with `cls` to display and manage the count.

---

## 3. Public Variables and Methods
Created a class `Car` with a public variable `brand` and a public method `start()`. Accessed both from outside the class.

---

## 4. Class Variables and Class Methods
Created a class `Bank` with a class variable `bank_name`. Added a class method `change_bank_name(cls, name)` to change the bank name, affecting all instances.

---

## 5. Static Variables and Static Methods
Created a class `MathUtils` with a static method `add(a, b)` to return the sum, without using class or instance variables.

---

## 6. Constructors and Destructors
Created a class `Logger` that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

---

## 7. Access Modifiers: Public, Private, and Protected
Created a class `Employee` with:
- A public variable `name`
- A protected variable `_salary`
- A private variable `__ssn`

Tested accessing all variables and observed access behavior.

---

## 8. The `super()` Function
Created a class `Person` with a constructor for `name`. Created a subclass `Teacher` that added `subject` and used `super()` to call the base class constructor.

---

## 9. Abstract Classes and Methods
Used the `abc` module to create an abstract class `Shape` with an abstract method `area()`. Created a subclass `Rectangle` that implemented `area()`.

---

## 10. Instance Methods
Created a class `Dog` with instance variables `name` and `breed`. Added an instance method `bark()` that printed a message with the dog's name.

---

## 11. Class Methods
Created a class `Book` with a class variable `total_books`. Added a class method `increment_book_count()` to increase the book count.

---

## 12. Static Methods
Created a class `TemperatureConverter` with a static method `celsius_to_fahrenheit(c)` that returned the Fahrenheit value.

---

## 13. Composition
Created a class `Engine` and a class `Car`. Used composition by passing an `Engine` object to the `Car` class and accessing the `Engine` method through the `Car`.

---

## 14. Aggregation
Created a class `Department` and a class `Employee`. Used aggregation by storing a reference to an independent `Employee` object inside `Department`.

---

## 15. Method Resolution Order (MRO) and Diamond Inheritance
Created four classes:
- `A` with a method `show()`
- `B` and `C` inherited from `A` and overrode `show()`
- `D` inherited from `B` and `C`

Tested MRO behavior by creating an object of `D` and calling `show()`.

---

## 16. Function Decorators
Created a function decorator `log_function_call` that printed a message before executing a function. Applied it to `say_hello()`.

---

## 17. Class Decorators
Created a class decorator `add_greeting` that added a `greet()` method to the decorated class. Applied it to `Person`.

---

## 18. Property Decorators: `@property`, `@setter`, and `@deleter`
Created a class `Product` with a private attribute `_price`. Used `@property` to get the price, `@price.setter` to update it, and `@price.deleter` to delete it.

---

## 19. `callable()` and `__call__()`
Created a class `Multiplier` with a `__call__()` method to multiply a value by a factor. Tested using `callable()` and by calling the object like a function.

---

## 20. Creating a Custom Exception
Created a custom exception `InvalidAgeError`. Wrote a function `check_age(age)` that raised this exception if `age < 18`, and handled it with `try...except`.

---

## 21. Make a Custom Class Iterable
Created a class `Countdown` that implemented `__iter__()` and `__next__()` to make the object iterable, counting down to 0 in a for-loop.

---

## ✅ All assignments completed successfully! 🚀  
[Submit Here](https://forms.gle/tS7C3sr55tUZ36GY8)
