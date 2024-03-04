import csv
import math

target = './bin/practice_data_1.csv'
with open(target, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    temperature_list = []
    humidity_list = []
    for row in csv_reader:
        temperature_list.append(float(row[0]))
        humidity_list.append(float(row[1]))

    highest_temperature = max(temperature_list)
    highest_temperature_index = temperature_list.index(highest_temperature) + 1 
    highest_humidity_percentage = max(humidity_list)
    highest_humidity_percentage_index = humidity_list.index(highest_humidity_percentage) + 1 

    print('Summary: 30 Days of Temp/Hum Record')
    print(f'Highest Temperature (°C) Record is Day #{highest_temperature_index}: {highest_temperature:.2f}°C')
    print(f'Highest Humidity (%) Record is Day #{highest_humidity_percentage_index}: {highest_humidity_percentage:.2f}%')
