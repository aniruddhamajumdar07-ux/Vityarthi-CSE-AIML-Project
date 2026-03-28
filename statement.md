# Project Statement: Library Book Management System

## What This Project Is

This is a simple Python program that helps manage books in a library. You can add books, see how many copies you have, borrow them, and return them. Everything runs in the terminal so you don't need any special software to use it.

---

## Why I Made This

The goal was to build something that solves a real problem in a simple way. Libraries need to track books and copies and who has what. This program handles that in a lightweight way without needing a database or internet connection or anything complicated.

---

## What the Program Does

- You can add a book by entering the title, author, and how many copies you have.
- If a book already exists it just adds more copies instead of making a duplicate.
- You can borrow a book and the program will check if there are copies available.
- You can return a book and it will update the count.
- You can list all the books to see what is in the library and how many copies are left.

---

## How It Is Built

The project is split into two files.

**book_manager.py** is where all the logic lives. It stores the books in a dictionary and has functions for adding, borrowing, returning, and listing books. This part doesn't deal with the user at all. It just does the work.

**main.py** is where the program starts. It shows the menu, reads what the user types, and calls the right function from book_manager. It also handles mistakes like if someone types a word instead of a number for copies.

Keeping them separate means if you ever want to change how the program looks or add a web interface you don't have to touch the logic.

---

## What It Can't Do Yet

- The data doesn't save. When you close the program everything is gone.
- It doesn't know who borrowed which book. It just tracks the count.
- The title has to match exactly. "gatsby" and "Gatsby" are treated as different books.
- Only one person can use it at a time.

---

## What Could Be Added Later

- Saving to a file or database so the data stays after you close it.
- User accounts so you can track who borrowed what.
- A search feature so you can look up books by author or keyword.
- Due dates and reminders for overdue books.

---

## How to Run It

You need Python 3.6 or higher. No extra libraries needed. Just run:

```bash
python main.py
```

---

## Summary

This project is a working example of how to build a small command line tool in Python. The code is clean and split up properly so it is easy to read and easy to build on later.
