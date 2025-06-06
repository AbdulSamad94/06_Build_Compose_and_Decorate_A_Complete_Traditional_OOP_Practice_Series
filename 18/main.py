class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


p = Product(500)

print(p.price)    

p.price = 700     
print(p.price)    

del p.price  