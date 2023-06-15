# Define the abstract class Animal
class Animal:
    def __init__(self, sound_when_greeting, sound_when_happy, sound_when_frightened):
        self.sound_when_greeting = sound_when_greeting
        self.sound_when_happy = sound_when_happy
        self.sound_when_frightened = sound_when_frightened

    def greet(self):
        print(self.sound_when_greeting)

    def express_happiness(self):
        print(self.sound_when_happy)

    def express_fear(self):
        print(self.sound_when_frightened)


# Define the abstract class Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def greet(self):
        pass

    def make_sound(self):
        pass


# Define the subclass Dog
class Dog(Animal):
    def greet(self):
        return f"{self.name} wagging its tail"

    def make_sound(self, feeling):
        if feeling == "comfortable":
            return f"{self.name} barking loudly"
        elif feeling == "frightened":
            return f"{self.name} making a whooping sound"
        else:
            return f"{self.name} making an unknown sound"


# Define the subclass Cat
class Cat(Animal):
    def greet(self):
        return f"{self.name} meowing"

    def make_sound(self, feeling):
        if feeling == "good mood":
            return f"{self.name} purring"
        elif feeling == "frightened":
            return f"{self.name} hissing"
        else:
            return f"{self.name} making an unknown sound"


# Testing the code
def main():
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    print(dog.greet())  # Output: Buddy wagging its tail
    print(dog.make_sound("comfortable"))  # Output: Buddy barking loudly

    print(cat.greet())  # Output: Whiskers meowing
    print(cat.make_sound("good mood"))  # Output: Whiskers purring


if __name__ == "__main__":
    main()
