# Activity 2: Polymorphism Challenge 🎭

class Animal:
    def move(self):
        pass  # to be overridden


class Dog(Animal):
    def move(self):
        print("🐕 Running on four legs")


class Bird(Animal):
    def move(self):
        print("🐦 Flying in the sky")


class Fish(Animal):
    def move(self):
        print("🐟 Swimming in water")


# ----------- TESTING -------------
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
