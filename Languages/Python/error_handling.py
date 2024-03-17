try:
    first_number = int(input('First Number: '))
    second_number = int(input('Second Number: '))
    if first_number < second_number:
        raise Exception('first num cannot be lesser than second num')
    division = first_number / second_number
    print(division)
except ZeroDivisionError as e:
    print('The numbers you provided cannot divide by zero!')
except Exception as e:
    print(e)
finally:
    print('Thank you for using :)!')
