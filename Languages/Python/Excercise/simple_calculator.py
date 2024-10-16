total = 0

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if x > 0 and y > 0:
        return x/y
    else:
        return 'You cannot divide by zero!'
print("1).Add\n2).Substract\n3).Multiply\n4).Divide")
Select = int(input("Please Select Operation (1-4): "))
X = int(input("X: "))
Y = int(input("Y: "))

if Select and Select > 0 and Select < 5:
    if Select == 1:
        print(add(X, Y))
    elif Select == 2:
        print(substract(X, Y))
    elif Select == 3:
        print(divide(X, Y))
    else:
        print(divide(X, Y))
else:
    print("Invaild number!")