class Checkbook:
    """
    A class to represent a simple checkbook system for managing deposits,
    withdrawals, and balance inquiries.
    """

    def __init__(self):
        """
        Initialize the checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook balance.

        Parameters:
        amount (float): The amount to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook balance.

        Parameters:
        amount (float): The amount to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance of the checkbook.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the Checkbook.
    Handles user input for deposit, withdraw, and balance inquiries,
    with error handling for invalid inputs.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Error: Amount cannot be negative. Please try again.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Error: Amount cannot be negative. Please try again.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
