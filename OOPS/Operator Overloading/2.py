class Xyz:
    def __init__(self):
        self.x = 10
        self.y = 20

    def show(self):
        print(self.x)
        print(self.y)

    def __add__(self, obj):
        return self.x + obj.x


obj1 = Xyz()
obj2 = Xyz()

print(obj1 + obj2)