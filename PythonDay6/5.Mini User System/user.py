class User:
    users_count = 0
    
    def __init__(self):
        self.__user_name = None
        self.__pws = None
        User.users_count += 1
        
# Encapsulation (setter)
    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd
        return self
    
    # Getter
    def get_user(self):
        return self.__user_name
    
    # Method chaining methods
    def login(self):
        print(f"{self.__user_name} logined")
        return self

    def register(self):
        print(f"{self.__user_name} registered")
        return self
    
    # Default greet
    def greet(self):
        print("Welcome User")
        return self
    
    # 🔹 Child Class: Student
class Student(User):
    def greet(self):   # method overriding
        print("Welcome Student")
        return self


# 🔹 Child Class: Faculty
class Faculty(User):
    def greet(self):   # method overriding
        print("Welcome Faculty")
        return self
    
    