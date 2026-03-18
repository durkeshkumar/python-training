# Section 2: While Loop (11–15)

# 11
i = 1
while i <=20:
    print(i)
    i+=1
  
# 12

n = int(input("Enter a number:-"))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("Factorial:", fact)

# 13

num = int(input("Enter number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

    print("Reversed number:", reverse)
    
# 14

num = int(input("Enter number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits:", count)

    
# 15

while True:
    user_input = input("Enter something (type 'stop' to end): ")
    
    if user_input.lower() == "stop":
        break
    
    print("You entered:", user_input)



