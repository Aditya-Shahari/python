class Parent:
    def __init__(self):             # instance variable not initialised, child constructor overrides parent constructor
        print("Parent constructor")
        self.x = 10

    def disp(self):
        print(self.x)

class Child(Parent):
    def __init__(self):
        print("Child constructor")
        self.y = 20

    def show(self):
        print(self.x)
        print(self.y)


obj = Child()
obj.disp()