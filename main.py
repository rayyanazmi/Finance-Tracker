# Defining the Fintracker class to manage financial transactions

class Fintracker:

    # Initializing the Fintracker class with an empty list to store transactions
    def __init__(self):
        self.transactions = []

    # Method to add a new transaction (either income or expense)
    # Parameters:
    # amount (float): The amount of the transaction
    # description (str): A brief description of the transaction
    def add_transaction(self, amount, description):
        self.transactions.append({'amount': amount, 'description': description})

    # Method to view all recorded transactions
    # Displays a list of transactions with their respective amounts and descriptions
    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
        else:
            for i, transaction in enumerate(self.transactions, 1):
                print(f"{i}. Amount: {transaction['amount']}, Description: {transaction['description']}")

    # Method to calculate the current balance based on all transactions
    # Returns:
    # balance (float): The sum of all transaction amounts
    def calculate_balance(self):
        balance = sum(transaction['amount'] for transaction in self.transactions)
        return balance
    
    # Main method to handle user interactions through a simple command-line interface
    def main():
        fin_tracker = Fintracker()

        while True:
            # Displaying the menu options for the user
            print("\nFinance Management System")
            print("1. Add Earnings")
            print("2. Add Expense")
            print("3. View Transactions")
            print("4. Calculate Balance")
            print("5. Exit")

            # Getting the user's choice of action
            choice = input("Choose an option: ")

            # Responding to the user's choice and performing the corresponding action
            if choice == "1":
                # Adding an earning (positive amount)
                amount = float(input("Enter earning amount: "))
                description = input("Enter earning description: ")
                fin_tracker.add_transaction(amount, description)
                print("Income Added Successfully.")
            
            elif choice == "2":
                # Adding an expense (negative amount)
                amount = float(input("Enter expenses amount: "))
                description = input("Enter expenses description: ")
                fin_tracker.add_transaction(-amount, description)
                print("Expense Added Successfully.")

            elif choice == "3":
                # Viewing all recorded transactions
                fin_tracker.view_transactions()

            elif choice == "4":
                # Calculating and displaying the current balance
                balance = fin_tracker.calculate_balance()
                print(f"Current Balance: {balance}")

            elif choice == "5":
                # Exiting the program
                print("Exiting the Finance Management System.")
                break

            else:
                # Handling invalid user input
                print("Invalid option. Please try again with the listed options.")

# Entry point of the program
if __name__ == "__main__":
    Fintracker.main()
