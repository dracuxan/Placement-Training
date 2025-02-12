class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Barks")


d1 = Dog("a", "b")

print(d1.name, d1.breed, d1.bark())
print()
