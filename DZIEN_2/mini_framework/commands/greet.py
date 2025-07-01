from framework import command

@command("greet")
def greet(name="stranger"):
    print(f"Hello, {name}!")
