class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self.balance += amount
        print(f"Successfully deposited {amount:.2f}.")
        print(f"New balance: {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        print(f"Successfully withdrawn {amount:.2f}.")
        print(f"Remaining balance: {self.balance:.2f}")

    def get_balance(self):
        return self.balance


# Create an account
account = Account("Yisehak Gebeyehu", "100001", 1000)

# Display account information
print("Owner:", account.owner)
print("Account Number:", account.account_number)
print("Initial Balance:", account.get_balance())

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Check balance
print(f"Current Balance: {account.get_balance():.2f}")

# Test invalid transactions
account.deposit(-100)
account.withdraw(-50)
account.withdraw(5000)