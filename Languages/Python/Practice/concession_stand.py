menu = {
    'pizza': 3.00,
    'hamburger': 12.00,
    'fries': 2.60
}

cart = []
checkout = 0
food = input('What would you like to eat? (Type "q" or "quit" to exit): ').lower()

while food != 'q' and food != 'quit':
    if food not in menu:
        print('Sorry! We don\'t sell that here')
    else:
        cart.append(food)
    food = input('What would you like to eat? (Type "q" or "quit" to exit): ').lower()

print("Items in your cart:")

for item in cart:
    price = menu[item]
    checkout += price
    print(f"{item}: ${price:.2f}")

print(f"Total: ${checkout:.2f}")
