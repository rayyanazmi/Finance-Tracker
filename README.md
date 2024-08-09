# Finance Management System

## Overview

The Finance Management System is a simple, command-line-based application written in Python 3. It allows users to manage their finances by recording income and expenses, categorizing transactions, setting budgets, tracking recurring expenses, and more. This project is ideal for those who want to learn the basics of Python programming while also keeping track of their personal finances.

## Features

- **Add Transactions:** Record income and expenses with descriptions and categories.
- **Category Tracking:** View transactions by category to better understand your spending habits.
- **Budgeting and Alerts:** Set budgets for specific categories and receive alerts if you exceed them.
- **Recurring Transactions:** Automatically add recurring transactions (like monthly rent or subscriptions).
- **Search Functionality:** Search for transactions by keywords in their descriptions.
- **Balance Calculation:** Calculate the current balance based on recorded transactions.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- A terminal or command prompt to run the application.

### Installation

1. **Clone the Repository:**

   Open your terminal or command prompt and run the following command to clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```

   Replace `your-username` and `your-repository-name` with your GitHub username and the repository name.

2. **Navigate to the Project Directory:**

   ```bash
   cd your-repository-name
   ```

3. **Run the Application:**

   Run the following command to start the Finance Management System:

   ```bash
   python fintracker.py
   ```

### Usage

Once the program is running, you will see the main menu with options to add earnings, expenses, view transactions, and more. Simply enter the number corresponding to the option you want to select and follow the prompts.

Here’s a quick overview of what each option does:

1. **Add Earnings:** Record income with an amount, description, and category.
2. **Add Expense:** Record expenses with an amount, description, and category.
3. **View Transactions:** View all recorded transactions.
4. **View Transactions by Category:** Filter transactions by a specific category.
5. **Set Budget:** Set a budget for a specific category.
6. **Check Budget:** Check if spending in any category exceeds the budget.
7. **Add Recurring Transaction:** Set up transactions that repeat at regular intervals.
8. **Search Transactions:** Search for transactions based on a keyword in their descriptions.
9. **Calculate Balance:** Calculate and display the current balance.
10. **Exit:** Exit the application.

### Example Workflow

Here’s an example of how you might use the Finance Management System:

1. **Add an Earning:**
   - Choose option `1`.
   - Enter the amount, description (e.g., "Salary"), and category (e.g., "Income").

2. **Add an Expense:**
   - Choose option `2`.
   - Enter the amount, description (e.g., "Groceries"), and category (e.g., "Food").

3. **Set a Budget:**
   - Choose option `5`.
   - Set a budget for the "Food" category, e.g., $500.

4. **Check Budget:**
   - Choose option `6` to see if you are within your budget for each category.

5. **Add a Recurring Transaction:**
   - Choose option `7`.
   - Set up a recurring expense for "Rent" that repeats every 30 days.

6. **View Your Balance:**
   - Choose option `9` to see your current balance.

### Code Overview

The project is implemented in Python using a single class `Fintracker` that handles all the financial operations. Below is a brief overview of the key methods:

- `add_transaction(amount, description, category)`: Adds a new transaction to the system.
- `view_transactions()`: Displays all transactions.
- `view_transactions_by_category(category)`: Filters and displays transactions by category.
- `set_budget(category, amount)`: Sets a budget for a specified category.
- `check_budget()`: Checks if the spending in any category exceeds the budget.
- `add_recurring_transaction(amount, description, category, interval_days)`: Adds a recurring transaction.
- `process_recurring_transactions()`: Processes due recurring transactions and adds them to the main transaction list.
- `search_transactions(keyword)`: Searches transactions based on a keyword.
- `calculate_balance()`: Calculates the current balance by summing up all transactions.

### Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

### License

This project is open-source and available under the [MIT License](LICENSE).
