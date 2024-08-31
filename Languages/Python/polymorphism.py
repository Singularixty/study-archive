class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
    
my_dog = Dog("Buddy")
my_cat = Cat("Puppy")

animals = [Dog("Buddy"), Cat("Puppy"), Cat("Som")]

for x in animals:
    print(x.speak())