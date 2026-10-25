
class BankAccount:

    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance = self.balance + amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance = self.balance - amount
            return amount

    def check_balance(self):
        print("Current Balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)

account1 = BankAccount("123456789", 15000, "26-10-2026", "John Kamau")

print("CUSTOMER DETAILS")
account1.customer_details()

print("----------------------")
print("Amount Deposited:", account1.deposit(5000))
print("Amount Withdrawn:", account1.withdraw(3000))
account1.check_balance()
