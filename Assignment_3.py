from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} completed via Credit Card.")

class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} completed via Debit Card.")

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} completed via UPI.")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)

amount = float(input("Enter the total amount to be paid: "))

print("\nSelect a Payment Option")
print("1 -> Credit Card")
print("2 -> Debit Card")
print("3 -> UPI")

choice = int(input("Choose an option (1-3): "))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = DebitCardPayment()
elif choice == 3:
    strategy = UPIPayment()
else:
    print("Please enter a valid option.")
    exit()

processor = PaymentProcessor(strategy)
processor.make_payment(amount)
