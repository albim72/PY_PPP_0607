from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Doładowanie {amount:.2f} złotych na Credit Card")

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Opłata {amount:.2f} złotych via PayPal")

def process_payment(method:PaymentMethod, amount):
    print("Pocessing payment...")
    method.pay(amount)
    print("Payment processed. Done")

if __name__ == '__main__':
    card = CreditCardPayment()
    paypal = PayPalPayment()

    process_payment(card, 100)
    process_payment(paypal, 200)


