import os
import json
from datetime import datetime

DATA_FILE = "expenses_data.json"

#ENSURE DATA FILE EXISTS
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump([], file)

# 🔹 Add a new expense
def load_expenses():
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
# 🔹 Save expenses to file
def save_expense(expense):
    expenses = load_expenses()
    expenses.append(expense)
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# 🔹 Add expense
def add_expense():
    try:
        amount = float(input("Enter amount: ₹").strip())
        category = input("Enter category (e.g., Food, Transport): ").strip().title()
        description = input("Enter description: ").strip()
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

        if date_input:
            date = datetime.strptime(date_input, "%Y-%m-%d").date().isoformat()
        else:
            date = datetime.today().date().isoformat()

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        save_expense(expense)
        print("✅ Expense saved successfully!")

    except ValueError:
        print("❌ Invalid amount or date format.")

# 🔹 View all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\n📊 Expense List:")
    for i, expense in enumerate(expenses, start=1):
        print(f"  {i}. {expense['description']} - ₹{expense['amount']} ({expense['date']})")

# 🔹 monthly summary
def monthly_summary():
    expenses = load_expenses()
    summary = {}

    for exp in expenses:
        month = exp["date"][:7]  # YYYY-MM
        summary.setdefault(month, 0)
        summary[month] += exp["amount"]

    if not summary:
        print("📭 No expenses to summarize.")
        return

    print("\n📊 Monthly Summary:")
    for month, total in sorted(summary.items()):
        print(f"- {month}: ₹{total:.2f}")
    total_expenses = sum(summary.values())
    print(f"Total Expenses: ₹{total_expenses:.2f}")


# 🔹 Filter by category
def filter_by_category():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    category = input("Enter category to filter: ").strip().title()
    filtered = [exp for exp in expenses if exp["category"] == category]

    if not filtered:
        print(f"No expenses found for category '{category}'.")
        return

    print(f"\n📂 Expenses in category '{category}':")
    for i, expense in enumerate(filtered, start=1):
        print(f"  {i}. {expense['description']} - ₹{expense['amount']} ({expense['date']})")
    total = sum(exp["amount"] for exp in filtered)
    print(f"Total in '{category}': ₹{total:.2f}")


# Menu
def main():
    while True:
        print("\n💰 Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("👋 Exiting. Track wisely!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()