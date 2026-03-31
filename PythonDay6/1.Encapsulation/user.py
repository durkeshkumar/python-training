# Task 1: Encapsulation (User Class)class User:

class User:
    def __init__(self):
        self.__user_name = None   
        self.__pwd = None         

    # Setter
    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    # Getter
    def get_user(self):
        return self.__user_name

    # Register
    def register(self):
        print(f"Registering user: {self.__user_name}")

    # Login 
    def login(self):
        print(f"Logging in: {self.__user_name}")

