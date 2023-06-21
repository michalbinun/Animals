from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, is_mammal, is_carnivorous, happy_mood=0, scared_mood=0):
        self.is_mammal = is_mammal
        self.is_carnivorous = is_carnivorous
        self.happy_mood = happy_mood
        self.scared_mood = scared_mood
    
    @abstractmethod
    def say_hello(self):
        pass
    
    @abstractmethod
    def get_number_of_legs(self):
        pass
    
    def is_mammal(self):
        return self.is_mammal
    
    def set_mammal(self, is_mammal):
        self.is_mammal = is_mammal
    
    def is_carnivorous(self):
        return self.is_carnivorous
    
    def set_carnivorous(self, is_carnivorous):
        self.is_carnivorous = is_carnivorous


class Dog(Animal):
    def __init__(self, is_mammal, is_carnivorous, happy_mood=0, scared_mood=0):
        super().__init__(is_mammal, is_carnivorous, happy_mood, scared_mood)
    
    def say_hello(self):
        print("The dog wags its tail and barks loudly.")
    
    def get_number_of_legs(self):
        return 4


class Cat(Animal):
    def __init__(self, is_mammal, is_carnivorous, happy_mood=0, scared_mood=0):
        super().__init__(is_mammal, is_carnivorous, happy_mood, scared_mood)
    
    def say_hello(self):
        print("The cat meows~")
    
    def get_number_of_legs(self):
        return 4


class Frog(Animal):
    def __init__(self, is_mammal, is_carnivorous, happy_mood=0, scared_mood=0):
        super().__init__(is_mammal, is_carnivorous, happy_mood, scared_mood)
    
    def say_hello(self):
        print("The frog quacks quack quack on the shore.")
    
    def get_number_of_legs(self):
        return 4


def main():
    dog = Dog(True, True)
    dog.say_hello()
    print("Number of legs:", dog.get_number_of_legs())
    dog.set_mammal(False)
    print("Is mammal?", dog.is_mammal())

    print()

    cat = Cat(True, True)
    cat.say_hello()
    print("Number of legs:", cat.get_number_of_legs())
    cat.set_carnivorous(False)
    print("Is carnivorous?", cat.is_carnivorous())

    print()

    frog = Frog(False, False)
    frog.say_hello()
    print("Number of legs:", frog.get_number_of_legs())

if __name__ == "__main__":
    main()

