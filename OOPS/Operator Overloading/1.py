class Xyz:
    def __init__(self):
        self.x = 10
        self.y = 20

    def show(self):
        print(self.x)
        print(self.y)


obj1 = Xyz()
obj2 = Xyz()

obj1.show()
obj2.show()

print(obj1 +  obj2)