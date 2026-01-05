class Mammal:
    def move(self):
        print("Walk")

class Dog(Mammal):
    def bark(self):
        print("Woof")

class Cat(Mammal):
    def meow(self):
        print("Meow")

kitty = Cat()
kitty.meow()

bosco = Dog()
bosco.bark()