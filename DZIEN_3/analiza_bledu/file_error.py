try:
    nazwa = input("Podaj nazwę pliku: ")
    with open(nazwa, "r") as f:
        zawartosc = f.read()
        print("Zawartość pliku:\n", zawartosc)

except FileNotFoundError:
    print("Błąd: Nie znaleziono pliku!")

except Exception as e:
    print("Inny błąd:", type(e).__name__)
    print("Opis:", str(e))

finally:
    print("Koniec programu.")
