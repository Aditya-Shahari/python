class Cafe:
    menucard = 1

    def __init__(self, dish):
        self.dish = dish

    def display(self):
        print(self.dish)
        print(Cafe.menucard)

obj1 = Cafe("Burger")
obj1.display()

obj2 = Cafe("Large fries")
obj2.display()
