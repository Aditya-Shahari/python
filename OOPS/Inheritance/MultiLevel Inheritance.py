class Parent(object):
    x = 10
    def __init__(self):
        print("Parent constructor")
        self.y = 20
        
    @classmethod
    def show(cls):
        print(cls.x)

    def disp(self):
        print(self.x)
        print(self.y)


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

    def childDisp(self):
        print(self.x)
        print(self.y)

obj = Child()
obj.childDisp()
obj.show()
obj.disp()