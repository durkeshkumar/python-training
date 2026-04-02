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
    Student("Vijay", 103, "EEE", 40000)
]

# Sort Students by Fees
students.sort(key=lambda x: x.fees)

print("Sorted Students (by fees):")

for s in students:
    print(s.name,s.fees)



# List of Faculty
faculty_list = [
    Faculty("Ravi", 201, 60000),
    Faculty("Kumar", 202, 45000),
    Faculty("Suresh", 203, 55000)
]

# Sort Faculty by Salary
faculty_list.sort(key=lambda x: x.salary)

print("\nSorted Faculty (by salary):")

for f in faculty_list: 
    print(f.name, f.salary)
