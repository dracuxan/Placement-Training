class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Barks")


class Owner:
    def __init__(self, name, no, dog):
        self.fname = name
        self.number = no
        self.dog = dog


d1 = Dog("a", "b")
o1 = Owner("Nisarg", 1, d1)


print(d1.name, d1.breed)
d1.bark()
print(o1.dog.name)
print()
