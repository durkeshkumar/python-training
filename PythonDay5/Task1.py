# Task 1: User Info Manager (Functions + Dictionary)

def create_user(name, age, role):
    user = {
        "name" : name.title(),
        "age" : age,
        "role" : role,
    }
    return user

users = []

users.append(create_user("durkesh",28,"Developer"))
users.append(create_user("priya",26,"Tester"))
users.append(create_user("kumar",27,"Analyst"))

for user in users:
    print(user)
