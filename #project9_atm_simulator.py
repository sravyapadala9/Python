# Project 9 - ATM Simulator

balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Balance =", balance)

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit Successful!")

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")