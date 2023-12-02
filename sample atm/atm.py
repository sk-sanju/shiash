balance = 0

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount}. New balance: ₹{balance}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{balance}")
    else:
        print("Insufficient funds!")

def check_balance():
    global balance
    print()
    print(f"Your balance is: ₹{balance}")

while True:
    print()
    print("===SANJU-ATM===")
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        withdraw(amount)
    elif choice == '3':
        check_balance()
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a correct option.")
