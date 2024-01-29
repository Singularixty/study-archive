import csv
import json
import random
import os
from datetime import datetime

# variables
PathOption = None
File_Name = None
File_Path = None
File_PathMode = None
illegal_start_characters = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']

# Retrieve Current Time
def GetCurrentTime():
    current_time = datetime.now()
    return str(current_time)

# Declare File_Name
while True: 
    FileName = input("Please specify a file name: ")
    if any(FileName.startswith(char) for char in illegal_start_characters):
        print("Invalid file name, Please specify a new data name!")
    else:
        File_Name = FileName
        break

print(f"&Name -> {File_Name}")

# Declare File_Path
while True:
    CustomPathOption = input("Do you want to specify a custom file path? (Y/N): ").lower()
    if CustomPathOption == 'yes' or CustomPathOption == 'y':
        CustomPath = input('Please specify a custom path: ')
        if os.path.exists(CustomPath) and os.path.isdir(CustomPath):
            if os.access(CustomPath, os.W_OK):
                File_PathMode = 'custom'
                break
            else:
                print("Insufficient privileges. Please specify a different directory.")
        else:
            print("Invalid custom path. Please specify a valid existing directory.")
    elif CustomPathOption == 'no' or CustomPathOption == 'n':
        File_PathMode = 'self'
        break

# PathMode.Check
if File_PathMode == 'custom':
    File_Path = os.path.join(CustomPath, f'{File_Name}.csv')
else:
    File_Path = os.path.join(os.getcwd(), f'{File_Name}.csv')

print(F"&FilePath -> {File_Path}")

# Generate File
Row_Count = 0
Column_Count = 0
RowName_Buffer = []
DataPattern_Buffer = []
FileData_Buffer = []

# specify total rows
while True:
    RowCount = input("Numbers of Rows: ")
    if RowCount.isdigit():
        Row_Count = int(RowCount)

        # specify each row a name
        for row in range(1, Row_Count + 1):
            RowName = input(f"Please specify a row #{row}'s name: ")
            RowName_Buffer.append(RowName)
        break
    else:
        print('Please specify a valid number of rows (0, 10, 100, etc.)')
print(F"&RowCount -> {Row_Count}")

# specify total columns
while True:
    ColumnCount = input("Please specify numbers of Data (columns): ")
    if ColumnCount.isdigit():
        Column_Count = int(ColumnCount)
        break
    else:
        print('Please specify a valid number of columns (0, 10, 100, etc.)')
print(F"&ColumnCount -> {Column_Count}")

# Declare column generate data's pattern
for rowNum in range(len(RowName_Buffer)):
    while True:
        os.system('cls')
        print("---- [Data Pattern] ----")
        print('1). Ordered Whole Integer (1, 2, 3, 4, 5, ...)')
        print('2). Random Whole Integer (3, 12, 4, 5, ....)')
        print('3). Floating Number (3.12, 3.4, 5.63, ...)')
        print('4). Fixed Data (symbols, special characters, ...)')
        DataPatternInput = input(f"Please specify a data pattern of row #{RowName_Buffer[rowNum]}: ")
        if DataPatternInput == '1':
            DataPattern_Buffer.append('ordered_whole_integer')
            break
        elif DataPatternInput == '2':
            StartNum = int(input('Start Number: '))
            EndNum = int(input('End Number: '))
            DataPattern_Buffer.append(f'random_whole_integer_start_{StartNum}_end_{EndNum}')
            break
        elif DataPatternInput == '3':
            DigitCount = int(input('Number of Digits: '))
            lower_bound = float(input(f'Lower bound for floating number: '))
            upper_bound = float(input(f'Upper bound for floating number: '))
            DataPattern_Buffer.append(f'floating_number_{DigitCount}_{lower_bound}_{upper_bound}')
            break
        elif DataPatternInput == '4':
            CustomDataPatternInput = input(f"Please specify a custom data pattern of row #{RowName_Buffer[rowNum]}: ")
            DataPattern_Buffer.append(f'fixed_data:{CustomDataPatternInput}')
            break
        else:
            print('Incorrect format, Please specify a number (1-4)')

print(f"Data Pattern: {DataPattern_Buffer}")

# Generate data
for i in range(Column_Count):
    column_data = []
    for j in range(Row_Count):
        pattern = DataPattern_Buffer[j]
        if pattern == 'ordered_whole_integer':
            column_data.append(i + 1) 
        elif pattern.startswith('random_whole_integer'):
            StartNum = int(pattern.split('_')[4])
            EndNum = int(pattern.split('_')[6])
            column_data.append(random.randint(StartNum, EndNum)) 
        elif pattern.startswith('floating_number'):
            DigitCount = int(pattern.split('_')[2])
            lower_bound = float(pattern.split('_')[3])
            upper_bound = float(pattern.split('_')[4])
            column_data.append(round(random.uniform(lower_bound, upper_bound), DigitCount))
        elif pattern.startswith('fixed_data'):
            fixed_data_value = pattern.split(':')[1]
            column_data.append(fixed_data_value)
        else:
            column_data.append('-')

    FileData_Buffer.append(column_data)

# Write {File_Name}.csv
with open(File_Path, mode='w', newline='') as NewFile:
    csv_writer = csv.writer(NewFile)
    csv_writer.writerow(RowName_Buffer)
    csv_writer.writerows(FileData_Buffer)

# Get current time, path, and file size
current_time = GetCurrentTime()
file_size = os.path.getsize(File_Path)
file_size_mb = file_size / 1024

os.system('cls')
print("----- [REPORT] -----")
print(f"FileName: {File_Name}.csv")
print(f"FileCreatedAt: {current_time} ")
print(f"FilePath: {File_Path}")
print(f"FileSize: {file_size:,} bytes ({file_size_mb:.2f}MB)")