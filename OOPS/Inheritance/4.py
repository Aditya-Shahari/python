class Company:
    def __init__(self, cname, total_emp):
        self.cname = cname
        self.total_emp = total_emp

    def company_info(self):
        print(self.cname)
        print(self.total_emp)


class Employee(Company):
    def __init__(self, e_name, e_id, cname, total_emp):
        super().__init__(cname, total_emp)
        self.e_name = e_name
        self.e_id = e_id

    def e_info(self):
        print(self.e_name)
        print(self.e_id)


obj = Employee("aditya", 2, "veritas", 200)
obj.e_info()
obj.company_info()