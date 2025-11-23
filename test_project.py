import os
import json
from project import add_expense, calculate_total, list_expenses, load_data, DATA_FILE


def setup_function():
    
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    with open(DATA_FILE, "w") as f:
        json.dump([], f)
    load_data()


def test_add_expense():
    add_expense(50, "food", "burger")
    add_expense(25, "transport", "bus")

    expenses = list_expenses()
    assert len(expenses) == 2
    assert expenses[0]["amount"] == 50
    assert expenses[0]["category"] == "food"


def test_calculate_total():
    add_expense(100, "food")
    add_expense(50, "food")
    add_expense(30, "other")

    assert calculate_total("food") == 150
    assert calculate_total() == 180


def test_list_expenses():
    add_expense(20, "shopping")
    add_expense(40, "shopping")
    add_expense(10, "other")

    shop_expenses = list_expenses("shopping")
    assert len(shop_expenses) == 2
    assert all(e["category"] == "shopping" for e in shop_expenses)
