class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
print(issubclass(Cat, Animal))
print(issubclass(Puppy, Dog))