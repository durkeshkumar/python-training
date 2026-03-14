#Input & Type Casting Tasks

# 15

name = input("Enter your name:")
print((type)(name))

#o/p:- 
# Enter your name:durkesh
# <class 'str'>

# 16
Age = int(input("Enter your Age:"))

print(Age)
print(type(Age))

#o/p:- 
# Enter your Age:21
# 21
# <class 'int'>

# 17

num1 = int(input("Enter Num1:"))
num2 = int(input("Enter Num2:"))

print("Sum:",num1 + num2)

#o/p:- 
# Enter Num1:2
# Enter Num2:5
# Sum: 7

# 18

num1 = int(input("Enter Num1:"))
num2 = int(input("Enter Num2:"))

print("Avg:",(num1 + num2) / 2)

#o/p:- 
# Enter Num1:15
# Enter Num2:4
# Avg: 9.5

# 19

a = int(input("Enter Num1:"))
b = int(input("Enter Num2:"))

Result = 3*a*2 + b - 2

print(Result)

#o/p:- 
# Enter Num1:2
# Enter Num2:4
# 14


# 20

num = input("Enter a number: ")
print("Before casting:", type(num))

num = int(num)
print("After casting:", type(num))

#o/p:-

# Enter a number: 15
# Before casting: <class 'str'>
# After casting: <class 'int'> 