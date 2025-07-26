## Personal Expense Tracker

This is a simple command-line Personal Expense Tracker written in Python. It allows you to record, view, and analyze your daily expenses efficiently.

### Features

- **Add Expense:** Record a new expense with amount, category, description, and date.
- **View All Expenses:** Display a list of all recorded expenses.
- **Filter by Category:** View expenses filtered by a specific category.
- **Monthly Summary:** Get a summary of total expenses for each month.
- **Persistent Storage:** All expenses are saved in a JSON file (`expenses_data.json`).

### How It Works

When you run `Tracker.py`, you will see a menu with the following options:

1. **Add Expense**: Prompts for amount, category, description, and date (defaults to today if left blank). The expense is saved to `expenses_data.json`.
2. **View All Expenses**: Lists all expenses with their description, amount, and date.
3. **Filter by Category**: Enter a category to see only expenses in that category, along with the total for that category.
4. **Monthly Summary**: Shows total expenses for each month and the overall total.
5. **Exit**: Exits the program.

### Data Storage

All expenses are stored in `expenses_data.json` in the same directory. The file is automatically created if it does not exist.

Each expense entry has the following format:

```json
{
  "amount": 100.0,
  "category": "Food",
  "description": "Lunch at cafe",
  "date": "2025-07-26"
}
```

### Running the Program

Make sure you have Python 3 installed. To run the tracker, use:

```powershell
python Tracker.py
```

Follow the on-screen prompts to add and manage your expenses.

### Example Usage

```
💰 Personal Expense Tracker
1. Add Expense
2. View All Expenses
3. Filter by Category
4. Monthly Summary
5. Exit
Choose an option: 1
Enter amount: ₹250
Enter category (e.g., Food, Transport): Food
Enter description: Dinner
Enter date (YYYY-MM-DD) or press Enter for today:
✅ Expense saved successfully!
```

### Notes

- Enter dates in `YYYY-MM-DD` format.
- Categories are case-insensitive and will be capitalized.
- The program handles invalid input gracefully.

---
Feel free to modify or extend the tracker as per your needs!
