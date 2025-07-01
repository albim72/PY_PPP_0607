#serializacja_pickle/pkl_tool.py
import pickle

def save_books_to_file(books,filename):
    with open(filename,'wb') as f:
        pickle.dump(books,f)
    print(f"Zapisano {len(books)} książek do pliku {filename} (binarnie)")

def load_books_from_file(filename):
    with open(filename,'rb') as f:
        books = pickle.load(f)
    print(f"Załadowano {len(books)} książek z pliku {filename} (binarnie)")
    return books
