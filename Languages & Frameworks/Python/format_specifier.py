year_1 = 1294192589
year_2 = -2189563634912894
year_3 = 69253253295818418

table = [year_1, year_2, year_3]

for i in range(0, 3):
    print('Year :',[i], table[i].__format__('> ,.2f'))