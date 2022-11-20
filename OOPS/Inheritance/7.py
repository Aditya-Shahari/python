class Company:
    cname = "Veritas"
    workplace = "Baner"

    def __init__(self):
        #print("Company constructor")
        self.teamCode = "Python Code"

    @classmethod
    def facilities(cls):
        print("Provides all facilities")
        print(cls.cname)
        print(cls.workplace)


class Employee(Company):
    role = "Developer"

    def __init__(self, empId, lang):
        super().__init__()
        #print("Child constructor")
        self.empId = empId
        self.lang = lang

    def info(self):
        print(self.empId)
        print(self.role)
        print(self.workplace)

    @classmethod
    def skillset(cls):
        print(cls.role)


emp1 = Employee(25, "Python developer")

emp1.info()
Company.workplace = "Hijewadi"
Employee.role = "Tester"
Employee.workplace = "Camp"
emp1.info()

emp2 = Employee(35, "Java developer")
emp2.info()

# 3 cases:
# 1 if you change variable with obj name it will for that objects scope only new variable will not share the same answer
# 2 if you change variable with class name of child it will reflect the change on all the objects created
# 3 if you change variable with parent class name and change the same variable with child class name then the change
# made by child class name will be used