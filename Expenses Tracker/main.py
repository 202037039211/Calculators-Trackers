# Function to add a new expense to the list
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Function to print all the expenses
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Function to calculate the total expenses
def total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

# Function to filter expenses by a specific category
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

# Main program execution
def main():
    expenses = []  # Initialize an empty list to store expenses

    # Main loop to interact with the user
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        # Get user input for the chosen option
        choice = input('Enter your choice: ')

        if choice == '1':
            # Add an expense
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # List all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            # Show total expenses
            print('\nTotal Expenses:', total_expenses(expenses))

        elif choice == '4':
            # Filter expenses by category
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(list(expenses_from_category))  # Convert filter object to list

        elif choice == '5':
            # Exit the program
            print('Exiting the program.')
            break

# Run the program
main()
