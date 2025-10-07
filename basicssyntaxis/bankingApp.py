class BankAccount:
    def __init__(self, owner, balance=1000):
        self.owner = owner
        self.balance = balance
        print(f"🏦 Account created for {self.owner} with balance ${self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"✅ You deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"💵 You withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("❌ Not enough balance.")

    def check_balance(self):
        print(f"💰 Current balance: ${self.balance}")

    def run(self):
        """Main menu loop."""
        while True:
            print("\n=== Banking System ===")
            print("1 > Deposit")
            print("2 > Withdraw")
            print("3 > Check Balance")
            print("4 > Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("⚠️ Invalid input, please enter a number.")
                continue

            if choice == 1:
                amount = int(input("Enter the amount to deposit: "))
                self.deposit(amount)

            elif choice == 2:
                amount = int(input("Enter the amount to withdraw: "))
                self.withdraw(amount)

            elif choice == 3:
                self.check_balance()

            elif choice == 4:
                print("👋 Thank you for using our banking system!")
                break

            else:
                print("⚠️ Invalid option, please try again.")



# Create an account
account1 = BankAccount("Cesar")

# Start interactive menu
account1.run()
