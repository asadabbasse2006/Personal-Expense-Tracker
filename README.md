# Personal Expense Tracker
#### Video Demo:  <[https://youtu.be/your-demo-video-url-here](https://youtu.be/5SdadgNaNjs)>
#### Description:
The **Personal Expense Tracker** is a lightweight, beginner-friendly command-line application written in Python that helps users record, view, and summarize personal expenses. It stores data locally in a JSON file (`data.json`) and provides features for adding new expense entries (amount, category, optional notes), viewing all expenses or filtered lists by category, and calculating totals either overall or per category.

This README documents the project's structure, how to install and run the application, testing instructions, and design choices made during development.

---

## Features
- Add expenses with: amount, category, notes (optional), and auto-generated date.
- View all expenses or filter by category (case-insensitive).
- Calculate total spending overall or for a specific category.
- Store all data in a local JSON file; no external database required.
- Input validation to prevent invalid amounts and missing categories.

---

## Project Structure
```
project/
│
├── project.py                # Main CLI application
├── test_project.py           # Unit tests for the application
├── data.json                 # Sample / runtime data file (created at runtime)
└── README.md                 # This file
```

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/asadabbasse2006/Personal-Expense-Tracker.git
cd Personal-Expense-Tracker
```

2. Ensure Python 3.x is installed:
```bash
python3 --version
```

3. No external dependencies are required. The application uses only Python's standard library.

---

## Usage
Run the application from the project directory:
```bash
python3 project.py
```

You will see the menu:
```
====== Personal Expense Tracker ======

1. Add Expense
2. View Expenses
3. Total Spent
4. Exit
```

### Add Expense
The program prompts for:
- Amount (float, > 0)
- Category (string)
- Notes (optional)

### View Expenses
- Displays all saved expenses or prompts for a category to filter by.

### Total Spent
- Calculates total spending across all records or for a specified category.

---

## Data Storage
By default the app stores records in `data.json` with entries like:
```json
{
    "amount": 15.99,
    "category": "food",
    "notes": "Lunch",
    "date": "2025-01-01"
}
```

---

## Running Tests
From the project directory:
```bash
python -m unittest test_project.py
```
Or run test discovery:
```bash
python -m unittest discover
```

---

## Error Handling & Validation
- Amounts must be numeric and greater than 0.
- Categories must be non-empty strings.
- The app provides user-friendly error messages and prevents invalid saves.

---

## Design Choices & Notes
- Chose JSON for simplicity and portability; it suits small personal projects and classroom assignments.
- CLI chosen for minimal dependencies and easy grading in academic settings.
- The code is organized to be easy-to-read and extend (e.g., adding CSV export or GUI later).

---

## Future Improvements
- Edit / delete expense entries.
- Monthly and yearly summaries and visualizations.
- CSV/Excel export.
- A web or mobile frontend.
- Protect the data file with optional encryption.

---

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes and push.
4. Open a pull request for review.

---

## License
This project is released under the MIT License.

---

## Author
**Asad Abbas**  
GitHub: https://github.com/asadabbasse2006

---

## Submission (for CS50 / course instructions)
Place this `README.md` and all project files in your `~/project` folder.  
Ensure your `project.py` runs and that `README.md` contains the video demo URL before executing:
```bash
submit50 cs50/problems/2025/x/expense-tracker
```
(Replace with the appropriate submit50 identifier if different.)

