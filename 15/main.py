class A:
    def show(self):
        print("showing A")


class B(A):
    def show(self):
        print("showing B")


class C(A):
    def show(self):
        print("showing C")


class D(B, C):
    pass


d = D()
d.show()
