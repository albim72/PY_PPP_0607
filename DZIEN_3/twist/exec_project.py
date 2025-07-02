komenda = input("Podaj kod Pythona do wykonania (np. print(2 + 2)): ")
try:
    exec(komenda)
except Exception as e:
    print("Wystąpił błąd:", e)



liczby = [1, 2, 3, 4, 5]
podniesione = list(map(lambda x: x ** 3, liczby))

print("Kostki liczb:", podniesione)
# Funkcyjny filtr liczb parzystych
parzyste = list(filter(lambda x: x % 2 == 0, liczby))

def zapamietaj_powitanie(imie):
    def witaj():
        print(f"Cześć, {imie}!")
    return witaj

moje_powitanie = zapamietaj_powitanie("Ania")
moje_powitanie()  # ➤ Cześć, Ania!


def podwajacz(funkcja):
    def wrapper(x):
        return funkcja(x) * 2
    return wrapper

@podwajacz
def daj_liczbe(x):
    return x + 1

print(daj_liczbe(3))  # ➤ (3 + 1) * 2 = 8
