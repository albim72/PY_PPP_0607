from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def describe(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def describe(self):
        print(f"Koło o promieniu: {self.radius}")


circle = Circle(10.5)
circle.describe()
print(f"pole koła: {circle.area()}")
