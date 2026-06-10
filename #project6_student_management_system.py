# Project 6 - Student Management System

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        students.append(name)
        print("Student Added Successfully!")

    elif choice == "2":
        print("\nStudent List:")
        for student in students:
            print(student)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")