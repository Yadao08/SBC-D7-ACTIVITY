import random  # Import the random module

class my_bank:
    def __init__(bank_acc, id, balance=0):
        bank_acc.id, bank_acc.balance = id, balance

    def deposit(bank_acc, amount):
        bank_acc.balance += amount
        return f"Deposit successful. New balance is {bank_acc.balance}"

    def withdraw(bank_acc, amount):
        bank_acc.balance -= amount
        return f"Withdrawal successful. New balance is {bank_acc.balance}"

class Bank:
    def __init__(bank_acc):
        bank_acc.accounts = {}

    def generate_id(bank_acc):
        id = str(random.randint(10, 20))
        while id in bank_acc.accounts:
            id = str(random.randint(10, 20))
        return id
    def create_account(bank_acc, initial_balance=100):
        id = bank_acc.generate_id()
        bank_acc.accounts[id] = initial_balance
        return f"Account created. User ID: {id}, Balance: {initial_balance}"

    def delete_account(bank_acc, id):
        if id in bank_acc.accounts:
            del bank_acc.accounts[id]
            return f"Account deleted successfully!"
        return "Account not found."

def create_account(bank):
    initial_balance = int(input("Enter initial balance: "))
    if initial_balance < 100:
        print("Initial balance must be at least 100.")
    else:
        print(bank.create_account(initial_balance))

def log_in(bank):
    id = input("Enter User ID: ")
    if id in bank.accounts:
        account_menu(bank, id)
    else:
        print("Account not found.")

def main():
    bank = Bank()
    while True:
        print("\n1. Create Account \n2. Log In\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_account(bank)
        elif choice == '2':
            log_in(bank)
        elif choice == '3':
            print("Thank You for Using!")
            break
        else:
            print("Invalid choice.")

def account_menu(bank, acc_id):
    account = my_bank(acc_id, bank.accounts[acc_id])
    while True:
        print(f"\nUser ID: {account.id}\nCurrent Balance: {account.balance}")
        print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Delete Account\n5. Log Out")
        choice = input("Choose an option: ")

        if choice == '1':
            print(f"Current Balance: {account.balance}")
        elif choice == '2':
            amount = int(input("Enter deposit amount: "))
            print(account.deposit(amount))
        elif choice == '3':
            amount = int(input("Enter withdrawal amount: "))
            print(account.withdraw(amount))
        elif choice == '4':
            confirm = input("Delete account? (y/n): ").lower()
            if confirm == 'yes':
                print(bank.delete_account(account.id))
                break
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
