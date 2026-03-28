# Library Book Management System
# Module: book_manager.py
books = {}  # title -> {author, available, total}
def add_book(title, author, copies):
    """Add a new book or increase copies of an existing book."""
    if title in books:
        books[title]["available"] += copies
        books[title]["total"] += copies
    else:
        books[title] = {
            "author": author,
            "available": copies,
            "total": copies
        }
    return "Book added successfully."
  
def borrow_book(title):
    """Borrow a book if available."""
    if title in books and books[title]["available"] > 0:
        books[title]["available"] -= 1
        return "Book borrowed successfully."
    return "Book not available."

def return_book(title):
    """Return a previously borrowed book."""
    if title in books:
        books[title]["available"] += 1
        return "Book returned successfully."
    return "Book not found."

def list_books():
    """Return list of all books."""
    if not books:
        return ["No books available in the library."]
    result = []
    for title, info in books.items():
        result.append(
            f"{title} | {info['author']} | Available: {info['available']} | Total: {info['total']}"
        )
    return result

# Main App (main.py)
def main():
    print("Library Book Management System")

    while True:
        cmd = input("\nCommand (add / borrow / return / list / quit): ").strip().lower()

        if cmd == "add":
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()

            try:
                copies = int(input("Enter number of copies: "))
            except:
                print("Invalid number!")
                continue

            print(add_book(title, author, copies))

        elif cmd == "borrow":
            title = input("Enter title: ").strip()
            print(borrow_book(title))

        elif cmd == "return":
            title = input("Enter title: ").strip()
            print(return_book(title))

        elif cmd == "list":
            for line in list_books():
                print(line)

        elif cmd == "quit":
            print("Exiting system.")
            break

        else:
            print("Invalid command! Please try again.")
          
if name== "main":
    main()
