print("to jest pierwszy program")
a = 100
print(a)
print(type(a))

miasto = "Kraków"
print(miasto)
print(type(miasto))

b:int = 2
print(b)
print(type(b))

#następuje usunięcie adresu pamięci przypisanego dla b:int
# a jednocześnie utworzenie nowego adresu pamięci dla b(które przy inicjacji staje się stringiem)
b = "dwójka"
print(b)
print(type(b))

imie = input("Podaj imię: ")
miasto = input("Podaj miasto: ")
wiek = input("Podaj wiek: ")

if not wiek.isdigit():
    print("Podano nie liczbę!")
    exit()
else:
    wiek:int = int(wiek)
    #logika zależna od wieku
    if wiek>=18:
        print(f"Czesc {imie} z {miasto}! masz {wiek} lat. Jesteś pełnoletni!")
    else:
        print(f"Czesc {imie} z {miasto}! masz {wiek} lat. Jesteś niepełnoletni!")


do_setki = 100 - wiek

print(f"{imie}!, za  {do_setki} lat będziesz miec 100!.")

print("__________________________________")

