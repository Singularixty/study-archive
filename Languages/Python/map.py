prices = [10, 20, 30, 40, 50]

discount = map(lambda x: x / 2, prices)
listed_discount = list(discount)

for i in listed_discount:
    print(f"Sale 50% off -> {i}$")