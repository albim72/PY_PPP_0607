class Book:
    def __init__(self, title, author, year, pages, price):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.price = float(price)
        self.read_pages = 0
        self.finished = False

    def read(self, pages):
        if self.finished:
            print(f"skończyłeś czytac książkę {self.title}")
            return
        self.read_pages += pages
        if self.read_pages >= self.pages:
            self.read_pages = self.pages
            self.finished = True
            print(f"zakończyłeś czytac książkę {self.title}")
        else:
            print(f"czytasz {pages} stronę książki. Przeczytano {(self.read_pages/self.pages)*100:.2f}% stron")

    def restart(self):
        self.read_pages = 0
        self.finished = False
        print(f"czytasz od początku książkę {self.title}")

    def percent_read(self):
        return round((self.read_pages/self.pages)*100,1)

    def value_read(self,new_price):
        self.price = float(new_price)
        print(f"nowa cena {self.title}: {self.price:.2f} zł")

    def discount(self,percent):
        self.price *= (1-percent/100)
        self.price = round(self.price,2)
        print(f"nowa cena po rabacie {self.title}: {self.price:.2f} zł")

    def __str__(self):
        status = "zakończona" if self.finished else "czytana"
        return f"{self.title} - {self.author} - {self.year} - {self.pages} stron - {status} - {self.percent_read()}%"

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.year} - {self.price:.2f} zł"

    #metody getter i setter - tradycyjnie
    def get_price(self):
        return self.price

    def set_price(self,new_price):
        if new_price <= 12:
            raise ValueError("Cena musi być liczbą większą od 12")
        self.price = new_price

    #metody getter i setter - wbudowane w pythona -> properties
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,new_title):
        if len(new_title) < 9:
            raise ValueError("Tytuł musi mieć co najmniej 9 znaków")
        self._title = new_title



print("***********************************************")

b1 = Book("Python 101 przepisów!","Marcin Albiniak",2025,340,60.0)
b2 = Book("AI dla  początkujących!","Marcin Albiniak",2025,220,72.0)

b1.read(70)
b2.read(110)

print(b1)
print(b2)

print("***********************************************")
print(f"wartość przeczytanej książki {b1.title}: {b1.get_price():.2f} zł")
print(f"wartość przeczytanej książki {b2.title}: {b2.get_price():.2f} zł")

print("***********************************************")
b1.discount(10)
b2.discount(15)
b1.read(99)
b2.read(101)
b1.value_read(89)
b2.value_read(122)

b1.set_price(211)
print(b1.get_price())

print("***********************************************")
print("zmiana tytułu książki")
b1.title = "Python 101"
print(b1)
