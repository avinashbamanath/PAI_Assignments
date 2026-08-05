class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Holder Name   :", self.holder)
        print("Available Bal.:", self.__balance)


class SavingsAccount(Account):
    def __init__(self, holder, balance, interest):
        super().__init__(holder, balance)
        self.interest = interest

    def display(self):
        super().display()
        print("Interest      :", self.interest, "%")


class CurrentAccount(Account):
    def __init__(self, holder, balance, overdraft):
        super().__init__(holder, balance)
        self.overdraft = overdraft

    def display(self):
        super().display()
        print("Overdraft     :", self.overdraft)


print("----- Savings Account Details -----")
s1 = SavingsAccount("Rohan", 50000, 6.5)
s1.display()

print("\n----- Current Account Details -----")
c1 = CurrentAccount("Priya", 80000, 25000)
c1.display()

print("\nCurrent Savings Balance:", s1.get_balance())
