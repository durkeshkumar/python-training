# Task 7: File Handling

# 1
file = open("team_data.txt", "w")

file.write("Name: Durkesh, Role: Developer\n")
file.write("Name: Priya, Role: Tester\n")
file.write("Name: Kumar, Role: Analyst\n")

print("Is file closed after writing?", file.closed)

file.close()

print("Is file closed now?", file.closed)


# 2
file = open("team_data.txt", "r")

content = file.read()
print("\nFile Content:\n")
print(content)

file.close()