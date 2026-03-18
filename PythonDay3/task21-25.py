# Section 4: String Basics (21–25)

# 21

text = input("Enter a string: ")
count = 0

for ch in text:
    count += 1

print("Total characters:", count)


# 22

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)


# 23

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch.isalpha() and ch not in vowels:
        count += 1

print("Consonant count:", count)

# 24

text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)

# 25

text = input("Enter to find palindrom")
reverse = ""

for ch in text:
    reverse = ch + reverse
        
    if text == reverse:
        print("Palindrome")
    else:
        print("Not a Palindrome")
