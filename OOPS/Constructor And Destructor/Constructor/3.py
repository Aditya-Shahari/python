class Movie:
    def __init__(self):
        print("In constructor")
        self.mname = "RRR"
        self.director = "SSR"

    def info(self):
        print(self.mname)
        print(self.director)

    def __new__(cls):
        print("Memory allocation")
        return super().__new__(cls)


movie1 = Movie()
print(movie1)
movie1.info()