import csv
import random

amount = 356
name = 'finance_data'
data = []
balance = 0  

for _ in range(amount):
    income = round(random.uniform(500, 1500), 2) 
    expense = round(random.uniform(100, 800), 2)  
    balance += income - expense

    data.append([income, expense, balance])

csv_filename = f'./bin/{name}.csv'
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Income ($)', 'Expense ($)', 'Balance ($)'])
    csv_writer.writerows(data)

print(f'{amount} days of financial data have been written to {csv_filename} -> @/root/bin/{name}.csv')
