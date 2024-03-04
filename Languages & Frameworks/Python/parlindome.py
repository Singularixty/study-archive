def palindrome(number):
    print("original number", number)
    original_num = number
    
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    if original_num == reverse_num:
        print(f"A number {original_num} is palindrome")
    else:
        print(f"A number {original_num} is not palindrome")

palindrome(121)
palindrome(125)