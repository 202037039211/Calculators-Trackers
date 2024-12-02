import csv
import os

# Configuration
BUDGET_FILE = os.path.expanduser("path/to/budget.csv")
EXPENSE_FILE = os.path.expanduser("path/to/expenses.csv")

# Initialize budget and expense files
def initialize_files():
    """Initialize the budget and expense CSV files if they don't exist."""
    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Budget'])
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
    print("Initialized budget and expense files.")

# Add budget category
def add_budget(category, amount):
    """Add a new budget category."""
    with open(BUDGET_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])
    print(f"Added budget: {category} - {amount}")

# Record an expense
def record_expense(date, category, amount, description):
    """Record an expense."""
    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print(f"Recorded expense: {description} - {amount} in {category} on {date}")

# Generate budget summary
def generate_summary():
    """Generate a summary of the budget and expenses."""
    budget = load_budget()
    expenses = load_expenses()
    summary = {category: {'Budget': budget.get(category, 0), 'Spent': 0} for category in budget}

    for expense in expenses:
        category = expense['Category']
        if category in summary:
            summary[category]['Spent'] += float(expense['Amount'])

    print("\nBudget Summary:")
    for category, data in summary.items():
        remaining = data['Budget'] - data['Spent']
        print(f"{category}: Budgeted: {data['Budget']}, Spent: {data['Spent']}, Remaining: {remaining}")

# Load budget from CSV
def load_budget():
    """Load the budget data from the CSV file."""
    budget = {}
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                budget[row['Category']] = float(row['Budget'])
    return budget

# Load expenses from CSV
def load_expenses():
    """Load the expenses data from the CSV file."""
    expenses = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    return expenses

# Main Menu
if __name__ == "__main__":
    initialize_files()
    while True:
        print("\nBudget and Expense Tracker")
        print("1) Add Budget")
        print("2) Record Expense")
        print("3) Generate Summary")
        print("4) Exit")
        choice = input("Select an option: ")

        if choice == '1':
            category_name = input("Enter budget category: ")
            try:
                amount = float(input("Enter budget amount: "))
                add_budget(category_name, amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            category_name = input("Enter expense category: ")
            try:
                amount = float(input("Enter expense amount: "))
                description = input("Enter description: ")
                record_expense(date, category_name, amount, description)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == '3':
            generate_summary()
        elif choice == '4':
            break
        else:
            print("Invalid option.")
