# Task 6: Exception Handling Module

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    if denominator == 0:
        print("Error: Cannot divide by zero")
    else:
        result = numerator / denominator
        print("Result:", result)

except ValueError:
    print("Error: Invalid input")

finally:
    print("Program Completed")