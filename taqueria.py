MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0.0
while True:
    try:
        item = input("Enter an item: ")
    except EOFError:
        break  # user pressed control-d
    item = item.strip().title()
    if item in MENU:
        price = MENU[item]
        total_cost += price
        print(f"${total_cost:.2f}")
    else:
        print("Invalid item")
