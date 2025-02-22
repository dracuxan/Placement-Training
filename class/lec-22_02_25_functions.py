class Hello:
    def __init__(self, name):
        print("Hello", name)

    def add(self, a, b):
        return (a + b, a * b, a / b, a - b)

    def recursive(self, n):
        print(n)
        if n < 10:
            self.recursive(n + 1)


a = Hello("Nisarg")
calc = a.add(1, 2)

a.recursive(1)
print(calc)
