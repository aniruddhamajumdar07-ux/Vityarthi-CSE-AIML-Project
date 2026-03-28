---
title: "Project Statement: Library Book Management System"
author: "Development Team"
date: "March 2026"
---

# Project Statement

## Library Book Management System

---

## 1. Project Overview

The **Library Book Management System** is a lightweight, command-line Python application designed to help library administrators manage their book inventory efficiently. The system allows staff to add books, track copy availability, process borrow and return transactions, and view the current state of the library catalogue — all through a simple, interactive terminal interface.

---

## 2. Objectives

The primary objectives of this project are:

- To provide a minimal yet functional tool for managing book records in a small library or classroom setting.
- To demonstrate clean separation of concerns by isolating business logic (`book_manager.py`) from the user interface (`main.py`).
- To create a reusable core module that can be extended or integrated into larger systems (e.g., a web or database-backed application).

---

## 3. Scope

### In Scope

- Adding new books and increasing copies of existing titles
- Borrowing available copies and returning borrowed books
- Listing all books with availability counts
- Basic input validation (non-numeric copy count handling)

### Out of Scope

- User authentication and per-user borrow tracking
- Persistent storage (data resets on exit)
- Fine/overdue management
- Graphical or web-based interface

---

## 4. System Design

### Module: `book_manager.py`

This module contains all core library functions and maintains an in-memory dictionary (`books`) as the data store. It exposes four public functions:

| Function | Description |
|---|---|
| `add_book(title, author, copies)` | Adds a new book or increments copies |
| `borrow_book(title)` | Decrements available count if copies exist |
| `return_book(title)` | Increments available count for a known title |
| `list_books()` | Returns formatted strings for all books |

### Module: `main.py`

Acts as the application entry point. It runs an interactive loop, reads user commands from standard input, delegates to `book_manager`, and prints results. Commands supported: `add`, `borrow`, `return`, `list`, `quit`.

---

## 5. Data Model

Each book is stored as a dictionary entry with the following fields:

| Field | Type | Description |
|---|---|---|
| `author` | `str` | Name of the book's author |
| `available` | `int` | Number of copies currently available |
| `total` | `int` | Total copies ever added |

Books are keyed by their **title** (case-sensitive string).

---

## 6. Known Limitations

- **No persistence**: All data is lost when the program exits. A future version should write to a JSON file or SQLite database.
- **Case-sensitive titles**: "gatsby" and "Gatsby" are treated as separate books. Input normalization should be added.
- **No borrow history**: The system does not track which user borrowed which book or when it is due.
- **Single-user mode**: Designed for one operator at a time; no concurrency support.

---

## 7. Future Enhancements

1. **Data persistence** via JSON or SQLite storage
2. **Search functionality** by author or keyword
3. **User accounts** with individual borrow history
4. **Due date tracking** with overdue notifications
5. **REST API** or web frontend for remote access

---

## 8. Conclusion

The Library Book Management System meets its core objective: a clean, functional, easily extensible Python application for basic library operations. Its modular structure makes it straightforward to build upon, whether adding a database layer, a web interface, or additional business rules.
