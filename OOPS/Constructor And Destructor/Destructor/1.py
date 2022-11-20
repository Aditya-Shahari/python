class Movie:
    def __init__(self):
        print("In constructor")
        self.mname = "RRR"
        self.director = "SSR"

    def info(self):
        print(self.mname)
        print(self.director)

    def __del__(self):
        print("Deleting object")


movie1 = Movie()
print(movie1)
movie1.info()
del movie1
movie2 = Movie()
print(movie2)
movie2.info()
print(movie1)