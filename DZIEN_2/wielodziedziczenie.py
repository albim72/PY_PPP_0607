#klasy bazowe - te które będą dziedziczone
class Camera:
    def __init__(self, rodzaj, rodzaj_kontrastu):
        self.rodzaj = rodzaj
        self.rodzaj_kontrastu = rodzaj_kontrastu
        print("Aparat został utworzony")

    def take_photo(self):
        print("Zdjęcie zostało zapisane")


class GPS:
    def __init__(self, miejsce):
        self.miejsce = miejsce
        print("GPS został utworzony")

    def get_location(self):
        print("Miejsce zostało zapisane - lokacja (52.23, 21.09)")

#klasa potomna
class Smartphone(Camera, GPS):
    def __init__(self, rodzaj, rodzaj_kontrastu, miejsce, marka):
        Camera.__init__(self, rodzaj, rodzaj_kontrastu)
        GPS.__init__(self, miejsce)
        self.marka = marka
        print("Smartphone został utworzony")

    def info(self):
        print(f"Marka: {self.marka}")


device = Smartphone("Nokia", "normalny", "Warszawa", "Nokia")
device.info()
device.take_photo()
device.get_location()
