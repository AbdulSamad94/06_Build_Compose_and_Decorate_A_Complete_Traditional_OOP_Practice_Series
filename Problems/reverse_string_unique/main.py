# def reverse_unique_chars(s: str):
#     unique_chars = []
#     for char in s:
#         if char not in unique_chars:
#             unique_chars.append(char)
#     unique_chars.reverse()
#     return "".join(unique_chars)


# output = reverse_unique_chars("abdulsamad")
# print(output)

# from abc import ABC, abstractmethod


# class Engine:
#     def start(self):
#         print("Engine started")


# class Car:
#     def __init__(self):
#         self.engine = Engine()  # Composition

#     def drive(self):
#         self.engine.start()  # Using Engine method
#         print("Car is moving")


# car = Car()
# car.drive()


# class Father:
#     def skills(self):
#         print("Gardening, Programming")


# class Mother:
#     def skills(self):
#         print("Cooking, Art")


# class Child(Father, Mother):
#     def skills(self):
#         # Agar child apna method define karta hai, to wo override karega
#         print("Sports, Music")


# # Object banao
# c = Child()
# c.skills()  # Output: Sports, Music


# # Agar child me method na ho to parent classes ke method kaise milte hain:
# class Child2(Mother, Father):
#     pass


# c2 = Child2()
# c2.skills()  # Output:  Gardening, Programming (Father class ka method call hoga kyunki wo pehle hai)
