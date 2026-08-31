# ---------------- BOOK CLASS ----------------

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
        self.member_id = None

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"ID: {self.book_id} | Title: {self.title} | "
              f"Author: {self.author} | Status: {status}")


# ---------------- MEMBER CLASS ----------------

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.issued_books = []

    def display(self):
        print(f"ID: {self.member_id} | Name: {self.name}")
        print(f"Issued Books: {self.issued_books}")


# ---------------- LIBRARY CLASS ----------------

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID: ")

        # Check whether Book ID already exists
        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print("Book Added Successfully!")

    # View Books
    def view_books(self):
        if not self.books:
            print("No Books Found!")
        else:
            print("\n----- BOOK LIST -----")
            for book in self.books:
                book.display()

    # Search Book
    def search_book(self):
        search = input("Enter Book ID or Title: ").lower()

        found = False

        for book in self.books:
            if book.book_id.lower() == search or search in book.title.lower():
                book.display()
                found = True

        if not found:
            print("Book Not Found!")

    # Delete Book
    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")

        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    print("Cannot delete an issued book!")
                    return

                self.books.remove(book)
                print("Book Deleted Successfully!")
                return

        print("Book Not Found!")

    # Add Member
    def add_member(self):
        member_id = input("Enter Member ID: ")

        # Check whether Member ID already exists
        for member in self.members:
            if member.member_id == member_id:
                print("Member ID already exists!")
                return

        name = input("Enter Member Name: ")

        new_member = Member(member_id, name)
        self.members.append(new_member)
        print("Member Registered Successfully!")

    # View Members
    def view_members(self):
        if not self.members:
            print("No Members Found!")
        else:
            print("\n----- MEMBER LIST -----")
            for member in self.members:
                member.display()

    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        book = None
        member = None

        # Find Book
        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        # Find Member
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if book is None:
            print("Book Not Found!")

        elif member is None:
            print("Member Not Found!")

        elif not book.available:
            print("Book is Already Issued!")

        else:
            book.available = False
            book.member_id = member_id
            member.issued_books.append(book_id)

            print("Book Issued Successfully!")

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:

                if book.available:
                    print("This Book is Already Available!")
                    return

                # Enter delayed days manually
                delayed_days = int(input("Enter Number of Delayed Days: "))

                # Fine calculation: ₹5 per day
                fine = delayed_days * 5

                # Remove book from member's issued books
                for member in self.members:
                    if member.member_id == book.member_id:
                        member.issued_books.remove(book_id)
                        break

                # Update book status
                book.available = True
                book.member_id = None

                print("Book Returned Successfully!")
                print(f"Delayed Days: {delayed_days}")
                print(f"Fine Amount: ₹{fine}")
                return

        print("Book Not Found!")

    # View Issued Books
    def view_issued_books(self):
        found = False

        print("\n----- ISSUED BOOKS -----")

        for book in self.books:
            if not book.available:
                print(f"Book: {book.title} | Issued to Member ID: {book.member_id}")
                found = True

        if not found:
            print("No Books are Currently Issued!")


# ---------------- MAIN PROGRAM ----------------

library = Library()

# Pre-added books
library.books.append(Book("B101", "Python Programming", "Guido van Rossum"))
library.books.append(Book("B102", "Java Programming", "Herbert Schildt"))
library.books.append(Book("B103", "Data Structures", "Mark Allen Weiss"))
library.books.append(Book("B104", "Web Development", "Jon Duckett"))
library.books.append(Book("B105", "Database Management", "Raghu Ramakrishnan"))

# Pre-added members
library.members.append(Member("M101", "Durga"))
library.members.append(Member("M102", "Anjali"))


# ---------------- MENU ----------------

while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Register Member")
    print("6. View Members")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. View Issued Books")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.delete_book()

    elif choice == "5":
        library.add_member()

    elif choice == "6":
        library.view_members()

    elif choice == "7":
        library.issue_book()

    elif choice == "8":
        library.return_book()

    elif choice == "9":
        library.view_issued_books()

    elif choice == "10":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid Choice! Please enter a number from 1 to 10.")
