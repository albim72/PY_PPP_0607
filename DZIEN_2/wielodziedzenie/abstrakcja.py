from abc import ABC, abstractmethod

class A(ABC):
    def metodaA(self):
        print("A")

class Abstract(ABC,A):
    @abstractmethod
    def metoda(self):
        pass


class Uchwyt(Abstract):
    def metoda(self):
        print("Uchwyt XZ")
