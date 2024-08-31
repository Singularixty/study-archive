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

print(my_dog.speak())
print(my_cat.speak())