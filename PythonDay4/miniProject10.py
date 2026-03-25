# Mini Project 10: Number Utility Tool

# 1. Convert Number
def convert_number(num):
    print("\n--- Number Conversions ---")
    print(f"Binary      : {bin(num)}")
    print(f"Octal       : {oct(num)}")
    print(f"Hexadecimal : {hex(num)}")

# 2. Format Number with Commas
def format_number(num):
    print("\n--- Formatted Number ---")
    print(f"With commas : {num:,}")

# 3. Scientific Notation
def scientific_notation(num):
    print("\n--- Scientific Notation ---")
    print(f"Scientific  : {num:.2e}")

# Menu system
def menu():
    while True:
        print("\n--- Number Utility Menu ---")
        print("1. Convert Number (Binary/Octal/Hex)")
        print("2. Format with Commas")
        print("3. Scientific Notation")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3']:
            try:
                num = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input! Enter a valid number.")
                continue

            if choice == '1':
                # Conversion works best with integers
                convert_number(int(num))
            elif choice == '2':
                format_number(num)
            elif choice == '3':
                scientific_notation(num)

        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

# Run program
menu()