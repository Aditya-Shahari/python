class A:
    def __init__(self):
        print("Constructor A")
        self.x = 400

    def valueX(self):
        print(self.x)


class B(A):
    def __init__(self):
        print("Constructor B")
        self.x = 300
        super().__init__()

    def valueX(self):
        print(self.x)
        super().valueX()


class C(A):
    def __init__(self):
        print("Constructor C")
        self.x = 200
        super().__init__()

    def valueX(self):
        print(self.x)
        super().valueX()


class D(B, C):
    def __init__(self):
        print("Constructor D")
        self.x = 100
        super().__init__()

    def valueX(self):
        print(self.x)
        super().valueX()


obj = D()
obj.valueX()