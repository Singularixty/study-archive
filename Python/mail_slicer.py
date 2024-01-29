your_email = input('Please enter your mail: ')

if '@' not in your_email:
    print('Please insert a valid email address!')
else:
    find_at = your_email.index('@')
    username = your_email[:find_at]
    domain = your_email[find_at+1:]
    print(f'Hello {username}! your domain is {domain}')
