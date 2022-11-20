# operator overloading on objects of two different classes?

class First:
    def __init__(self):
        self.x = 10

    def disp(self):
        print(self.x)

    def __add__(self, obj):             # __add__ must be in first object/class
        return self.x + obj.x


class Second:
    def __init__(self):
        self.x = 20

    def disp(self):
        print(self.x)


obj1 = First()
obj1.disp()
obj2 = Second()
obj2.disp()

print(obj1 + obj2)