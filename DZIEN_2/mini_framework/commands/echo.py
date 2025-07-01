from framework import command_with_description

@command_with_description("echo", "Powtarza podany tekst")
def echo(*args):
    print(" ".join(args))
