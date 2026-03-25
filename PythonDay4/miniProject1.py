# Employee Management System

employees = []

# Add Employee
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))

    emp = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }

    employees.append(emp)
    print("Employee added successfully!\n")


# Display Employees
def display_employees():
    if not employees:
        print("No employees found\n")
        return

    print("\n--- Employee List ---")
    for i, emp in enumerate(employees):
        print(f"{i+1}. Name: {emp['name']}, Age: {emp['age']}, Role: {emp['role']}, Salary: {emp['salary']}")
    print()


# Update Employee
def update_employee():
    display_employees()
    index = int(input("Enter employee number to update: ")) - 1

    if 0 <= index < len(employees):
        print("Enter new details:")
        employees[index]["name"] = input("Name: ")
        employees[index]["age"] = int(input("Age: "))
        employees[index]["role"] = input("Role: ")
        employees[index]["salary"] = float(input("Salary: "))
        print("Employee updated!\n")
    else:
        print("Invalid employee number\n")


# Delete Employee
def delete_employee():
    display_employees()
    index = int(input("Enter employee number to delete: ")) - 1

    if 0 <= index < len(employees):
        employees.pop(index)
        print("Employee deleted!\n")
    else:
        print("Invalid employee number\n")


# Menu
def menu():
    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice\n")

menu()