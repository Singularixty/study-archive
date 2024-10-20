number = input("Your Number: ")
got_result = False


while got_result != True:
    if not number.isdigit():
        print("Only numbers are allowed!")
        number = input("Your Number: ")
    else:
        got_result = True
        if int(number) % 2 == 0:
            print(f"Number {number} is even")
        else:
            print(f"Number {number} is odd")