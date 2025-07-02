import random

def zgadnij_liczbe():
    tajna_liczba = random.randint(1, 10)
    try:
        wejscie = input("Podaj liczbę od 1 do 10: ")
        liczba = int(wejscie)
        assert 1<=liczba<=10, "Liczba spoza przedziału"
        if liczba == tajna_liczba:
            print("Brawo! Zgadłeś!")
        else:
            print(f"Nie tym razem. Prawidłowa liczba to: {tajna_liczba}.")
    except ValueError:
        print("To nie jest liczba całkowita!")
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Inny błąd:", type(e).__name__)
        print("Opis:", str(e))
    finally:
        print("Koniec gry.")

zgadnij_liczbe()
