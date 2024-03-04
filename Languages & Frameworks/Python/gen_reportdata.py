import csv
import random

amount = 365
name = 'practice_data_2023'
data = []
for i in range(amount):
    day = i+1
    temperature = round(random.uniform(-20, 40), 2)
    humidity = round(random.uniform(20, 80), 2)
    wind = round(random.uniform(1, 30), 2)
    data.append([day, temperature, humidity, wind])

csv_filename = f'./bin/{name}.csv'
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Day (#)','Temperature (C)', 'Humidity (%)', 'Wind (Km/h)'])
    csv_writer.writerows(data)

print(f'{len(data)} sets of data have been written to {csv_filename} -> @/root/bin/{name}.csv')
