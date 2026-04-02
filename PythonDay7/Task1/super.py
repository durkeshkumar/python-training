# Task 1: Use super() properly


# Parent class

class User:
    def __init__(self,name,id):
        self.name =  name
        self.id = id
        
# child class : Student
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

# Child Class: Faculty
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
        
# Child Class: TempFaculty (inherits from Faculty)
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration