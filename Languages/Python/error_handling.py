first_num = input("First Number: ")
sec_num = input("Second Number: ")

try:
    ans = float(first_num) / float(sec_num)
    print(ans)
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("Ended program c:")