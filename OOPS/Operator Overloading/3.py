class Xyz:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        return self.x + obj.x, self.y + obj.y
    #
    # def __eq__(self, obj):
    #
    # def __ne__(self, obj):
    #
    # def __ge__(self, obj):
    #
    # def __gt__(self, obj):
    #
    # def __le__(self, obj):
    #
    # def __lt__(self, obj):



obj1 = Xyz(10, 15)
obj2 = Xyz(5, 20)

print(obj1 + obj2)

print(dir(Xyz))


