class Outer:
    clsOuter = 40

    def __init__(self):
        print("Outer Constructor")
        self.x = 10

    def dispOut(self):
        print(self.x)

    @classmethod
    def dispCls(cls):
        print(cls.clsOuter)

    class Inner:

        def __init__(self, outObj):
            print("Inner Constructor")
            self.y = 20
            self.outObj = outObj

        def dispIn(self):
            print(self.outObj.x)
            print(self.outObj.dispCls)


outObj = Outer()
innObj = outObj.Inner(outObj)
innObj.dispIn()






