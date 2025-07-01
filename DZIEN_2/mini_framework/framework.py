registry = {}

#rejest będzie miał 2 elementy:
#1. nazwa komendy
#2. funkcja związana z komendą
#to jest podstawowy mechanizm tzw.rejestru (registry pattern)

#to jest dekorator
def command(name):
    """funkcja dekoratora - rejstrująca funkcję jako komendę frameworku"""
    def decorator(func):
        registry[name] = func
        return func
    return decorator

def run():
    """Uruchamia framework: wybiera i wywołuje komendę"""
    import sys
    if len(sys.argv) < 2:
        print("usage: python -m pip <command>")
        print("available commands:", ", ".join(registry.keys()))
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd in registry:
        registry[cmd](*args)
    else:
        print(f"unknown command: {cmd}")

