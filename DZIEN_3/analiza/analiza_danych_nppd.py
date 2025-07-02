
import csv
import random
import pandas as pd
import xml.etree.ElementTree as ET

# === KROK 1: Generowanie dużego pliku CSV ===

plik_wejsciowy = "produkty_analityka.csv"

naglowki = ["ID", "Nazwa", "Kategoria", "Cena", "Dostępność"]
kategorie = ["Elektronika", "Książki", "Moda", "Dom", "Zabawki", "Sport"]
statusy = ["Dostępny", "Brak", "Na zamówienie"]

with open(plik_wejsciowy, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(naglowki)
    for i in range(1, 1001):  # 1000 rekordów
        writer.writerow([
            i,
            f"Produkt_{i}",
            random.choice(kategorie),
            round(random.uniform(10.0, 2000.0), 2),
            random.choice(statusy)
        ])

print("Plik CSV został wygenerowany.")

# === KROK 2: Wczytanie danych z CSV ===

df = pd.read_csv(plik_wejsciowy)

# === KROK 3: Analiza danych ===

# 1. Liczba produktów w każdej kategorii
produkty_na_kategorie = df["Kategoria"].value_counts().to_dict()

# 2. Średnia cena dostępnych produktów
srednia_cena_dostepnych = round(df[df["Dostępność"] == "Dostępny"]["Cena"].mean(), 2)

# 3. Najdroższy produkt ogólnie
najdrozszy_produkt = df.loc[df["Cena"].idxmax()]

# === KROK 4: Zapis wyników do CSV ===

plik_wynikowy_csv = "wyniki_analizy.csv"

with open(plik_wynikowy_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Metryka", "Wartość"])
    for kategoria, liczba in produkty_na_kategorie.items():
        writer.writerow([f"Liczba produktów w kategorii: {kategoria}", liczba])
    writer.writerow(["Średnia cena dostępnych produktów", srednia_cena_dostepnych])
    writer.writerow(["Najdroższy produkt", najdrozszy_produkt["Nazwa"]])
    writer.writerow(["Cena najdroższego produktu", najdrozszy_produkt["Cena"]])

print(f"Wyniki analizy zapisano do {plik_wynikowy_csv}")

# === KROK 5: Zapis wyników do XML ===

plik_wynikowy_xml = "wyniki_analizy.xml"

root = ET.Element("analiza")

# Produkty na kategorie
kat_elem = ET.SubElement(root, "produkty_na_kategorie")
for kat, liczba in produkty_na_kategorie.items():
    ET.SubElement(kat_elem, "kategoria", nazwa=kat).text = str(liczba)

# Średnia cena
ET.SubElement(root, "srednia_cena_dostepnych").text = str(srednia_cena_dostepnych)

# Najdroższy produkt
naj_elem = ET.SubElement(root, "najdrozszy_produkt")
ET.SubElement(naj_elem, "nazwa").text = najdrozszy_produkt["Nazwa"]
ET.SubElement(naj_elem, "cena").text = str(najdrozszy_produkt["Cena"])

# Zapis do pliku
tree = ET.ElementTree(root)
tree.write(plik_wynikowy_xml, encoding="utf-8", xml_declaration=True)

print(f"Wyniki analizy zapisano do {plik_wynikowy_xml}")
