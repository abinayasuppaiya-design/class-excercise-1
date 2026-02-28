class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited Successfully!")
        else:
            print("Invalid Deposit Amount!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Main Program
print("===== Welcome to Simple Banking System =====")

name = input("Enter Account Holder Name: ")
acc_no = input("Enter Account Number: ")
account = BankAccount(name, acc_no)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == '3':
        account.check_balance()

    elif choice == '4':
        print("Thank you for using Banking System!")
        break

    else:
        print("Invalid Choice! Please try again.")
