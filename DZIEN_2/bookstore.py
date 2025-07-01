class Book:
    def __init__(self, title, author, year, pages, price):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.price = float(price)
        self.read_pages = 0
        self.finished = False
