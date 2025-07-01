# framework.py

registry = {}  # 'nazwa_komendy': funkcja
descriptions = {}  # 'nazwa_komendy': opis

def command(name):
    """Podstawowy dekorator rejestrujący komendę."""
    def decorator(func):
        registry[name] = func
        return func
    return decorator

def command_with_description(name, description):
    """Dekorator rejestrujący komendę z opisem."""
    def decorator(func):
        registry[name] = func
        descriptions[name] = description
        return func
    return decorator

def list_commands():
    """Wyświetla dostępne komendy z opisami."""
    print("Dostępne komendy:")
    for name in sorted(registry):
        desc = descriptions.get(name, "(brak opisu)")
        print(f"  • {name:<12} – {desc}")

def run():
    """Główna pętla wykonująca komendę."""
    import sys
    if len(sys.argv) < 2:
        print("Użycie: python app.py <komenda>")
        list_commands()
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd in registry:
        registry[cmd](*args)
    else:
        print(f"Nieznana komenda: {cmd}")
        list_commands()
