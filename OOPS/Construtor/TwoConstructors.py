class TwoConstructors:
    def __init__(self, name, std_id):
        print("In Constructor 1")
        self.name = name
        self.std_id = std_id

    def __init__(self, company, name):
        print("In Constructor 2")
        self.company = company


    def display(self):
        print(self.name)

obj1 = TwoConstructors("Badhe", 105)


