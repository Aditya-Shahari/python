class Cric:
    format = "T20"

    def __init__(self, name, jerNo):
        self.name = name
        self.jerNo = jerNo

    @classmethod
    def display(cls):
        cls.format = "OneDay"

    # def printData(self):
    #     self.format = "Test"

player1 = Cric("Dhoni", 7)
player2 = Cric("Virat", 18)

print(player1.format)
print(player2.format)

# player1.printData()
player1.display()

print(player1.format)
print(player2.format)
