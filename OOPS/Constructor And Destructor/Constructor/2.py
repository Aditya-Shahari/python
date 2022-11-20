class Movie:
    def __init__(self):
        print("In constructor")
        self.mname = "RRR"
        self.director = "SSR"

    def info(self):
        print(self.mname)
        print(self.director)

    def __new__(self):
        print("Memory allocation")


movie1 = Movie()        # Constructor not initialized, no memory allocation
print(movie1)
movie1.info()