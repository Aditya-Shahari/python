# class Addition:
#     def add(self, x = None, y = None, z):
#         return x + y + z
#
# obj = Addition()


 class Addition:
    def add(self, x = None, y = None, z = None):
        if x != None and y != None and z != None:
            sum = x + y + z

        elif x != None and y != None:
            sum = x + y

        return sum

obj = Addition()