from abstraction import  Student,Faculty,TempFaculty



s = Student("Durkesh", 101, "ECE", 50000)

f = Faculty ("Kumar",101,75000)

t = TempFaculty("Priya", 301, 30000, "6 months")

print(s.get_details())
print(f.get_details())
print(t.get_details())
