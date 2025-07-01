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


