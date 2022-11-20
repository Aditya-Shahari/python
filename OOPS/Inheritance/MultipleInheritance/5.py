class A:
    def __init__(self):
        print("A")


class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")


obj1 = C()
print(C.mro())

