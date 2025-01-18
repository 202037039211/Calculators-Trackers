class Category:
    def __init__(self, name):
        """Initialize the category with a name and an empty ledger."""
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Deposit a specified amount with an optional description."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Withdraw a specified amount if sufficient funds are available."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Return the current balance by summing the ledger entries."""
        total_balance = sum(entry["amount"] for entry in self.ledger)
        return total_balance

    def transfer(self, amount, category):
        """Transfer a specified amount to another category if sufficient funds exist."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Check if there are enough funds for the withdrawal."""
        return self.get_balance() >= amount

    def __str__(self):
        """Return a string representation of the category's ledger and balance."""
        # Title line centered within 30 characters
        title = f"{self.name:*^30}\n"
        
        # Ledger entries with descriptions and amounts
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        
        # Total balance
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    """Generate a chart showing the percentage spent by each category."""
    total_spent = 0
    category_spent = []

    # Calculate total withdrawal amounts per category
    for category in categories:
        spent = sum(-entry['amount'] for entry in category.ledger if entry['amount'] < 0)
        category_spent.append(spent)
        total_spent += spent

    # Calculate percentages spent for each category
    percentages = [(spent / total_spent) * 100 for spent in category_spent]

    # Start building the chart
    chart = "Percentage spent by category\n"
    
    # Loop over 100 to 0 percentage points
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"
    
    # Bottom line for the chart
    chart += "    -" + "---" * len(categories) + "\n"

    # Category names vertically
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            chart += (category.name[i] if i < len(category.name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n")


# Example usage
if __name__ == "__main__":
    # Create categories
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')

    clothing = Category('Clothing')
    food.transfer(50, clothing)

    auto = Category('Auto')
    auto.deposit(1000, 'initial deposit')
    auto.withdraw(15)

    # Print category details and the spend chart
    print(food)
    print(create_spend_chart([food, clothing, auto]))
