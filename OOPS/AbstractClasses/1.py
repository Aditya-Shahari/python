class Parent:
    def property(self):
        print("Jameen, paise, car")

    def marry(self):
        pass


class Child(Parent):
    pass


obj = Child()
obj.property()
obj.marry()