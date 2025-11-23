# 💰 Personal Expense Tracker

A simple, lightweight, command-line **Personal Expense Tracker** written
in Python.
Track expenses, filter by category, and calculate totals --- all stored
locally in a JSON file.

------------------------------------------------------------------------

## 📑 Table of Contents

-   [Introduction](#-introduction)
-   [Features](#-features)
-   [Demo](#-demo)
-   [Project Structure](#-project-structure)
-   [Installation](#️-installation)
-   [Usage](#-usage)
-   [Configuration](#-configuration)
-   [Data Storage](#-data-storage)
-   [Running Tests](#-running-tests)
-   [Error Handling](#-error-handling)
-   [Future Improvements](#-future-improvements)
-   [Contributing](#-contributing)
-   [License](#️-license)
-   [Author](#-author)

------------------------------------------------------------------------

## 📝 Introduction

This project provides a clean and simple command-line tool for tracking
personal expenses.
Add expense entries, categorize them, filter them, and calculate total
spending instantly.

All data is stored in a local JSON file (`data.json`), so no external
database or dependencies are required.

------------------------------------------------------------------------

## ✨ Features

-   ➕ Add expenses with amount, category, notes, and auto-generated
    date
-   📄 View all expenses or filter by category
-   📊 Calculate total spending (overall or per category)
-   💾 Local JSON storage
-   🔍 Case-insensitive category matching
-   🧱 Clean, beginner-friendly Python code
-   🛡 Built-in validation to prevent invalid inputs

------------------------------------------------------------------------

## 🎥 Demo

    ====== Personal Expense Tracker ======

    1. Add Expense
    2. View Expenses
    3. Total Spent
    4. Exit

------------------------------------------------------------------------

## 📁 Project Structure

    project/
    │
    ├── project.py
    ├── test_project.py
    ├── data.json
    └── README.md

------------------------------------------------------------------------

## 🛠️ Installation

### 1. Clone the repository

``` bash
git clone https://github.com/asadabbasse2006/Personal-Expense-Tracker.git
cd expense-tracker
```

### 2. Make sure Python is installed

``` bash
python3 --version
```

### 3. Dependencies

No third-party libraries required.

------------------------------------------------------------------------

## ▶️ Usage

Run the program:

``` bash
python3 project.py
```

You will see:

    ====== Personal Expense Tracker ======

    1. Add Expense
    2. View Expenses
    3. Total Spent
    4. Exit

### Menu Overview

#### **1. Add Expense**

Prompt for: - Amount
- Category
- Notes (optional)

#### **2. View Expenses**

Display: - All expenses
- Or filtered by category

#### **3. Total Spent**

Get: - Total of all expenses
- Or category-specific total

#### **4. Exit**

Quit the application.

------------------------------------------------------------------------

## 🔧 Configuration

``` python
DATA_FILE = "data.json"
```

------------------------------------------------------------------------

## 💾 Data Storage

``` json
{
    "amount": 15.99,
    "category": "food",
    "notes": "Lunch",
    "date": "2025-01-01"
}
```

------------------------------------------------------------------------

## 🧪 Running Tests

``` bash
python -m unittest test_expense_tracker.py
```

Or:

``` bash
python -m unittest discover
```

------------------------------------------------------------------------

## 🛠 Error Handling

The application includes validation for invalid inputs, such as amounts
≤ 0 or missing categories.

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Edit/delete expense entries
-   Monthly/yearly summary reports
-   CSV/Excel export
-   Web or mobile interface
-   Dashboard analytics
-   Data encryption

------------------------------------------------------------------------

## 🤝 Contributing

1.  Fork the repo
2.  Create a new branch
3.  Commit changes
4.  Open a pull request

------------------------------------------------------------------------

## ©️ License

MIT License.

------------------------------------------------------------------------

## 👤 Author

**Asad Abbas**
GitHub: https://github.com/asadabbasse2006
