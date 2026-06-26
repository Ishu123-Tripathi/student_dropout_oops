from manager import StudentManager

manager = StudentManager()

while True:

    print("\n====== Student Dropout Management ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Mark Dropout")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        manager.search_student()

    elif choice == "4":
        manager.mark_dropout()

    elif choice == "5":
        manager.delete_student()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")