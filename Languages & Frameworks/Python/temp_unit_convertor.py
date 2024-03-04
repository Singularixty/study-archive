your_unit = input('Is your temperature unit (C/F): ')
temp_num = float(input('Your temperature number: '))

if your_unit.upper() == 'C':
    converted_temp = (temp_num * 9/5) + 32
    print(f'Converted from Celsius to Fahrenheit: {converted_temp:.2f} °F')
elif your_unit.upper() == 'F':
    converted_temp = (temp_num - 32) * 5/9
    print(f'Converted from Fahrenheit to Celsius: {converted_temp:.2f} °C')
else:
    print('Invalid input. Please enter either "C" for Celsius or "F" for Fahrenheit.')
