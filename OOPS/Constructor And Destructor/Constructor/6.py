class Youtube:
    def __del__(self):
        print("In constructor")
        self.pname = "Google"

    def disp(self):
        print("Object. . . ")

    def __new__(cls):
        print("Object Creation")
        return super().__new__(cls)

    def __del__(self):
        print("Deleting Object")

obj1 = Youtube()
obj2 = obj1
del obj1
print("End")