# Task 4: Method Chaining

class User():
    
    def register(self):
        print("Registered")
        return self
    
    def login(self):
        print("logined")
        return self
    
    
    def greet(self):
        print("enjoy everyone")
        return self
    
user = User()
user.login().greet().register()

    