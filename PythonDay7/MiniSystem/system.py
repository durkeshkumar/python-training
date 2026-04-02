from abc import ABC, abstractmethod
from functools import reduce

# Abstract Base Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass
    
    #  Parent Class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


#  Student Class
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"
#  Faculty Class
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"
    
    
students = [
    Student("Durkesh", 101, "ECE", 50000),
    Student("Arun", 102, "CSE", 30000),
    Student("Vijay", 103, "EEE", 60000)
]

faculty_list = [
    Faculty("Ravi", 201, 60000),
    Faculty("Kumar", 202, 25000),
    Faculty("Suresh", 203, 55000)
]

# 1.All details (get_details())

print("All Student Details:")
print(list(map(lambda s: s.get_details(), students)))

print("\nAll Faculty Details:")
print(list(map(lambda f: f.get_details(), faculty_list)))

# 2.Sorted data

students.sort(key=lambda s: s.fees)

print("\nSorted Students (by fees):")
print(list(map(lambda s: (s.name, s.fees), students)))

faculty_list.sort(key=lambda f: f.salary)
print("\nSorted Faculty (by salary):")
print(list(map(lambda f: (f.name, f.salary), faculty_list)))

# 3.Filtered data

high_fee_students = list(filter(lambda s: s.fees > 40000, students))

print("\nHigh Fee Students:")
print(list(map(lambda s: (s.name, s.fees), high_fee_students)))

high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty_list))

print("\nHigh Salary Faculty:")
print(list(map(lambda f: (f.name, f.salary), high_salary_faculty)))


# 4. Total fees & salary

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty_list, 0)

print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)