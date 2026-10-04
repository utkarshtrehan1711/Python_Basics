class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

emp=Person("Utkarsh", 18)
print(emp.getName())
print(emp.getAge())
print(emp.isEmployee())

emp1=Employee("Utkarsh Trehan", 28)
print(emp1.getName())
print(emp1.getAge())
print(emp1.isEmployee())

