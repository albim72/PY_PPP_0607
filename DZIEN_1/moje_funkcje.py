#funkcja bez argumentów - nic  nie zwracająca
def przywiatanie():
    print("Witaj! To moja pierwsza funkcja!")

przywiatanie()
przywiatanie()

#funkcja z argumentem nic nie zwracająca
def powiedz_cos(imie,cos):
    print(f"{imie} mówi: {cos}")

powiedz_cos("Jan", "Cześć!")
powiedz_cos("Anna", "Ładna dziś pogoda!")

#funkcja z parametrami która zwraca wartośc
def policz(a,b):
    return a+b*2

wynik = policz(1,2)
print(wynik)

#funkcja z domyślnym argumentem
def powtorz_teskt(tekst, ile=3):
    print(f"{tekst*ile}")

powtorz_teskt("Hej",6)
powtorz_teskt("Echo")
powtorz_teskt("Mocny cios ",11)

#funkcja zwracająca True/False
def czy_parzysta(liczba):
    return liczba%2==0

print(czy_parzysta(10))
print(czy_parzysta(11))

print("__________________________________________________")

#zmienne lokalne
def funkcja_zmienne_lokalne():
    x = 10
    y = 20
    print(x+y)

funkcja_zmienne_lokalne()

#zmienne globalne
x=7
def funkcja_zmienne_globalne():
    # x = 10
    global x
    x = 8
    k = x * 2
    x = x +.004
    print(f"x globalne: {x}, -> wynik {k}")

funkcja_zmienne_globalne()
print(f"x globalne: {x}")

print("__________________________________________________")
l = [1,4,7,8]
def dodaj_el(l):
    l.append(10)

dodaj_el(l)
print(l)

print("dobra praktyka")
def funkcja_paramx(x):
    # x = 1
    k = x * 2
    x = x +.004
    print(f"x globalne: {x}, -> wynik {k}")

funkcja_paramx(10)
