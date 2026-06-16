# Project 10 - Expense Tracker

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense Added!")

    elif choice == "2":
        print("Expenses:", expenses)

    elif choice == "3":
        print("Total Expense =", sum(expenses))

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")