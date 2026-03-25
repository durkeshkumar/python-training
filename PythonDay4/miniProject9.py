# Mini Project 9: Course Enrollment System

# Store students and their courses
students = []

# 1. Add Student
def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma separated): ").split(",")

    student = {
        "name": name,
        "courses": [course.strip() for course in courses]
    }

    students.append(student)
    print(f"\n{name} added successfully!")

# 2. Update Courses
def update_courses():
    name = input("Enter student name to update: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Current courses:", student["courses"])
            new_courses = input("Enter new courses (comma separated): ").split(",")
            student["courses"] = [course.strip() for course in new_courses]
            print("Courses updated successfully!")
            return

    print("Student not found!")

# 3. Display Student Details
def display_students():
    if not students:
        print("\nNo students found!")
        return

    print("\n--- Student Details ---")
    for student in students:
        print(f"Name: {student['name']}")
        print("Courses:", ", ".join(student["courses"]))
        print("-" * 30)

# Menu system
def menu():
    while True:
        print("\n--- Course Enrollment Menu ---")
        print("1. Add Student")
        print("2. Update Courses")
        print("3. Display Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_courses()
        elif choice == '3':
            display_students()
        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

# Run program
menu()