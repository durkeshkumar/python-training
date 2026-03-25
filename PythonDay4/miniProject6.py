# Mini Project 6: String Formatter Tool

def string_formatter():
    # Input
    name = input("Enter your name: ")
    product = input("Enter product name: ")

    # 1. Basic formatted sentence
    sentence = f"Hello {name}, thank you for purchasing {product}!"
    print("\nFormatted Sentence:")
    print(sentence)

    # 2. Padding examples
    print("\n--- Padding Output ---")

    # Left align
    print("Left Align :")
    print(name.ljust(20, '*'))

    # Right align
    print("Right Align :")
    print(name.rjust(20, '*'))

    # Center align
    print("Center Align :")
    print(name.center(20, '*'))


# Run the program
string_formatter()