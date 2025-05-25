class Bank:
    bank_name = "Habib Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
print(b1.bank_name)
Bank.change_bank_name("Meezan Bank")
print(b2.bank_name)
