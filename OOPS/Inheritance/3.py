class Company:
    def __init__(self):
        self.cname = "Amazon"
        self.noEmp = 200

    def info(self):
        print(self.cname)
        print(self.noEmp)

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.ename = "Aditya"
        self.eId = 1

    def info(self):
        super().info()
        print(self.ename)
        print(self.eId)


obj = Employee()
obj.info()