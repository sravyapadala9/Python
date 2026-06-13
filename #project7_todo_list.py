# Project 7 - To Do List

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for task in tasks:
            print("-", task)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")