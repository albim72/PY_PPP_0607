from animals import Dog,Cat,Snake
from utils import make_animal_speak

def main():
    zoo = [
        Dog("Ludvik"),
        Cat("Luna"),
        Snake("Slitherin")
    ]

    for animal in zoo:
        make_animal_speak(animal)
        print("_________________")

if __name__ == '__main__':
    main()
