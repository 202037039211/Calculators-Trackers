# Budget App

A simple budget management app that allows users to manage multiple categories (e.g., Food, Clothing, Auto) with features such as deposits, withdrawals, transfers, and a spending chart.

## Features:
- Add and manage categories for tracking various budgets (e.g., Food, Clothing, Auto).
- Deposit funds into a category.
- Withdraw funds and track spending in each category.
- Transfer funds between categories.
- Generate a chart displaying the percentage of spending for each category.

## Requirements:
- Python 3.x

## Installation:
1. Clone this repository or download the script.
2. Ensure that you have Python 3.x installed.

## Usage:
1. Run the script:
```bash
python main.py
```
2. The script will create and manipulate categories, making deposits and withdrawals, and generating a spending chart.

## Example:
```python
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')

clothing = Category('Clothing')
food.transfer(50, clothing)

auto = Category('Auto')
auto.deposit(1000, 'initial deposit')
auto.withdraw(15)

print(food)
print(create_spend_chart([food, clothing, auto]))
```
