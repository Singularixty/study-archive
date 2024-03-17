import csv

Fruit_list = ['Banana', 'Orange', 'Apple', 'Papaya', 'Avocado']
sorted_fruit = sorted(Fruit_list)
print(sorted_fruit)

temp_hum_list = []

with open('./bin/practice_data_1.csv', 'r') as csvFile:
    file_content = csv.reader(csvFile)
    next(file_content)
    for row in file_content:
        temp_hum_list.append(row)

get_temp = lambda temp: float(temp[1])

sorted_by_temp = sorted(temp_hum_list, key=get_temp, reverse=True)

print(f'Sorted: {sorted_by_temp}')
for i in sorted_by_temp:
    print(f'Day #{i[0]} {i[1]}C {i[2]}%')

