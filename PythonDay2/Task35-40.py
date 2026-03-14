# 35

age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:

            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")
    
    # 36
    
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Age not eligible")
else:
    print("Marks not eligible")

# 37

age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected for sports")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")
    
  # 38
  
day = int(input("Enter number (1-7): "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    
#  39

num = int(input("Enter number (1-3): "))

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
        
# 40

num = int(input("Enter number (1-4): "))

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
        