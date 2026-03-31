from user import User,Student,Faculty

s1 = Student()
s1.set_user("john", "1234").login().greet().register()

print("-----")

f1 = Faculty()
f1.set_user("david", "5678").login().greet().register()
f1.set_user("kumar", "9876").login().greet().register()

print("-----")

# total users created
print("Total Users:", User.users_count)