class PoliParty:
    def __init__(self):
        print("In constructor")
        self.pname = "NCP"
        self.symbol = "Alarm clock"

    def dispParty(self):
        print(self.pname)
        print(self.symbol)

obj1 = PoliParty()
obj1.dispParty()
print(obj1.dispParty)
print(type(obj1.dispParty))
# functions are stored directly in heap
# methods are stored inside namespace
