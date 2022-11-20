
class X:
    def __init__(self):
        super().__init__()
        print("X")


class A(X):
    def __init__(self):
        super().__init__()
        print("A")


class B(X):
    def __init__(self):
        super().__init__()
        print("B")


class D:
    def __init__(self):
        super().__init__()
        print("D")


class C(A, B, D):
    def __init__(self):
        super().__init__()
        print("C")


obj1 = C()
print(C.mro())