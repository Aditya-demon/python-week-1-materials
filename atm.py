
# Simple ATM Simulator
# Mini Project - Week 1

correct_pin = "1234"
balance = 5000.0


def login():
    attempts = 3

    while attempts > 0:
        pin = input("Enter your 4-digit ATM PIN: ")

        if pin == correct_pin:
            print("\nLogin successful!")
            return True
        else:
            attempts -= 1
            print("Incorrect PIN. Attempts left:", attempts)

    print("Your session has ended.")
    return False


def check_balance():
    print(f"\nYour current balance is: Rs. {balance:.2f}")


def deposit():
    global balance

    try:
        amount = float(input("Enter amount to deposit: Rs. "))

        if amount > 0:
            balance += amount
            print("Deposit successful!")
            check_balance()
        else:
            print("Amount must be greater than zero.")

    except ValueError:
        print("Please enter a valid number.")


def withdraw():
    global balance

    try:
        amount = float(input("Enter amount to withdraw: Rs. "))

        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("Withdrawal successful!")
            check_balance()

    except ValueError:
        print("Please enter a valid number.")


def atm_menu():
    while True:
        print("\n===== SIMPLE ATM SIMULATOR =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


def main():
    print("Welcome to the ATM Simulator!")

    if login():
        atm_menu()


if __name__ == "__main__":
    main()
