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
        return None,None
    najlepszy = max(slownik, key=slownik.get)
    return najlepszy,slownik[najlepszy]

def wyswietl_wszystkie_oceny(slownik):
    print("oceny uczniów(lista):")
    for imie,ocena in slownik.items():
        print(f"{imie}: {ocena}")
