# Library Book Management System

This is a program that helps manage library books. You can add books track how many copies you have borrow books and return them.

## Project Structure

```
library/
├── book_manager.py   # This is where the main library logic is (add, borrow, return, list)
├── main.py           # This is where the program starts
└── README.md         # This file
```

## Features

* Add Books. You can add a book or get more copies of one you already have.
* Borrow Books. If there are copies you can borrow a book.
* Return Books. You can return a book you borrowed.
* List Books. You can see all the books and how many are available.

## Requirements

* You need Python 3.6 or higher.
* You don't need any libraries.

## Getting Started

**1. Get the project.**

You can clone it. Download it from

```bash
git clone https://github.com/your-username/library-book-manager.git
cd library-book-manager
```

**2. Run the program.**

```bash
python main.py
```

## Usage

When you start the program you'll see a menu. You can choose what to do.

```
Library Book Management System

What do you want to do? (add / borrow / return / list / quit):
```

## Commands

| Command | Description |
|---------|-------------|
| `add` | Add a book or get more copies of one you have. |
| `borrow` | Take a book if there are copies |
| `return` | Give back a book you borrowed. |
| `list` | See all the books and how many are available. |
| `quit` | Stop using the program. |

## Example Session

```
What do you want to do? add
Enter the title: The Great Gatsby
Enter the author: F. Scott Fitzgerald
Enter the number of copies: 3
The book was added.

What do you want to do? list
The Great Gatsby | F. Scott Fitzgerald | Available: 3 Total: 3

What do you want to do? borrow
Enter the title: The Great Gatsby
The book was borrowed.

What do you want to do? list
The Great Gatsby | F. Scott Fitzgerald | Available: 2 Total: 3
```

## Notes

* The book information is stored in the computers memory. So when you stop the program all the information will be gone.
* The program treats "gatsby" and "Gatsby" as books.
* When you return a book it makes more copies available.. It doesn't keep track of who borrowed it.

## Future Improvements

* Save the data to a file or database (like JSON or SQLite).
* Add user accounts. Track what books each user borrowed.
* Let users search for books by author or keyword.
* Add dates and alerts for overdue books.
