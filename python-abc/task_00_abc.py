from abc import ABC, abstractmethod

# Définition de la classe abstraite Animal
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Implémentation de la sous-classe Dog
class Dog(Animal):
    def sound(self):
        return "Bark"

# Implémentation de la sous-classe Cat
class Cat(Animal):
    def sound(self):
        return "Meow"
