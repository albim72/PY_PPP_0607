#wejście wyjście użytkownika - konsola
miasto = input("Jakie jest miasto? ")
print("Miasto:", miasto)
#wejście z klawiatury - konsola, wyjście na ekran

#zapis do pliku
with open("miasto.txt", "w", encoding="utf-8") as plik:
    plik.write(f"to jest miasto: {miasto}\n")
    plik.write("kolejna linia\n")

f = open("info.txt", "w", encoding="utf-8")
f.write("taki ważne słowa.....\n")

f = open("info.txt", "a", encoding="utf-8")
f.write("drugie ważne słowa.....")

print(f.closed)
print(plik.closed)
#odczyt z pliku

with open("miasto.txt", "r", encoding="utf-8") as plik:
    for linia in plik:
        print(linia, end="")

with open("miasto.txt", "r", encoding="utf-8") as plik:
    content = plik.read()
    print(content)


#zapis z klekcji

dane = ["Henryk","Jolanta","Tomasz","Ula"]

with open("words.txt","w",encoding="utf-8") as f:
    for word in dane:
        f.write(word+"\n")
