#zbiory (set)
from itertools import combinations

grupa_A = {"Anna","Bartek","Celina","Darek","Edyta","Leon","Maria","Leon"}
grupa_B = {"Henryk","Bartek","Miłosz","Darek","Tomasz","Julia","Maria"}

print(grupa_A)
print(grupa_A)
print(grupa_B)
print(grupa_B)
print(type(grupa_A))

specjalny = {4,6}
lt = [3,7,2,6]
specjalny.update(lt)
print(specjalny)

#wzpólne imiona  obu grupach
wspolne = grupa_A.intersection(grupa_B)
print(wspolne)

#osoby tylko z grupy A
osoby_A = grupa_A.difference(grupa_B)
print(osoby_A)

#wszysycy unikalni uczestnicy
unikalni = grupa_A.union(grupa_B)
print(unikalni)

#tworzenie słownika par jako frozenset
pary = {}
for osoba1,osoba2 in combinations(unikalni,2):
    klucz = frozenset({osoba1,osoba2})
    pary[klucz] = "match"

print(f"\nliczba możliwych unikalnych par: {len(pary)}")
print("Przykładowe pary(pierwsze 5):")
for i,(klucz,wartosc) in enumerate(pary.items()):
    if i>=5:
        break
    print(f"{klucz} -> {wartosc}")

#słowniki

oceny = {
    "Anna": 5,
    "Bartek": 4,
    "Celina": 3,
    "Darek": 2,
    "Edyta": 4,
    "Leon": 4,#zbiory (set)
from itertools import combinations

grupa_A = {"Anna","Bartek","Celina","Darek","Edyta","Leon","Maria","Leon"}
grupa_B = {"Henryk","Bartek","Miłosz","Darek","Tomasz","Julia","Maria"}

print(grupa_A)
print(grupa_A)
print(grupa_B)
print(grupa_B)
print(type(grupa_A))

specjalny = {4,6}
lt = [3,7,2,6]
specjalny.update(lt)
print(specjalny)

#wzpólne imiona  obu grupach
wspolne = grupa_A.intersection(grupa_B)
print(wspolne)

#osoby tylko z grupy A
osoby_A = grupa_A.difference(grupa_B)
print(osoby_A)

#wszysycy unikalni uczestnicy
unikalni = grupa_A.union(grupa_B)
print(unikalni)

#tworzenie słownika par jako frozenset
pary = {}
for osoba1,osoba2 in combinations(unikalni,2):
    klucz = frozenset({osoba1,osoba2})
    pary[klucz] = "match"

print(f"\nliczba możliwych unikalnych par: {len(pary)}")
print("Przykładowe pary(pierwsze 5):")
for i,(klucz,wartosc) in enumerate(pary.items()):
    if i>=5:
        break
    print(f"{klucz} -> {wartosc}")

#słowniki

oceny = {
    "Anna": 5,
    "Bartek": 4,
    "Celina": 3,
    "Darek": 2,
    "Edyta": 4,
    "Leon": 4,
    "Maria": 3,
    "Leon": 3,
}

print(oceny)

oceny["Franek"] = 5
print(oceny)
oceny["Anna"]=3
print(oceny)

#studenci z oceną powyżej 3
print(f"studenci z oceną powyżej 3:\n")
for imie,ocena in oceny.items():
    if ocena > 3:
        print(f"{imie} - {ocena}")

print(f"\nuczeń z najwyższą oceną:\n")
najlepszy = max(oceny,key=oceny.get)
print(f"{najlepszy} - {oceny[najlepszy]}")

print(f"\nśrednia ocen\n")
srednia = sum(oceny.values())/len(oceny) if len(oceny)>0 else 0
print(f"średnia: {srednia}")

print(srednia)
    "Maria": 3,
    "Leon": 3,
}

print(oceny)

oceny["Franek"] = 5
print(oceny)
oceny["Anna"]=3
print(oceny)

#studenci z oceną powyżej 3
print(f"studenci z oceną powyżej 3:\n")
for imie,ocena in oceny.items():
    if ocena > 3:
        print(f"{imie} - {ocena}")

print(f"\nuczeń z najwyższą oceną:\n")
najlepszy = max(oceny,key=oceny.get)
print(f"{najlepszy} - {oceny[najlepszy]}")

print(f"\nśrednia ocen\n")
srednia = sum(oceny.values())/len(oceny) if len(oceny)>0 else 0
print(f"średnia: {srednia}")

print(srednia)
