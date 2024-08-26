# Library/Built-in > enclosed > global > local
def my_function():
    x = 10
    print(x)

def globalf():
    global x
    x = 20
    print(x)

my_function()
globalf()

def outer_function():
    y = 10

    def inner_function():
        nonlocal y
        y = 20  
        print(y)

    inner_function() 
    print(y) 

outer_function()