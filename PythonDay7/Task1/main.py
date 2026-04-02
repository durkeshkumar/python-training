from super import Student,Faculty,TempFaculty

s1 = Student("Durkesh", 101, "ECE", 50000)
f1 = Faculty("Ravi", 201, 60000)
t1 = TempFaculty("Kumar", 301, 30000, "6 months")

print(s1.name, s1.dept)
print(f1.name, f1.salary)
print(t1.name, t1.duration)