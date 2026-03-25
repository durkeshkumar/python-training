# Mini Project 2: Student Report Card


def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


def student_report():
    print("===== Student Report Card =====")

    name = input("Enter student name: ")

    #  marks
    
    sub1 = float(input("Enter marks for Subject 1: "))
    sub2 = float(input("Enter marks for Subject 2: "))
    sub3 = float(input("Enter marks for Subject 3: "))

    # Store in dictionary
    student = {
        "name": name,
        "marks": [sub1, sub2, sub3]
    }

    # Calculate total and average
    
    total = sum(student["marks"])
    average = total / 3

    grade = calculate_grade(average)

    # Print formatted report
    
    print("\n===== Report Card =====")
    print(f"Name     : {student['name']}")
    print(f"Marks    : {student['marks']}")
    print(f"Total    : {total}")
    print(f"Average  : {average:.2f}")
    print(f"Grade    : {grade}")
    print("========================")


# Run program
student_report()