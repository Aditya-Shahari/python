class Cric:
    format = "T20"

    def __init__(self, name, jerNo):
        self.name = name
        self.jerNo = jerNo

    @classmethod
    def display(cls):
        print(cls)
        print(cls.format)


player1 = Cric("Dhoni", 7)
player2 = Cric("Virat", 18)

Cric.display()
player1.display()