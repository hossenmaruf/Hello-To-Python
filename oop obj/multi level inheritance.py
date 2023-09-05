class Organism:
    alive = True

class Animal(Organism):

    def eat(self):
         print("animal are eating")

class Dog(Animal):
    def bark(self):
     print("this dog are barking")


dog = Dog()
print(dog.alive)