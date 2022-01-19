class Dog:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
    def bark(self):
        print("Woof!")
    def eat(self):
        print(f"{self.name} is eating")

dog1 = Dog("Choco","Brown","Big")
dog1.bark()
dog1.eat()