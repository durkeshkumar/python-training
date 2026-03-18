# Section 6: List Basics (31–35)

# 31

nums = [10, 20, 30, 40, 50]

total = 0
for n in nums:
    total += n

print("Sum:", total)

# 32

nums = [10, 25, 5, 60, 15]

max_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n

print("Maximum:", max_val)

# 33

nums = [10, 25, 5, 60, 15]

min_val = nums[0]

for n in nums:
    if n < max_val:
        max_val = n

print("Maximum:", max_val)

# 34
nums = [10, 20, 30, 40, 50]

count = 0
for n in nums:
    count += 1
    
print("Total Elements:", count)

# 35

nums = [10, 20, 30, 40, 50]

x = int(input("Enter number to find"))

found = False

for n in nums:
    if n ==x:
        found = True
        break
if found:
    print("Element found")
else:
    print("Not found")

