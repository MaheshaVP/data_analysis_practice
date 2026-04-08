#polymorphism

class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def Sound(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def Sound(self):
        print(f"{self.name} meows")

dog = Dog("Rookie")
cat = Cat("Pillu")

for breed in (dog,cat):
    print(breed.name)
    breed.Sound()
