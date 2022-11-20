
from abc import ABC, abstractmethod

class Boss(ABC):
    def time_office(self):
        print("10 am at office")

    def lunch_time(self):
        print("lunch at 1 pm")

    @abstractmethod
    def sal(self):
        print("salary of boss")


class Employee(Boss):
    def sal(self):
        print("salary of employee")


class Manager(Boss):
    def sal(self):
        print("salary of manager")

obj = Employee()
obj.sal()
print(dir(obj))

