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
            print(f"czytasz {pages} stronę książki. Przeczytano {(self.read_pages/self.pages)*100}% stron")
            
    def restart(self):
        self.read_pages = 0
        self.finished = False
        print(f"czytasz od początku książkę {self.title}")
        
    def percent_read(self):
        return round((self.read_pages/self.pages)*100,1)
    
    def value_read(self,new_price):
        self.price = float(new_price)
        print(f"nowa cena {self.title}: {self.price:.2f} zł")
