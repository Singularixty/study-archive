import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('./example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

with open('./example.csv', newline='') as CSVFile:
    Reader = csv.reader(CSVFile)
    for row in Reader:
        print(row)