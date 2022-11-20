class Cric:
    matchFormat = "T20"

    def myClassMethod(fun):

        def inner(*args):
            fun(args[0].__class__)

        return inner()

    def __init__(self):
        self.name = "Dhoni"
        self.jerName = 7

    def disp(self):
        print(self.name)
        print(self.jerName)

    @myClassMethod
    def dispForm(cls):
        print(cls.matchFormat)


player1 = Cric()
player1.disp()

print(player1)
player1.dispForm()