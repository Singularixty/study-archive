import matplotlib.pyplot as mpl
import csv
import os

with open('./data/jan_temp.csv','r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    day = []
    temp = []
    print(day)
    print(temp)

    for row in csv_reader:
        day.append(float(row[0]))
        temp.append(float(row[1]))

    mpl.xlabel('Total Days in January')
    mpl.ylabel('Temperature (C)')
    mpl.plot(day, temp)
    mpl.show()