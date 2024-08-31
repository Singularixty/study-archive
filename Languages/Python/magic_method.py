from typing import Any


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"-------------------\n[Person Info]\nName: {self.name}\nAge: {self.age} years old\n-------------------"

Person_1 = Person("Alice", 20)
print(Person_1)
Person_2 = Person("Alex", 30)
print(Person_2)

print("\n\n\n\n")

people = [Person("Alice", 20), Person("Alex", 30), Person("Johnson", 50)]

for person in people:
    print(person)


class Greet():
    def __call__(self, name):
        return f"Hello {name}"
    
greet = Greet()

print(greet("Alex"))
print(greet("Johnson"))