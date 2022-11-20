class Outer:
    x = 10

    def __init__(self):
        print("Outer Constructor")
        self.out = 10


    class Inner:
        y = 20

        def __init__(self):
            print("Inner Constructor")
            self.inn = 20

        def dispIn(self):
            print(self.inn)
            print(self.y)


    def dispOut(self):
        print(self.out)
        print(self.x)


objOut = Outer()
objOut.dispOut()

objInn = objOut.Inner()
objInn.dispIn()




