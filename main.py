# Creating Fintracker class with attributes

class Fintracker:

    def __init__(self):
        
        self.transactions = []

# Defining method to add new transaction

    def add_transaction(self, amount, description):

        self.transactions.append({'amount': amount, 'description': description})

# Defining method to view all transactions

    def view_transactions(self):

        if not self.transactions:

            print("No transactions recorded.")

        else:

            for i,transaction in enumerate(self.transactions, 1):

                print(f"{i}. Amount: {transaction['amount']}, Description: {transaction['description']}")

# Defining method to calculate balance

    def calculate_balance(self):

        balance = sum(transaction['amount'] for transaction in self.transactions)

        return balance
    
# Creating Main function for user interaction

    def main():

        fin_tracker = Fintracker()

        while True:

            print("\nFinance Management System")
            print("1. Add Earnings")
            print("2. Add Expense")
            print("3. View Transactions")
            print("4. Calculate Balance")
            print("5. Exit")

            choice = input("Choose an option: ")

#  Responding according to user choice
            if choice == "1":

                amount = float(input("Enter earning amount: "))

                description = input("Enter earning description: ")

                fin_tracker.add_transaction(amount, description)
                print("Income Added Succefully.")
            
            elif choice == "2":

                amount = float(input("Enter expenses amount: "))

                description = input("Enter expenses description: ")

                fin_tracker.add_transaction(-amount, description)
                print("Expense Added Succefully.")

            elif choice == "3":

                fin_tracker.view_transactions()

            elif choice == "4":
                
                balance = fin_tracker.calculate_balance()

                print(f"Current Balance: {balance}")

            elif choice == "5":

                print("Exiting the Finance Management System.")
                break

            else:

                print("Invalid option. Please try again.")

# Calling the module
if __name__ == "__main__":
    Fintracker.main()