from Handler import read_file, write_file

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    book_data = f"{book_id},{title},{author}\n"
    write_file("books.txt", book_data)
    print("Book added successfully!")

def search_book():
    book_id = input("Enter Book ID: ")
    books = read_file("books.txt")
    for book in books:
        if book.startswith(book_id):
            book_id, title, author = book.strip().split(",")
            print("Book found!")
            print("Book ID:", book_id)
            print("Title:", title)
            print("Author:", author)
            return
    print("Book not found!")

def display_all_books():
    books = read_file("books.txt")
    if books:
        print("===== All Books =====")
        for book in books:
            book_id, title, author = book.strip().split(",")
            print("Book ID:", book_id)
            print("Title:", title)
            print("Author:", author)
            print("---------------------")
    else:
        print("No books available!")