from functools import reduce

# Student Class
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees


# Faculty Class
class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary


# List of Students
students = [
    Student("Durkesh", 101, "ECE", 50000),
    Student("Arun", 102, "CSE", 30000),
    Student("Vijay", 103, "EEE", 60000)
]

# Total Fees using reduce
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

print("Total Fees:", total_fees)


# List of Faculty
faculty_list = [
    Faculty("Ravi", 201, 60000),
    Faculty("Kumar", 202, 25000),
    Faculty("Suresh", 203, 55000)
]

# Total Salary using reduce
total_salary = reduce(lambda acc, f: acc + f.salary, faculty_list, 0)

print("Total Salary:", total_salary)