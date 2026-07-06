menu = {
    1: ("Pizza", 200),
    2: ("Mo:Mo", 120),
    3: ("Biryani", 150),
    4: ("Cold drinks", 100),
    5: ("Laughing", 80),
    6: ("Veg keema-noodles", 120),
    7: ("Chicken keema-noodles", 140),
    8: ("Buff keema-noodles", 150),
    9: ("Burger", 150)
}

print("........WELCOME TO MERO KHAJA RESTAURANT........")

order_total = 0

while True:
    print("\nMENU:")
    for key, value in menu.items():
        print(f"{key}. {value[0]} : {value[1]}")

    choice = int(input("Enter your item (1-9): "))

    if choice in menu:
        item_name = menu[choice][0]
        item_price = menu[choice][1]

        order_total += item_price
        print(f"{item_name} has been added to your order.")
    else:
        print("Item not available.")

    another_order = input("Do you want to add another item? (yes/no): ").lower()

    if another_order != "yes":
        break

print("Your total amount is:", order_total)