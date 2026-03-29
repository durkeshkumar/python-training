# Task 4: Factorial Service (Recursion)

def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    if n == 0:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))
print(factorial(0))
print(factorial(-3))