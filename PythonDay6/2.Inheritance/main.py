from user import Student,Faculty,TempFaculty

# objects

s1 = Student()
f1 = Faculty()
t1 = TempFaculty()


print("----Student----")

s1.register()
s1.login()
s1.student_greet()

print("----Faculty----")

f1.register()
f1.login()
f1.faculty_greet()


print("----Temp Faculty----")

t1.register()
t1.login()
t1.faculty_greet()
t1.tempFaculty_greet()