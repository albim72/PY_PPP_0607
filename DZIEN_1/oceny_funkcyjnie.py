def dodaj_ucznia(slownik,imie,ocena):
    slownik[imie]=ocena

def zmien_ocene(slownik,imie,nowa_ocena):
    slownik[imie]=nowa_ocena

def usun_ucznia(slownik,imie):
    slownik.pop(imie,None)

def wyswietl_uczniow_z_dobra_ocena(slownik,prog=3):
    print(f"uczniowie z oceną powyzej {prog}:")
    for imie,ocena in slownik.items():
        if ocena>prog:
            print(f"{imie}: {ocena}")

def znajdz_najlepszego_ucznia(slownik):
    if not slownik:
        return []
    najwyzsza = max(slownik.values())
    return [(imie,ocena) for imie,ocena in slownik.items() if ocena==najwyzsza]

def wyswietl_wszystkie_oceny(slownik):
    print("oceny uczniów(lista):")
    for imie,ocena in slownik.items():
        print(f"{imie}: {ocena}")


# ==== Głowna częśc programu ======

oceny={
    "Anna":5,
    "Mikołaj":4,
    "Jakub":3,
    "Maria":2,
    "Kasia":1,
    "Łukasz":5,
    "Ola":3,
    "Piotr":4,
    "Felicia":1,
    "Alicja":1,
    "Ewa":5,
    "Michał":2,
    "Tomasz":4,
    "Marcin":4,
    "Mateusz":4,
    "Katarzyna":5,
    "Eryk":2,
    "Nadia":4
}

#wykonywanie operacji
dodaj_ucznia(oceny,"Aneta",5)
dodaj_ucznia(oceny,"Leon",2)
dodaj_ucznia(oceny,"Bartek",3)

wyswietl_wszystkie_oceny(oceny)
print("____________________________________")

zmien_ocene(oceny,"Piotr",5)
usun_ucznia(oceny,"Aneta")
usun_ucznia(oceny,"Tomasz")

wyswietl_uczniow_z_dobra_ocena(oceny,4)
print("____________________________________")

najlepsi =znajdz_najlepszego_ucznia(oceny)
print(f"\nnajlepsi uczniowie:")
for imie,ocena in najlepsi:
    print(f"{imie}: {ocena}")
