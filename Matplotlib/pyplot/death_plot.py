import matplotlib.pyplot as mpl
import csv
import os

with open('./data/jan_death_report.csv','r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    day = []
    deaths = []

    for row in csv_reader:
        day.append(float(row[0]))
        deaths.append(float(row[1]))

    mpl.xlabel('Total Days in January')
    mpl.ylabel('Total Deaths (person)')
    mpl.plot(day, deaths)
    mpl.show()