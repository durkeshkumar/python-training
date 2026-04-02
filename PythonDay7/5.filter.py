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

# Filter students with fees > 50000
high_fee_students = list(filter(lambda s: s.fees > 50000, students))

print([(s.name, s.fees) for s in high_fee_students])


# List of Faculty
faculty_list = [
    Faculty("Ravi", 201, 60000),
    Faculty("Kumar", 202, 25000),
    Faculty("Suresh", 203, 55000)
]

# Filter faculty with salary > 30000
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty_list))

print([(f.name, f.salary) for f in high_salary_faculty])