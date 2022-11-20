class Student:

    def __init__(self, name, std_id):
        self.name = name
        self.std_id = std_id

    def display(self):
        print(self.name)
        print(self.std_id)


print("Enter student 1 data")
name = input("Enter student name: ")
std_id = input("Enter student id: ")
obj1 = Student(name, std_id)

print("Enter student 2 data")
name = input("Enter student name: ")
std_id = input("Enter student id: ")
obj2 = Student(name, std_id)

obj1.display()
obj2.display()