store = [('Nike x Adidas Shoes', 1200),
         ('Luxury Tiger Shirt', 14999),
         ('Louis Vuitton Bag', 102859),
         ('CELINE Bag', 61000)]

convert_to_yen = lambda store: (store[0], f'{float(store[1]*4.10):,.2f}¥')

yen_store = (map(convert_to_yen, store))
print(type(yen_store))
yen_store_list = list(yen_store)
print(type(yen_store_list))
for item in yen_store_list:
    print(f'Selling {item[0]} for {item[1]}')