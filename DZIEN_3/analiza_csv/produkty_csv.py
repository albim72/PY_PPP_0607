import csv
from collections import defaultdict

kategoria_licznik = defaultdict(int)
suma_dostepnych = 0
licznik_dostepnych = 0
najdrozszy_elektronika = ("", 0.0)

with open("produkty_duze.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        kat = row["Kategoria"]
        cena = float(row["Cena"])
        dostepnosc = row["Dostępność"]
        nazwa = row["Nazwa"]

        kategoria_licznik[kat] += 1

        if dostepnosc == "Dostępny":
            suma_dostepnych += cena
            licznik_dostepnych += 1

        if kat == "Elektronika" and cena > najdrozszy_elektronika[1]:
            najdrozszy_elektronika = (nazwa, cena)

# Wyniki
print("Produkty wg kategorii:")
for k, v in kategoria_licznik.items():
    print(f" - {k}: {v} szt.")

print("\nŚrednia cena dostępnych produktów:",
      round(suma_dostepnych / licznik_dostepnych, 2))

print("\nNajdroższy produkt w kategorii 'Elektronika':",
      f"{najdrozszy_elektronika[0]} – {najdrozszy_elektronika[1]} zł")
