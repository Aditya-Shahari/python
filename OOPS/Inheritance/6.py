class Parent(object):
    x = 10

    def __init__(self):
        print("Parent constructor")
        self.y = 20

    @classmethod
    def show(cls):
        print(cls.x)


class Child(Parent):
    x = 110

    def __init__(self):
        super().__init__()
        print("Child constructor")

    @classmethod
    def disp(cls):
        print(cls.x)
        #print(Parent.x)
        print(super().x)


obj = Child()
obj.disp()