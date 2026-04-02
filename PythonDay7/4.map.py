# Student Class
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees


# List of Students
students = [
    Student("Durkesh", 101, "ECE", 50000),
    Student("Kumar", 102, "CSE", 30000),
    Student("Vijay", 103, "EEE", 40000)
]

# Using map to extract only names
names = list(map(lambda s: s.name, students))

print(names)