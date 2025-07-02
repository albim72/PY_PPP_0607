import pandas as pd
import random

# === KROK 1: Generowanie danych do DataFrame ===

kategorie = ["Elektronika", "Książki", "Moda", "Dom", "Zabawki", "Sport"]
statusy = ["Dostępny", "Brak", "Na zamówienie"]

# Tworzymy słownik z listami kolumn
data = {
    "ID": list(range(1, 1001)),
    "Nazwa": [f"Produkt_{i}" for i in range(1, 1001)],
    "Kategoria": [random.choice(kategorie) for _ in range(1000)],
    "Cena": [round(random.uniform(10.0, 2000.0), 2) for _ in range(1000)],
    "Dostępność": [random.choice(statusy) for _ in range(1000)]
}

# Tworzymy DataFrame
df = pd.DataFrame(data)

# === KROK 2: Zapis do pliku CSV ===

plik_csv = "produkty_pandas.csv"
df.to_csv(plik_csv, index=False)
print(f"Dane zapisano do pliku: {plik_csv}")

# === KROK 3: Wczytanie pliku CSV ponownie ===

df_wczytane = pd.read_csv(plik_csv)
print(f"Plik {plik_csv} został wczytany.")

# === KROK 4: Prosta analiza danych ===

# 1. Liczba produktów w każdej kategorii
produkty_na_kategorie = df_wczytane["Kategoria"].value_counts()

# 2. Średnia cena tylko dla produktów „Dostępnych”
srednia_dostepnych = round(
    df_wczytane[df_wczytane["Dostępność"] == "Dostępny"]["Cena"].mean(), 2)

# 3. Najdroższy produkt w całym zbiorze
najdrozszy = df_wczytane.loc[df_wczytane["Cena"].idxmax()]

# === KROK 5: Wyświetlenie wyników ===

print("\nLiczba produktów w kategoriach:")
print(produkty_na_kategorie)

print(f"\nŚrednia cena dostępnych produktów: {srednia_dostepnych} zł")

print("\nNajdroższy produkt:")
print(f"  Nazwa: {najdrozszy['Nazwa']}")
print(f"  Cena: {najdrozszy['Cena']} zł")
