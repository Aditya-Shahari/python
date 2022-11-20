class Meta:
    def __init__(self, child1, child2):
        print("In constructor")
        self.child1 = child1
        self.child2 = child2

    def disp(self):
        print(self.child1)
        print(self.child2)


mark = Meta("Facebook", "Whatsapp")
mark.disp()