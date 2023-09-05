class Animal:

    alive = True


    def eat(self):
        print("this is animal eating")
    def slumber(self):
        print("aminaal is sleeping")

class Rabbit(Animal):


    def run(self):
        print("this rabbit can run")

class Fish(Animal):
    pass
class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()


print(rabbit.alive)
rabbit.run()