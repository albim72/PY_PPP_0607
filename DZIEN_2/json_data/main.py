import json

#ładowanie listy książek
def load_books(filename):
    try:
        with open(filename, 'r',encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Plik nie istnieje. Tworzę nową listę kiążek")
        return []

#zapisanie listy do pliku
def save_books(books, filename):
    with open(filename, 'w',encoding='utf-8') as f:
        json.dump(books, f, indent=4,ensure_ascii=False)
    print(f"Zapisano listę {len(books)} kiążek do pliku {filename}")

#wyświetl wszystkie ksiażki
def display_books(books):
    if not books:
        print("Brak książek do wyświetlenia")
    for book in books:
        print(f"{book['title']} wydany w roku {book['year']}")

#dodawanie nowej książki
def add_new_book():
    print(f"\nDodaj nową książkę: ")
    title = input("Tytuł: ").strip()
    author = input("Autor: ").strip()
    while True:
        try:
            year = int(input("Rok wydania: "))
            break
        except ValueError:
            print("Błędny format daty. Spróbuj ponownie.")
    return {"title": title, "author": author, "year": year}

def main():
    filename = "books_20.json"
    books = load_books(filename)
    choice = input("\nCzy chcesz dodacmbać nową książkę? (t/n): ").lower()
    if choice == "t":
        new_book = add_new_book()
        books.append(new_book)
        save_books(books, filename)
        print("Książka dodana pomyślnie!")
        display_books(books)
    else:
        print("Zakończono bez zmiany")

if __name__ == '__main__':
    main()
