# Section 7: List Operations (36–40)

# 36
nums =[10,20,30]
nums.append(40)
nums.append(50)
nums.append(60)
print(nums)

# 37

nums = ["chennai","Madurai","Tirunelveli","Salem","Nagercoil"]
nums.insert(2,"India")
print(nums)

# 38

nums = ["chennai","Madurai","Tirunelveli","Salem","Nagercoil"]
nums.remove("Nagercoil")
print(nums)

# 39
nums = ["chennai","Madurai","Tirunelveli","Salem","Nagercoil"]

reversed_list = []

for i in range(len(nums)-1, -1, -1):
    reversed_list.append(nums[i])

print(reversed_list)

# 40

nums = [40, 10, 30, 20]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums)