# Task 2: Inheritance (User → Student, Faculty)


# parent class

class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")
        

# Child class 1

class Student(User):
    def student_greet(self):
        print("Hello Student")
        
# Child class 2

class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")
        

# Multilevel Inheritance

class TempFaculty (Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")