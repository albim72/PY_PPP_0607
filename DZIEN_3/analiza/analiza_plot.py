import pandas as pd
import numpy as np
import csv
import random
import matplotlib.pyplot as plt
import plotly.express as px
import xml.etree.ElementTree as ET

# === KROK 1: Generowanie danych i zapis do CSV ===
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

print(f"✅ Plik {plik_csv} został wygenerowany.")

# === KROK 2: Wczytanie danych do DataFrame ===
df = pd.read_csv(plik_csv)

# === KROK 3: Analiza danych ===
produkty_na_kategorie = df["Kategoria"].value_counts()
ceny_dostepne = df[df["Dostępność"] == "Dostępny"]["Cena"].to_numpy()
srednia_cena_dostepnych = np.round(np.mean(ceny_dostepne), 2)
najdrozszy = df.loc[df["Cena"].idxmax()]
mediana_ceny = np.median(df["Cena"])
std_ceny = np.std(df["Cena"])

# === KROK 4: Wizualizacja danych ===

# Matplotlib – wykres słupkowy
plt.figure(figsize=(10, 6))
produkty_na_kategorie.plot(kind="bar", color="orange")
plt.title("Liczba produktów w każdej kategorii")
plt.xlabel("Kategoria")
plt.ylabel("Liczba produktów")
plt.tight_layout()
matplotlib_path = "wykres_matplotlib.png"
plt.savefig(matplotlib_path)
plt.close()

# Plotly – interaktywny wykres pudełkowy
fig = px.box(df, x="Kategoria", y="Cena", color="Kategoria",
             title="Rozkład cen w poszczególnych kategoriach")
plotly_path = "plotly_wykres.html"
fig.write_html(plotly_path)

# === KROK 5: Eksport wyników analizy do CSV (Pandas) ===
wyniki_df = pd.DataFrame([
    *[(f"Liczba produktów w kategorii: {kat}", liczba) for kat, liczba in produkty_na_kategorie.items()],
    ("Średnia cena dostępnych produktów", srednia_cena_dostepnych),
    ("Najdroższy produkt", najdrozszy["Nazwa"]),
    ("Cena najdroższego produktu", najdrozszy["Cena"]),
    ("Mediana ceny wszystkich produktów", round(mediana_ceny, 2)),
    ("Odchylenie standardowe cen", round(std_ceny, 2))
], columns=["Metryka", "Wartość"])

csv_result_path = "wyniki_pandas.csv"
wyniki_df.to_csv(csv_result_path, index=False)

print(f"✅ Wyniki zapisano do pliku CSV: {csv_result_path}")

# === KROK 6: Eksport wyników do XML (z użyciem Pandas i ElementTree) ===
xml_result_path = "wyniki_pandas.xml"
root = ET.Element("analiza")

for _, row in wyniki_df.iterrows():
    entry = ET.SubElement(root, "element")
    ET.SubElement(entry, "metryka").text = str(row["Metryka"])
    ET.SubElement(entry, "wartosc").text = str(row["Wartość"])

tree = ET.ElementTree(root)
tree.write(xml_result_path, encoding="utf-8", xml_declaration=True)

print(f"✅ Wyniki zapisano do pliku XML: {xml_result_path}")
print(f"📈 Wykresy zapisano jako: {matplotlib_path} oraz {plotly_path}")
