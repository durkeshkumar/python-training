#  Section 3: Nested Loop (16–20)

# 16

for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
     
    #  for i in range(1, 5):
    #   print("*" * i)
    
# 17

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    
# 18

for i in range(1, 6): 
    print(f"\nTable of {i}")
    for j in range(1, 11):
        print(f" {j} x {i} = {i*j}")
        
# 19

for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()
    
# 20

num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()