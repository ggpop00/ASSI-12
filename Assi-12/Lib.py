from Book import add_book, search_book, display_all_books
from Member import add_member, search_member, display_all_members
from Borrow import borrow_book, return_book, display_borrowed_books

def display_menu():
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Display All Books")
    print("4. Add Member")
    print("5. Search Member")
    print("6. Display All Members")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Display Borrowed Books")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            display_all_books()
        elif choice == "4":
            add_member()
        elif choice == "5":
            search_member()
        elif choice == "6":
            display_all_members()
        elif choice == "7":
            borrow_book()
        elif choice == "8":
            return_book()
        elif choice == "9":
            display_borrowed_books()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


main()