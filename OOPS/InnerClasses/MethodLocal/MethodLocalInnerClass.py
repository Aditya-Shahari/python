class Outer:

    def __init__(self):
        print("Outer constructor")
        self.x = 10

    def dispData(self):
        print(self.x)

        class Inner:
            def __init__(self):
                print("Inner constructor")
                self.y = 20

            def dispData(self):
                print(self.y)

        z = 40
        print(z)

        innObj = Inner()
        innObj.dispData()
        print(innObj)

outObj = Outer()
outObj.dispData()