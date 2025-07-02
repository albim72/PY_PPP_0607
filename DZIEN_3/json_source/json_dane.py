import json

# Wczytaj dane
with open("uzytkownicy_duzy.json", encoding="utf-8") as f:
    users = json.load(f)

# 1. Ilu aktywnych?
aktywni = [u for u in users if u["aktywny"]]
print("Liczba aktywnych użytkowników:", len(aktywni))

# 2. Średni wiek aktywnych
if aktywni:
    sredni_wiek = sum(u["wiek"] for u in aktywni) / len(aktywni)
    print("Średni wiek aktywnych:", round(sredni_wiek, 2))

# 3. Najwięcej punktów
top_user = max(users, key=lambda u: u["punkty"])
print(f"Najlepszy użytkownik: {top_user['imie']} {top_user['nazwisko']} ({top_user['punkty']} pkt)")

# 4. Top 10 użytkowników
top10 = sorted(users, key=lambda u: u["punkty"], reverse=True)[:10]

# Zapisz do pliku JSON
with open("top10.json", "w", encoding="utf-8") as f:
    json.dump(top10, f, indent=2, ensure_ascii=False)

print("Zapisano top 10 użytkowników do pliku top10.json")
