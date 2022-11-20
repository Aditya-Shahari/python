class Parent:
    def __init__(self):
        print("Parent constructor")
        self.x = 10

    def disp(self):
        print(self.x)

class Child(Parent):
    pass


obj = Child()
obj.disp()