accounts = [
    {'name': 'RAGAA', 'pin': '5050', 'balance': 100000},
    {'name': 'JODY', 'pin': '2323', 'balance': 200000},
    {'name': 'HAMODY', 'pin': '7575', 'balance': 300000},
]

def check_pin():
    attempts = 0
    while attempts < 3:
        pin = input("Enter your PIN: ")
        for account in accounts:
            if account['pin'] == pin:
                return account
        print("Invalid PIN.")
        attempts += 1
    print("Too many attempts. Your account is now locked.")
    return None

def check_balance(account):
    print(f"Your current balance is ${account['balance']}")

def deposit(account):
    amount = int(input("Enter amount to deposit: "))
    account['balance'] += amount
    print(f"Successfully deposited ${amount}. Your new balance is ${account['balance']}")

def withdraw(account):
    amount = int(input("Enter amount to withdraw: "))
    if amount > account['balance']:
        print("Insufficient funds.")
    else:
        account['balance'] -= amount
        print(f"Successfully withdrawn ${amount}. Your new balance is ${account['balance']}")

account = check_pin()
if account:
    print(f"Welcome, {account['name']}.")
    while True:
        print("What would you like to do?")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")