import csv
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import xml.etree.ElementTree as ET

# === KROK 1: Generowanie pliku CSV ===

plik_csv = "produkty_plot.csv"
naglowki = ["ID", "Nazwa", "Kategoria", "Cena", "Dostępność"]
kategorie = ["Elektronika", "Książki", "Moda", "Dom", "Zabawki", "Sport"]
statusy = ["Dostępny", "Brak", "Na zamówienie"]

with open(plik_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(naglowki)
    for i in range(1, 1001):
        writer.writerow([
            i,
            f"Produkt_{i}",
            random.choice(kategorie),
            round(random.uniform(10.0, 2000.0), 2),
            random.choice(statusy)
        ])

print("✅ Plik CSV wygenerowany.")

# === KROK 2: Wczytanie danych z Pandas + NumPy ===

df = pd.read_csv(plik_csv)

# Zamieniamy kolumnę "Cena" na tablicę NumPy
ceny_numpy = df["Cena"].to_numpy()

# Analiza: NumPy – statystyki ogólne
srednia_numpy = np.mean(ceny_numpy)
mediana_numpy = np.median(ceny_numpy)
min_numpy = np.min(ceny_numpy)
max_numpy = np.max(ceny_numpy)
std_numpy = np.std(ceny_numpy)

# Analiza: Pandas – logika warunkowa
produkty_na_kategorie = df["Kategoria"].value_counts()
srednia_cena_dostepnych = round(df[df["Dostępność"] == "Dostępny"]["Cena"].mean(), 2)
najdrozszy = df.loc[df["Cena"].idxmax()]

# === KROK 3: Matplotlib – wykres słupkowy kategorii ===

plt.figure(figsize=(10, 6))
produkty_na_kategorie.plot(kind="bar", color="skyblue")
plt.title("Liczba produktów w kategoriach")
plt.xlabel("Kategoria")
plt.ylabel("Liczba produktów")
plt.tight_layout()
plt.savefig("wykres_matplotlib.png")
plt.close()

# === KROK 4: Plotly – wykres pudełkowy cen wg kategorii ===

fig = px.box(df, x="Kategoria", y="Cena", color="Kategoria",
             title="Rozkład cen w kategoriach (Plotly)", points="all")
fig.write_html("plotly_wykres.html")

# === KROK 5: Zapis wyników analizy do CSV ===

plik_wynik_csv = "wyniki_analizy.csv"

with open(plik_wynik_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Metryka", "Wartość"])
    for k, v in produkty_na_kategorie.items():
        writer.writerow([f"Liczba produktów w kategorii: {k}", v])
    writer.writerow(["Średnia cena (Dostępne)", srednia_cena_dostepnych])
    writer.writerow(["Najdroższy produkt", najdrozszy["Nazwa"]])
    writer.writerow(["Cena najdroższego produktu", najdrozszy["Cena"]])
    writer.writerow(["Średnia cena (NumPy)", round(srednia_numpy, 2)])
    writer.writerow(["Mediana ceny", round(mediana_numpy, 2)])
    writer.writerow(["Min. cena", round(min_numpy, 2)])
    writer.writerow(["Max. cena", round(max_numpy, 2)])
    writer.writerow(["Odchylenie standardowe", round(std_numpy, 2)])

# === KROK 6: Zapis wyników do XML ===

plik_wynik_xml = "wyniki_analizy.xml"
root = ET.Element("analiza")

kat_elem = ET.SubElement(root, "produkty_na_kategorie")
for kat, liczba in produkty_na_kategorie.items():
    ET.SubElement(kat_elem, "kategoria", nazwa=kat).text = str(liczba)

ET.SubElement(root, "srednia_cena_dostepnych").text = str(srednia_cena_dostepnych)
ET.SubElement(root, "srednia_numpy").text = str(round(srednia_numpy, 2))
ET.SubElement(root, "mediana_numpy").text = str(round(mediana_numpy, 2))
ET.SubElement(root, "max_cena").text = str(round(max_numpy, 2))
ET.SubElement(root, "min_cena").text = str(round(min_numpy, 2))
ET.SubElement(root, "odchylenie_std").text = str(round(std_numpy, 2))

naj_elem = ET.SubElement(root, "najdrozszy_produkt")
ET.SubElement(naj_elem, "nazwa").text = najdrozszy["Nazwa"]
ET.SubElement(naj_elem, "cena").text = str(najdrozszy["Cena"])

ET.ElementTree(root).write(plik_wynik_xml, encoding="utf-8", xml_declaration=True)

print("✅ Wyniki zapisano do CSV, XML oraz wygenerowano wykresy.")
