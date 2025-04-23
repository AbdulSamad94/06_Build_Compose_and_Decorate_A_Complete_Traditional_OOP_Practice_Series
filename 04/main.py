class Bank:
    bank_name = "Bank of Python"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name changed to {cls.bank_name}")


bank_name = Bank.bank_name
print(f"Initial bank name: {bank_name}")

Bank.change_bank_name("Bank of Java")
bank_name = Bank.bank_name
print(f"Updated bank name: {bank_name}")
