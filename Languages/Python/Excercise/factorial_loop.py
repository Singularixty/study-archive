number = input("Enter non-negative integer: ")

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers!")
    result = 1
    for i in range(1, n+1):
        result *= i
    return f"The answer of {n}! is {result:,}"
    
if not number.isdigit():
    print("Only numbers are allowed!")
else:
    print(factorial(int(number)))