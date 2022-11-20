class Employee:
    cname = "Veritas"

    def __init__(self):
        self.empName = "Jeevan"
        self.empId = 4

    def display(self):
        print(self.empName)
        print(self.empId)


obj = Employee()

print(obj.empName)
#Employee.init()
obj.empName = "Aditya"

print(obj.empName)
print(obj.empId)

# maybe the answer is we cannot access instance variables from other classes
# because if I try to change it using obj name it works
