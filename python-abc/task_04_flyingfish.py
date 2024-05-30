class Fish:
    def swim(self):
        print("The fish is swimming")
    
    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")
    
    def fly(self):
        print("The flying fish is soaring!")
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")

if __name__ == "__main__":
    poisson_volant = FlyingFish()
    
    poisson_volant.swim()
    poisson_volant.fly()
    poisson_volant.habitat()
    
    # Imprimer l'ordre de résolution des méthodes
    print(FlyingFish.mro())
