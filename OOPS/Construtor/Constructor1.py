class Cafe:
    def __init__(self):
        self.x = 10
        self.y = 20

obj1 = Cafe()
print(obj1.x)
print(id(obj1.x))
print(obj1.y)

obj2 = Cafe()
print(obj2.x)
print(id(obj2.x))
print(obj2.y)

