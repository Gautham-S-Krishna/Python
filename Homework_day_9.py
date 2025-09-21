class Account:
    def __init__ (self, account_holder_name: str, balance: float):
        self._account_holder_name = account_holder_name
        self._balance = balance
    def __add__(self, other):
        return self._balance + other._balance
    def show_output(self):
        print(f"Account Holder: {self._account_holder_name}, Balance: {self._balance}")
class SavingsAccount(Account):
    def __init__ (self, account_holder_name: str, balance: float, interest_rate: float):
        super().__init__(account_holder_name, balance)
        self._interest_rate = interest_rate
    def calculate_interest(self):
         f"Saving accounts interest: {self._balance * 0.05}"
class CurrentAccount(Account):
    def __init__ (self, account_holder_name: str, balance: float):
        super().__init__(account_holder_name, balance)
    def calculate_interest(self):
        return f"Current accounts interest: {self._balance * 0.02}"
savings_acc = SavingsAccount("Akshai", 1000.0, 0.05)
current_acc = CurrentAccount("Karthik", 2000.0)

print(savings_acc.show_output(), savings_acc.calculate_interest())
print(current_acc.show_output(), current_acc.calculate_interest())
print("Total Balance:", savings_acc + current_acc)

