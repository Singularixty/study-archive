class Cat:
    def __init__(self, name, color):
        self.name = name # instance_attribute
        self.color = color

    def meow(self): # method
        print(f"{self.name} meow!")

# object
my_cat = Cat("Som", "Brown")
my_cat.meow()