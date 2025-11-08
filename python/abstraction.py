# lecture 5--> Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    def action(self):
        pass

class Lion(Animal):
    def action(self):
        print("Roar")

class Dog(Animal):
    def action(self):
        print("Bark")
class Cat(Animal):
    def action(self):
        print("Meow")

obj = Lion()
obj.action()
obj = Dog()
obj.action()
obj = Cat()
obj.action()