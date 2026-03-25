# Mini Project 7: Bank Account System

# Store account details
account = {}

# 1. Create Account
def create_account():
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))
    
    account["name"] = name
    account["balance"] = balance
    
    print(f"\nAccount created successfully for {name}!")

# 2. Deposit Money
def deposit():
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        account["balance"] += amount
        print(f"₹{amount} deposited successfully!")
    else:
        print("Invalid amount!")

# 3. Withdraw Money
def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"₹{amount} withdrawn successfully!")
    else:
        print("Insufficient balance!")

# 4. Check Balance
def check_balance():
    print(f"Current Balance: ₹{account['balance']}")

# Menu system
def menu():
    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            if account:
                deposit()
            else:
                print("Please create an account first!")
        elif choice == '3':
            if account:
                withdraw()
            else:
                print("Please create an account first!")
        elif choice == '4':
            if account:
                check_balance()
            else:
                print("Please create an account first!")
        elif choice == '5':
            print("Thank you for using Bank System!")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
menu()