#method overriding

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

#method overloading

class Math:
    def add(self,a,b=0,c=0):
        return a+b+c
    
m = Math()

print(m.add(2,4))
print(m.add(1,2,5))