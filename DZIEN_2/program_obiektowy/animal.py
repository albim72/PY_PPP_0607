class Animal:
    #opis stanu
    #konstruktory
    def __init__(self, name):
        self.name = name

    #opis działania
    def speak(self):
        return "???"

    def info(self):
        return f"Jestem zwirzęciem: {self.name}"
