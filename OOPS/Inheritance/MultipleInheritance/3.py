class Parent1:
    def __init__(self):
        super().__init__()
        print("Parent1 constructor")

class Parent2:
    def __init__(self):
        super().__init__()
        print("Parent2 constructor")


class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        print("Child constructor")

obj1 = Child()
print(Child.mro())
