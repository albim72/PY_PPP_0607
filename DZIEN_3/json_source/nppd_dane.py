import csv
import random
import pandas as pd

# === KROK 1: Generowanie pliku CSV ===
plik_csv = "produkty_duze.csv"

naglowki = ["ID", "Nazwa", "Kategoria", "Cena", "Dostępność"]
kategorie = ["Elektronika", "Książki", "Moda", "Dom", "Zabawki", "Sport"]
dostepnosc_opcje = ["Dostępny", "Brak", "Na zamówienie"]

with open(plik_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(naglowki)
    for i in range(1, 501):
        produkt = [
            i,
            f"Produkt_{i}",
            random.choice(kategorie),
            round(random.uniform(10.0, 1000.0), 2),
            random.choice(dostepnosc_opcje)
        ]
        writer.writerow(produkt)

print("Plik CSV został wygenerowany.")

# === KROK 2: Wczytanie danych z CSV ===
df = pd.read_csv(plik_csv)

# === KROK 3: Analiza danych ===

# 1. Liczba produktów w każdej kategorii
produkty_na_kategorie = df["Kategoria"].value_counts()

# 2. Średnia cena tylko dla produktów „Dostępnych”
srednia_dostepnych = df[df["Dostępność"] == "Dostępny"]["Cena"].mean()

# 3. Najdroższy produkt w kategorii „Elektronika”
df_elektronika = df[df["Kategoria"] == "Elektronika"]
najdrozszy = df_elektronika.loc[df_elektronika["Cena"].idxmax()]

# === KROK 4: Wyświetlenie wyników ===
print("\n📊 Produkty na kategorię:")
print(produkty_na_kategorie)

print(f"\n💰 Średnia cena dostępnych produktów: {round(srednia_dostepnych, 2)} zł")

print("\n🔝 Najdroższy produkt w kategorii 'Elektronika':")
print(f"   Nazwa: {najdrozszy['Nazwa']}")
print(f"   Cena: {najdrozszy['Cena']} zł")
