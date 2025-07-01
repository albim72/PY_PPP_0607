# Listy samochodów
toyota = ["Corolla", "Yaris", "Camry", "Corolla", "Avensis"]
ford = ["Focus", "Mondeo", "Fiesta", "Focus", "Kuga"]
bmw = ["320i", "X3", "320i", "X5", "i3"]

# 1. Zbiór wszystkich unikalnych modeli dostępnych w komisie
wszystkie_modele = set(toyota + ford + bmw)
print("Unikalne modele:", wszystkie_modele)

# 2. Modele powtarzające się w więcej niż jednej marce
toyota_set = set(toyota)
ford_set = set(ford)
bmw_set = set(bmw)

powtarzajace_sie = (toyota_set & ford_set) | (toyota_set & bmw_set) | (ford_set & bmw_set)
print("Modele w więcej niż jednej marce:", powtarzajace_sie)

# 3. Liczba unikalnych modeli dla każdej marki (słownik)
liczba_modeli = {
    "Toyota": len(toyota_set),
    "Ford": len(ford_set),
    "BMW": len(bmw_set)
}
print("Liczba unikalnych modeli każdej marki:", liczba_modeli)

# 4. Marka z największą liczbą modeli
max_marka = max(liczba_modeli, key=liczba_modeli.get)
print("Marka z największą liczbą modeli:", max_marka)
if max_marka == "Toyota":
    print("Modele:", toyota_set)
elif max_marka == "Ford":
    print("Modele:", ford_set)
else:
    print("Modele:", bmw_set)


___________________________________________________________________________

# Lista słowników samochodów
samochody = [
    {"marka": "Toyota", "model": "Corolla", "rok": 2018, "przebieg": 67000},
    {"marka": "Ford", "model": "Focus", "rok": 2020, "przebieg": 40000},
    {"marka": "BMW", "model": "X3", "rok": 2017, "przebieg": 90000},
    {"marka": "Toyota", "model": "Yaris", "rok": 2019, "przebieg": 35000},
    {"marka": "Ford", "model": "Fiesta", "rok": 2016, "przebieg": 110000}
]

# 1. Funkcja zwracająca średni przebieg
def sredni_przebieg(samochody):
    suma = sum(samochod["przebieg"] for samochod in samochody)
    return suma / len(samochody)

# 2. Funkcja zwracająca najmłodszy samochód (słownik)
def najmlodszy_samochod(samochody):
    return max(samochody, key=lambda x: x["rok"])

# 3. Funkcja zwracająca modele danej marki
def samochody_marki(samochody, marka):
    return [s["model"] for s in samochody if s["marka"].lower() == marka.lower()]

# Wywołania funkcji i prezentacja wyników
print("Średni przebieg:", sredni_przebieg(samochody))
print("Najmłodszy samochód:", najmlodszy_samochod(samochody))
print("Modele Toyoty:", samochody_marki(samochody, "Toyota"))
print("Modele Forda:", samochody_marki(samochody, "Ford"))
print("Modele BMW:", samochody_marki(samochody, "BMW"))


