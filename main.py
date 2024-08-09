# Fintracker: A Simple Finance Management System

# Importing necessary libraries for additional functionality
from datetime import datetime, timedelta

# Defining the Fintracker class to manage financial transactions
class Fintracker:

    def __init__(self):
        """
        Initialize the Fintracker class with an empty list to store transactions,
        an empty list for recurring transactions, and a budget dictionary.
        """
        self.transactions = []
        self.recurring_transactions = []
        self.budget = {}

    def add_transaction(self, amount, description, category):
        """
        Add a new transaction to the list.

        Parameters:
        - amount (float): The amount of the transaction (positive for income, negative for expenses)
        - description (str): A brief description of the transaction
        - category (str): The category to which the transaction belongs (e.g., 'Food', 'Rent', etc.)
        """
        self.transactions.append({'amount': amount, 'description': description, 'category': category})

    def view_transactions(self):
        """
        View all recorded transactions, displaying their amount, description, and category.
        """
        if not self.transactions:
            print("No transactions recorded.")
        else:
            for i, transaction in enumerate(self.transactions, 1):
                print(f"{i}. Amount: {transaction['amount']}, Description: {transaction['description']}, Category: {transaction['category']}")

    def view_transactions_by_category(self, category):
        """
        View all transactions filtered by a specific category.

        Parameters:
        - category (str): The category to filter transactions by
        """
        filtered_transactions = [t for t in self.transactions if t['category'] == category]
        if not filtered_transactions:
            print(f"No transactions recorded under category: {category}")
        else:
            for i, transaction in enumerate(filtered_transactions, 1):
                print(f"{i}. Amount: {transaction['amount']}, Description: {transaction['description']}, Category: {transaction['category']}")

    def set_budget(self, category, amount):
        """
        Set a budget for a specific category.

        Parameters:
        - category (str): The category for which the budget is being set
        - amount (float): The budget amount
        """
        self.budget[category] = amount
        print(f"Budget of {amount} set for category: {category}")

    def check_budget(self):
        """
        Check if spending in any category has exceeded the budget and alert the user.
        """
        for category, budget in self.budget.items():
            spent = sum(t['amount'] for t in self.transactions if t['category'] == category)
            if spent > budget:
                print(f"Alert: You have exceeded the budget for {category}. Budget: {budget}, Spent: {spent}")

    def add_recurring_transaction(self, amount, description, category, interval_days):
        """
        Add a recurring transaction that will be automatically added after a specified interval.

        Parameters:
        - amount (float): The amount of the recurring transaction
        - description (str): A brief description of the transaction
        - category (str): The category of the transaction
        - interval_days (int): The interval in days for the recurring transaction
        """
        next_date = datetime.now() + timedelta(days=interval_days)
        self.recurring_transactions.append({'amount': amount, 'description': description, 'category': category, 'next_date': next_date, 'interval_days': interval_days})
        print(f"Recurring transaction added: {description}, every {interval_days} days.")

    def process_recurring_transactions(self):
        """
        Check and add any due recurring transactions to the main transaction list.
        """
        for transaction in self.recurring_transactions:
            if datetime.now() >= transaction['next_date']:
                self.add_transaction(transaction['amount'], transaction['description'], transaction['category'])
                transaction['next_date'] = datetime.now() + timedelta(days=transaction['interval_days'])
                print(f"Recurring transaction processed: {transaction['description']}")

    def search_transactions(self, keyword):
        """
        Search for transactions that match a specific keyword in their description.

        Parameters:
        - keyword (str): The keyword to search for in transaction descriptions
        """
        results = [t for t in self.transactions if keyword.lower() in t['description'].lower()]
        if not results:
            print("No matching transactions found.")
        else:
            for i, transaction in enumerate(results, 1):
                print(f"{i}. Amount: {transaction['amount']}, Description: {transaction['description']}, Category: {transaction['category']}")

    def calculate_balance(self):
        """
        Calculate the current balance based on all transactions.

        Returns:
        - balance (float): The sum of all transaction amounts
        """
        balance = sum(transaction['amount'] for transaction in self.transactions)
        return balance
    
    def main():
        """
        Main method to handle user interactions through a command-line interface.
        """
        fin_tracker = Fintracker()

        while True:
            # Process any recurring transactions before showing the menu
            fin_tracker.process_recurring_transactions()

            # Displaying the menu options for the user
            print("\nFinance Management System")
            print("1. Add Earnings")
            print("2. Add Expense")
            print("3. View Transactions")
            print("4. View Transactions by Category")
            print("5. Set Budget")
            print("6. Check Budget")
            print("7. Add Recurring Transaction")
            print("8. Search Transactions")
            print("9. Calculate Balance")
            print("10. Exit")

            # Getting the user's choice of action
            choice = input("Choose an option: ")

            # Responding to the user's choice and performing the corresponding action
            if choice == "1":
                # Adding an earning (positive amount)
                amount = float(input("Enter earning amount: "))
                description = input("Enter earning description: ")
                category = input("Enter category: ")
                fin_tracker.add_transaction(amount, description, category)
                print("Income Added Successfully.")
            
            elif choice == "2":
                # Adding an expense (negative amount)
                amount = float(input("Enter expense amount: "))
                description = input("Enter expense description: ")
                category = input("Enter category: ")
                fin_tracker.add_transaction(-amount, description, category)
                print("Expense Added Successfully.")

            elif choice == "3":
                # Viewing all recorded transactions
                fin_tracker.view_transactions()

            elif choice == "4":
                # Viewing transactions filtered by category
                category = input("Enter category to view transactions: ")
                fin_tracker.view_transactions_by_category(category)

            elif choice == "5":
                # Setting a budget for a category
                category = input("Enter category for budget: ")
                amount = float(input(f"Enter budget amount for {category}: "))
                fin_tracker.set_budget(category, amount)

            elif choice == "6":
                # Checking the budget and alerting if exceeded
                fin_tracker.check_budget()

            elif choice == "7":
                # Adding a recurring transaction
                amount = float(input("Enter amount for recurring transaction: "))
                description = input("Enter description for recurring transaction: ")
                category = input("Enter category for recurring transaction: ")
                interval_days = int(input("Enter interval in days for recurrence: "))
                fin_tracker.add_recurring_transaction(amount, description, category, interval_days)

            elif choice == "8":
                # Searching transactions by keyword
                keyword = input("Enter keyword to search in transaction descriptions: ")
                fin_tracker.search_transactions(keyword)

            elif choice == "9":
                # Calculating and displaying the current balance
                balance = fin_tracker.calculate_balance()
                print(f"Current Balance: {balance}")

            elif choice == "10":
                # Exiting the program
                print("Exiting the Finance Management System.")
                break

            else:
                # Handling invalid user input
                print("Invalid option. Please try again with the listed options.")

# Entry point of the program
if __name__ == "__main__":
    Fintracker.main()
