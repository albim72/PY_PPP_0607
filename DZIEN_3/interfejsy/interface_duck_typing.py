class Printer:
    def print_document(self, content):
        print(f"Dziękuję: {content}")

class Logger:
    def print_document(self, content):
        print(f"Zapisuję do loga: {content}")

def use_printer(device):
    device.print_document("mamy czas rozwoju koncepcji AI")


printer = Printer()
logger = Logger()
use_printer(printer)
use_printer(logger)
