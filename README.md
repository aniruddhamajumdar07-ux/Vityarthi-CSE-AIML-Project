# Library Book Management System

A simple command-line application for managing library books — add titles, track copies, borrow, and return books with ease.

---

## Project Structure

```
library/
├── book_manager.py   # Core library logic (add, borrow, return, list)
├── main.py           # CLI entry point
└── README.md         # This file
```

---

## Features

- **Add Books** — Add new titles or increase copies of existing ones
- **Borrow Books** — Check out a book if copies are available
- **Return Books** — Return a previously borrowed book
- **List Books** — View all books with availability status

---

## Requirements

- Python 3.6 or higher
- No external dependencies

---

## Getting Started

### 1. Clone or download the project

```bash
git clone https://github.com/your-username/library-book-manager.git
cd library-book-manager
```

### 2. Run the application

```bash
python main.py
```

---

## Usage

Once running, you'll be prompted with a command menu:

```
Library Book Management System

Command (add / borrow / return / list / quit):
```

### Commands

| Command  | Description                              |
|----------|------------------------------------------|
| `add`    | Add a new book or increase its copies    |
| `borrow` | Borrow an available copy of a book       |
| `return` | Return a previously borrowed book        |
| `list`   | Display all books and their availability |
| `quit`   | Exit the application                     |

### Example Session

```
Command: add
Enter title: The Great Gatsby
Enter author: F. Scott Fitzgerald
Enter number of copies: 3
Book added successfully.

Command: list
The Great Gatsby | F. Scott Fitzgerald | Available: 3 | Total: 3

Command: borrow
Enter title: The Great Gatsby
Book borrowed successfully.

Command: list
The Great Gatsby | F. Scott Fitzgerald | Available: 2 | Total: 3
```

---

## Notes

- Book data is stored **in-memory** and will reset when the application exits.
- Book titles are **case-sensitive** — `"gatsby"` and `"Gatsby"` are treated as different books.
- Returning a book increments the available count; no borrow-tracking per user.

---

## Future Improvements

- Persist data to a file or database (JSON / SQLite)
- Add user accounts and per-user borrow history
- Search books by author or keyword
- Due date tracking and overdue alerts

---

## License

This project is open source and available under the [MIT License](LICENSE).
