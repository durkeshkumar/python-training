# Student Class
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees
        
   # Higher Order Function
def process_users(users, func):
    return list(map(func, users))


# List of Students
students = [
    Student("Durkesh", 101, "ECE", 50000),
    Student("Arun", 102, "CSE", 30000),
    Student("Vijay", 103, "EEE", 60000)
]

# Example 1: Extract names
names = process_users(students, lambda s: s.name)
print(names)

# Example 2: Extract fees
fees = process_users(students, lambda s: s.fees)
print(fees)