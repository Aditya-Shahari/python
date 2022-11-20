# Method overloading is not possible in Python by inbuilt functions.
# It can be still achieved by 1) if-else code 2) decorator

class Addition:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z


obj = Addition()
print(obj.add(2, 4))
print(obj.add(2, 4, 5))