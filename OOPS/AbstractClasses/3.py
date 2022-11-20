from abc import ABCMeta, ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def show(self):
        None

    @abstractmethod
    def info(self):
        None

class Child(Parent):
    def show(self):
        print("In show")

    def info(self):
        print("In info")


class Xyz:
    pass

# obj = Child()
# obj.show()
# obj.info()

print(type(Parent))         # <class 'abc.ABCMeta'>
print(type(Child))          # <class 'abc.ABCMeta'>
print(type(Xyz))            # <class 'type'>

