class A:
    def __init__(self):
        super().__init__()
        print("A")


class B:
    def __init__(self):
        print("B")


class D:
    def __init__(self):     # not called because B does not have super call
        print("D")


class C(A, B, D):
    def __init__(self):
        super().__init__()
        print("C")


obj1 = C()
print(C.mro())