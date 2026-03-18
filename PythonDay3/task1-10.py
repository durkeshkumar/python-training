# Section 1: Loop Basics (1–10)

# 1
for i in range(1,51):
  print(i)
  
# 2

for i in range(2,101,2):
    print(i)

# 3

for i in range(1,101,2):
    print(i)
    
# 4

for i in range(1,11):
    print(f"7 x {i} = {7 * i}")
    
# 5
total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

# 6

for i in range(50,1,-1):
    print(i)

# 7

count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Count:", count)

# 8

for i in range(1,11):
    print(i**2)
    
# 9

for i in range(1,11):
    print(i**3)
    
# 10

n = int(input("Enter a number :-"))
for i in range(1,n+1):
 print(i)

