#  Mini Project 4: Login & User Validation# Login & User Validation System

# Store users (username: password)
users = {
    "admin": "1234",
    "durkesh": "pass123",
    "john": "abc123"
}

# Login function
def login():
    print("===== Login System =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Validate username
    if username in users:
        # Validate password
        if users[username] == password:
            print("Login Successful ✅\n")
        else:
            print("Incorrect Password ❌\n")
    else:
        print("User not found ❌\n")


# Run program
login()