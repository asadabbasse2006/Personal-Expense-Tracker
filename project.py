import json
from datetime import date

DATA_FILE = "data.json"

def main():
    load_data()
    while True:
        print("\n====== Personal Expense Tracker ======\n")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            notes = input("Notes (Optional): ")
            add_expense(amount, category, notes)
            print("Expense added.")

        elif choice == 2:
            category = input("Filter by category (Press Enter for all): ")
            expenses_list = list_expenses(category if category else None)

            if not expenses_list:
                print("Your expense list is empty!")
            else:
                for e in expenses_list:
                    print(f"{e['date']} - {e['amount']} - {e['category']} - {e['notes']}")

        elif choice == 3:
            category = input("Category total (Press Enter for all): ")
            total = calculate_total(category if category else None)
            print(f"Total spent: {total}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


def load_data():
    global expenses
    try:
        with open(DATA_FILE, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []


def add_expense(amount, category, notes="", expense_date=None):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    if not category:
        raise ValueError("Category required")
    
    if expense_date is None:
        expense_date = str(date.today())

    record = {
        "amount": amount,
        "category": category.lower(),
        "notes": notes,
        "date": expense_date
    }

    expenses.append(record)
    save_data()
    return record


def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def list_expenses(category=None):
    if category:
        return [e for e in expenses if e["category"] == category.lower()]
    return expenses


def calculate_total(category=None):
    if category:
        return sum(e["amount"] for e in expenses if e["category"] == category.lower())
    return sum(e["amount"] for e in expenses)


if __name__ == "__main__":
    main()
