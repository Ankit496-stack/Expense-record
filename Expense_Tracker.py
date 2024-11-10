import json
from datetime import datetime

# File to store the expenses
EXPENSE_FILE = "expenses.json"

def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(amount, category, description):
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("\n--- Expense List ---")
    total = 0
    for expense in expenses:
        print(f"Amount: ${expense['amount']}, Category: {expense['category']}, "
              f"Description: {expense['description']}, Date: {expense['date']}")
        total += expense['amount']
    
    print(f"\nTotal Expenses: ${total}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            try:
                amount = float(input("Enter amount: $"))
                category = input("Enter category (e.g., Food, Transport, Utilities): ")
                description = input("Enter description: ")
                add_expense(amount, category, description)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")
        
        elif choice == "2":
            view_expenses()
        
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
