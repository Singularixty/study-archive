def my_decorator(func):
    def wrapper():
        print("This happens before func is called")
        func()
        print("This happens after func is called")
    return wrapper

@my_decorator
def SayHappyBirthday():
    print("Hello World")

SayHappyBirthday()