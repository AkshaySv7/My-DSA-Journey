class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.transactions = []  # Store history

    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def add_amount(self):
        if not self.verify_pin():
            print("Incorrect PIN.")
            return
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully.")
        else:
            print("Enter a valid amount.")

    def withdraw(self):
        if not self.verify_pin():
            print("Incorrect PIN.")
            return
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        if not self.verify_pin():
            print("Incorrect PIN.")
            return
        print(f"Current Balance: ₹{self.balance}")

    def show_transactions(self):
        if not self.verify_pin():
            print("Incorrect PIN.")
            return
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for t in self.transactions:
                print(" -", t)
def main():
    account = BankAccount("Akshay", 10000, "1234")

    while True:
        print("\n--- Welcome to the Bank ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account.add_amount()
        elif choice == "2":
            account.withdraw()
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.show_transactions()
        elif choice == "5":
            print("Thank you for using our bank system.")
            break
        else:
            print("Invalid choice. Try again.")
main()
