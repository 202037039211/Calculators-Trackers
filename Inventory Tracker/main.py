import csv
import os

# Configuration
INVENTORY_FILE = os.path.expanduser("path/to/inventory.csv")
LOW_STOCK_THRESHOLD = 5  # Threshold for low stock alerts

# Initialize inventory if file does not exist
def initialize_inventory():
    if not os.path.exists(INVENTORY_FILE):  # Check if inventory file exists
        with open(INVENTORY_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item', 'Quantity'])  # Write header row
        print("Initialized inventory file.")
    else:
        print("Inventory file already exists.")

# Add or update inventory item
def update_inventory(item, quantity):
    inventory = load_inventory()
    if item in inventory:
        inventory[item] += quantity  # Update quantity if item exists
    else:
        inventory[item] = quantity  # Add new item if not in inventory

    save_inventory(inventory)
    print(f"Updated inventory: {item} - {inventory[item]}")

# Load inventory from CSV file
def load_inventory():
    inventory = {}
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                inventory[row[0]] = int(row[1])  # Load item and quantity into dictionary
    return inventory

# Save updated inventory to CSV file
def save_inventory(inventory):
    with open(INVENTORY_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item', 'Quantity'])  # Write header row
        for item, quantity in inventory.items():
            writer.writerow([item, quantity])  # Write each item and its quantity

# Check for low stock items based on defined threshold
def check_low_stock():
    inventory = load_inventory()
    low_stock_items = [item for item, quantity in inventory.items() if quantity < LOW_STOCK_THRESHOLD]
    
    if low_stock_items:
        print("Low stock items:", low_stock_items)
    else:
        print("No low stock items.")

# Main menu for interacting with the inventory
if __name__ == "__main__":
    initialize_inventory()  # Ensure inventory file is initialized

    while True:
        print("\nInventory Tracker")
        print("1) Add/Update Item")
        print("2) Check Low Stock")
        print("3) Exit")
        choice = input("Select an option: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to add: "))
            update_inventory(item_name, quantity)
        elif choice == '2':
            check_low_stock()
        elif choice == '3':
            break  # Exit the program
        else:
            print("Invalid option. Please choose a valid action.")
