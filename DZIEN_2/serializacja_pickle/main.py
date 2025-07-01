from book import Book
from  pkl_tool import save_books_to_file,load_books_from_file

if __name__ == '__main__':
    books = [
        Book("Python", "Harry Potter", 100),
        Book("Java", "Harry Potter", 100),
        Book("C++", "Harry Potter", 100)

    ]
    save_books_to_file(books,"books.pkl")
    books = load_books_from_file("books.pkl")
    for book in books:
        print(book)

    print(books)
