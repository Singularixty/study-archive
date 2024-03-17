import string
import random
import pyperclip

length = input('Your password length (8-32): ')

if not length.isdigit():
    print('Please insert only a positive number')
else:
    length = int(length)
    if length > 32 or length < 8:
        print('Password length must be between 8 and 32')
    else:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        print(f'Generated Password: {password}')
        copy_prompt = input('Would you like to copy the password (Y/N)?: ').upper()
        if copy_prompt == 'Y':
            pyperclip.copy(password)
            print('Password has been copied to your clipboard, Enjoy :>!')
        else:
            print('Oops!')
