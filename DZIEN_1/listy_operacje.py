teksty = ["Anna","Tymek","Marek","Kasia","Krzysztof","Michał","Krzysztof","Krzysztof","Leon"]

print(teksty)

wycinek = teksty[2:5] #wycinek - slice
print(wycinek)
print(teksty[6])
print(teksty[:4])
print(teksty[3:])
print(teksty[-1])
print(teksty[::2]) #pozycje parzyste
print(teksty[1::2]) #pozycje nieparzyste
#odwrócmy listę -> list[start:stop:krok]
print(teksty[::-1])

teksty.reverse() #zamiana listy

print(teksty)

tk = list(teksty)
tk.sort()#sortowanie listy
print(teksty)
print(tk)

#tworzenie kopii
import copy

l1 = [[1,2],[3,4]]
l2 = copy.copy(l1)
# l1[0] = [2,7]
# l1[0][1] = 90
# l2[1] = [3,3]
l2[1][1] = 100 #kopia copy nie  blokuje w wewnętrznych listach
print(l1)
print(l2)

#kopia głęboka
listaR = [[1,2],[3,4],[5,6]]

listaR2 = copy.deepcopy(listaR)
listaR2[1][1] = 100

print(listaR)
print(listaR2)

hero = "superman"

print(hero)

print(hero[1:3])
print(hero[:4])
print(hero[4:])
print(hero[::-1])

print(hero.upper())
print(hero.replace("m","n"))
print(len(hero))

#operacje tekstowe na liście
duze = [tekst.upper() for tekst in teksty] #list comprehension
print(duze)

#zamiana liter w liście
zamienione = [imie.replace("a","e") for imie in teksty]
print(zamienione)

#filtrowanie
filtr = [imie for imie in teksty if imie.startswith(("K","A"))]
print(filtr)


