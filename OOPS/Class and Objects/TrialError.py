class Company:
    # class variables
    cname = "Google"
    workplace = "Mumbai"

    def __init__(self, department):
        self.department = department

    def hire(self):
        print("Hired an employee")

    @classmethod
    def facilities(cls):
        print("Provides all facilities")
        print(cls.cname)
        print(cls.workplace)


class Employee(Company):
    role = "Developer"

    def __init__(self, empId, lang):
        super().__init__()
        self.empId = empId
        self.lang = lang

    def info(self):
        print(self.empId)
        print(self.lang)
        print(self.workplace)

    @classmethod
    def skillset(cls):
        print(cls.role)




# emp1 = Employee(25, "Python")
#
# emp1.info()
# Company.workplace = "Hijewadi"
# Employee.role = "Tester"
# Employee.workplace = "Camp"
# emp1.info()
#
# emp2 = Employee(35, "Java")
# emp2.info()
