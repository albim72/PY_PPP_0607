print((lambda x: x**2)(45))

f = lambda x,y: x*3+y*2
print(f(4,2))

#sortowanie listy par
oceny = [("Anna",5),("Kasia",4),("Mikołaj",3),("Michal",2),("Michał",1)]
posortowane = sorted(oceny, key=lambda x: x[1])
print(posortowane)
poimieniu = sorted(oceny, key=lambda x: x[0])
print(poimieniu)

#filtorwanie liczb
liczby = [23,32,11,4,5,6,78,8,91,47]
wynik = list(filter(lambda x: x>10, liczby))
print(wynik)

#funcja lambda na return innej funckji
def stworz_mnoznik(n):
    return lambda x: x*n

p2 = stworz_mnoznik(2)
p3 = stworz_mnoznik(3)(3)
print(p2(2))
print(p3)
