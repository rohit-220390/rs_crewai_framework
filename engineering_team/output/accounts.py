# accounts.py

class Transaction:
    def __init__(self, account, symbol, operation_type, quantity, price):
        self.account = account
        self.symbol = symbol
        self.operation = operation_type
        self.quantity = quantity
        self.price = price


class Account:
    def __init__(self, account_number, initial_balance):
        """
        Initializes an Account object.

        :param account_number: Unique identifier for the account.
        :param initial_balance: Initial balance in the account.
        """
        self.account_number = account_number
        self.balance = initial_balance
        self.holdings = {}
        self.transactions = []
        self._initial_balance = initial_balance
        self.share_prices = {}  # Initialize share_prices here

    def set_share_prices(self, share_prices):
        """Set share prices for the account."""
        self.share_prices = share_prices

    def deposit(self, amount):
        """
        Deposits funds into the account.

        :param amount: Amount to deposit.
        :raises ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        self.transactions.append(Transaction(self, 'Cash', 'Deposit', amount, 1))

    def withdraw(self, amount):
        """
        Withdraws funds from the account.

        :param amount: Amount to withdraw.
        :raises ValueError: If the withdrawal amount is negative or exceeds balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        elif amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        self.transactions.append(Transaction(self, 'Cash', 'Withdrawal', -amount, 1))

    def buy(self, symbol, quantity):
        """
        Records a purchase of shares.

        :param symbol: Symbol for the share (e.g., AAPL).
        :param quantity: Number of shares to buy.
        :raises ValueError: If the purchase would leave the account with negative balance or insufficient funds.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        price = self.get_share_price(symbol)
        cost = price * quantity
        
        if cost > self.balance:
            raise ValueError("Insufficient funds")
        
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.balance -= cost
        self.transactions.append(Transaction(self, symbol, 'Buy', quantity, price))

    def sell(self, symbol, quantity):
        """
        Records a sale of shares.

        :param symbol: Symbol for the share (e.g., AAPL).
        :param quantity: Number of shares to sell.
        :raises ValueError: If the user does not have sufficient shares to sell.
        """
        if symbol not in self.holdings or quantity > self.holdings[symbol]:
            raise ValueError("Insufficient shares")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        price = self.get_share_price(symbol)
        revenue = price * quantity
        
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        
        self.balance += revenue
        self.transactions.append(Transaction(self, symbol, 'Sell', quantity, price))

    def get_balance(self):
        """
        Retrieves the current account balance.

        :return: Current account balance.
        """
        return self.balance

    def get_holdings(self):
        """
        Retrieves the current holdings of the user.

        :return: Dictionary of symbol-quantity pairs representing the user's holdings.
        """
        return self.holdings

    def get_portfolio_value(self):
        """
        Calculates and retrieves the total value of the user's portfolio.

        :return: Total value of the user's portfolio.
        """
        portfolio_value = self.balance
        for symbol, quantity in self.holdings.items():
            price = self.get_share_price(symbol)
            portfolio_value += price * quantity

        return portfolio_value

    def get_profit_loss(self):
        """
        Calculates and retrieves the profit or loss from the user's initial deposit.

        :return: Profit or loss from the user's initial deposit.
        """
        current_portfolio_value = self.get_portfolio_value()
        return current_portfolio_value - self._initial_balance

    def get_transactions(self):
        """
        Retrieves a list of all transactions made by the user.

        :return: List of transaction objects.
        """
        return self.transactions

    def cost_basis(self, symbol, quantity):
        """
        Calculates the total cost basis of a particular share.

        :param symbol: Symbol for the share (e.g., AAPL).
        :param quantity: Number of shares to consider.
        :return: Total cost basis of the specific shares.
        """
        if symbol not in self.holdings:
            raise ValueError(f"No record found for that share: {symbol}")
        
        # Calculate cost basis from buy transactions
        total_cost = 0
        shares_counted = 0
        
        for transaction in self.transactions:
            if transaction.symbol == symbol and transaction.operation == 'Buy':
                if shares_counted + transaction.quantity <= quantity:
                    total_cost += transaction.price * transaction.quantity
                    shares_counted += transaction.quantity
                else:
                    remaining = quantity - shares_counted
                    total_cost += transaction.price * remaining
                    shares_counted += remaining
                    break
        
        return total_cost

    def get_share_price(self, symbol):
        """
        Retrieves the current price of a specific share.

        :param symbol: Symbol for the share (e.g., AAPL).
        :return: Current price of the specified share.
        """
        symbol_upper = symbol.upper()
        if symbol_upper not in self.share_prices:
            raise ValueError(f"No price found for symbol: {symbol}")
        return self.share_prices[symbol_upper]


class MarketInfo:
    def __init__(self):
        self.share_prices = {
            'AAPL': 123.45,
            'GOOGL': 1500.99,
            'TSLA': 22000.11
        }

    def get_prices(self):
        """Return share prices dictionary."""
        return self.share_prices


def main():
    account_number = "A001"
    initial_balance = 10000
    account = Account(account_number, initial_balance)
    
    # Set share prices
    market = MarketInfo()
    account.set_share_prices(market.get_prices())
    
    print("You have created an account with balance of ${}.".format(account.get_balance()))
    account.deposit(5000)
    
    price = account.get_share_price('AAPL')
    account.buy('AAPL', 10)

    print("Account holdings after buying AAPL stocks: {}".format(account.get_holdings()))

    profit_loss = account.get_profit_loss()
    portfolio_value = account.get_portfolio_value()
    
    print("You have held {} shares of stock for {}, costing ${} per share and currently trading at ${}, giving you a cost basis of ${}".format(
        'AAPL', 10, price, account.get_share_price('AAPL'), account.cost_basis('AAPL', 10)))
    
    print("Your total portfolio value: ${:.2f}".format(portfolio_value))
    print("Your profit/loss: ${:.2f}".format(profit_loss))


if __name__ == "__main__":
    main()