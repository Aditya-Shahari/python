class Cafe:
    menucard = 1

    def __init__(self, dish):
        self.dish = dish

    def order(self):
        print(self.dish)
        self.menucard = 0


obj1 = Cafe("Burger")
obj2 = Cafe("Large fries")

print(obj1.menucard)
print(obj2.menucard)
obj1.order()
print(obj1.menucard)
print(obj2.menucard)