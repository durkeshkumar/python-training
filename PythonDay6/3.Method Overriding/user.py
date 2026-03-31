# Task 3: Method Overriding

# Parent
class User:
    def greet(self):
        print("Welcome User")

# class1

class student(User):
    def greet(self):
        print("Welcome Student")
        
# class2

class Faculty(User):
    def greet(self):
        print("Welcome Faculty")