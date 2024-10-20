number = input("Enter non-negative integer: ")

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers!")
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)
    
if not number.isdigit():
    print("Only numbers are allowed!")
else:
    print(f"Factorial of {number}! is {factorial(int(number)):,}")