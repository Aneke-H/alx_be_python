class BankAccount:
    def __init__(self,account_balance: float = 0.0):
        """"Initializes a BankAccount instance with a given balance."""
        self.account_balance = account_balance
        
    def deposit(self, amount: float) -> None:
        """Deposits a specified amount into the account."""
        self.account_balance += amount
        
    def withdraw(self, amount: float) -> bool:
        """Withdraws a specified amount from the account if sufficient funds are available.
        Returns True if the withdrawal was successful, False otherwise."""
        if amount <= self.account_balance:
            return True
        return False
            
            
    def display_balance(self) -> None:
        """Displays the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
    