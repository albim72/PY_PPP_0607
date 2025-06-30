#lista ulubionych języków programowania
jezyki:list[str] = ["Python", "C++", "Java","C#","JavaScript"]

#krotka z danymi
uzytkownik:tuple[str,int,str] = ("Mikołaj",25,"Kraków")

print(jezyki)
print(type(jezyki))
print(uzytkownik)
print(type(uzytkownik))

#dopisanie języka
jezyki.append("Ruby")
print(jezyki)
#dopsanie języka na pyzcji 2
jezyki.insert(2,"C")
print(jezyki)

jezyki.remove("C#")
print(jezyki)
print("Java" in jezyki)
print("Swift" in jezyki)

#usunięcie ostatniego elementu
ost =  jezyki.pop()
print(jezyki)
print(ost)

print("\nUlubione języki:")
for j,jz in enumerate(jezyki,start=1):
    print(f"{j}. {jz}")

print("\nwyświetlenie danych użytkownika:")
print(f" Imie: {uzytkownik[0]},\n Wiek: {uzytkownik[1]},\n Miejsce zamieszkania: {uzytkownik[2]}")
dodatkowe_dane = ("1974","Dyrektor techniczy (CTO)")

d = uzytkownik.__add__(dodatkowe_dane) #__add__ - konkatenacja krotek
print(d)

kolory = ("czerwony","niebieski","zielony","fioletowy","zolty")
#dodaj dwa kolory do krotki: srebrny i purpurowy
kolory = kolory + ("srebrny","purpurowy")
print(kolory)

kolorlt = list(kolory)
kolorlt.append("magenta")
kolorlt.insert(0,"cyan")

kolory = tuple(kolorlt)
print(kolory)
