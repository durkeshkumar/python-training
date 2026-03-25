# Mini Project 3: Shopping Cart System


cart = []

# Add Product
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(product)
    print("Product added to cart!\n")


# Display Cart
def display_cart():
    if not cart:
        print("Cart is empty\n")
        return

    print("\n===== Cart Items =====")
    for i, item in enumerate(cart):
        total_price = item["price"] * item["quantity"]
        print(f"{i+1}. {item['name']} | Price: {item['price']} | Qty: {item['quantity']} | Total: {total_price}")
    print()


# Calculate Total Bill
def calculate_total():
    total_bill = 0
    for item in cart:
        total_bill += item["price"] * item["quantity"]

    print(f"\nTotal Bill: {total_bill}\n")


# Remove Product
def remove_product():
    display_cart()
    index = int(input("Enter item number to remove: ")) - 1

    if 0 <= index < len(cart):
        removed = cart.pop(index)
        print(f"{removed['name']} removed from cart!\n")
    else:
        print("Invalid item number\n")


# Menu
def menu():
    while True:
        print("===== Shopping Cart Menu =====")
        print("1. Add Product")
        print("2. View Cart")
        print("3. Remove Product")
        print("4. Calculate Total Bill")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_cart()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")


# Run program
menu()