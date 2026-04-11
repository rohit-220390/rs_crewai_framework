```python
import unittest
from accounts import Account  #, Transaction, MarketInfo


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("A001", 10000)

    def test_get_balance(self):
        """
        :return:
        """
        self.assertEqual(self.account.get_balance(), 10000)
        self.account.deposit(5000)
        self.assertEqual(self.account.get_balance(), 15000)

    def test_deposit(self):
        """
       Deposits funds into the account.

       Args:
           amount: Amount to deposit.
       Returns:
           Nothing
       """
        self.account.deposit(10000)
        self.assertEqual(self.account.get_balance(), 20000)


    def test_withdraw_from_empty_account_raises_value_error(self):
        """
        :return:
        """
        with self.assertRaises(ValueError) as e:
            self.account.withdraw(0)

    def test_withdraw_more_than_balance_raises_value_error(self):

        self.account.deposit(12000)
        self.assertEqual(self.account.get_balance(), 20000)
        with self.assertRaises(ValueError) as e:
            self.account.withdraw(14000)


    def test_buy_inadequate_funds_from_deposited_initial_amount(self):
        """
        Raises ValueError because this purchase leaves the account balance very low
           and it cannot afford more shares than can be afforded.
        """

        with self.assertRaises(ValueError) as e:
            self.account.buy('AAPL', 20)

    def test_sell_more_than_owned_share(self):
        """
        A ValueError must be raised here, if any error occurs
        else asserts True (No Error Raised)
        """
        with self.assertRaises(ValueError) as e:

           self.account.sell('AAPL', 15)


    def test_get_holdings(self):
        """
       Retrieves the current holdings of the user.

       Args:
            None

       Returns

          Dictionary symbol-quantity pairs representing user's holdings
           """
        initial = {'AAPL': 10}
        result =  self.account.buy('AAPL', 15)
        expected ={'AAPL' : 15}
        self.assertEqual(self.account.get_holdings(), expected)

    def test_get_portfolio_value(self):
        """
       Retrieves the total value of user's portfolio.

       Args:
           None
            Raises ValueError: If insufficient funds or more shares than can be afforded

         Returns:

             Total Portfolio Value (Current Shares Value + Balance)
              """

        initial = self.account.get_balance()
        price AAPL, GOOGL = 125.99
        price TSLA= 22000
        portfolio_value_expected = (125*15) +(1500 *5) + (22000 *3)+10000
        
        self.assertEqual(self.account.buy('AAPL', 10), True)
        self.assertEqual(self.account.get_portfolio_value(),portfolio_value_expected )
        total_cost = price * quantity

    def test_get_profit_loss(self):
        """
       Retrieves profit or loss from user's initial deposit.

           Args         None
                               Returns:

            Profit/Loss
                  """
        initial_balance = 10000
        current_portfolio_value = self.account.get_holdings().values()
        print("Account value %: ", self.account.buy('AAPL',10))

        for key in list(self.account.holdings.keys()):
            holding_weightage = (self.account.holdings[key] / initial_balance) * 100
            value=(holding_weightage/100)*current_portfolio_value+(holding_weightage/100)*(current_portfolio_value - initial_balance-1)
            total_holding_value -= value

        self.assertEqual((total_investment_value-(account.get_portfolio_value())), 1)


class TestTransactions(unittest.TestCase):
    def setUp(self):

        self.account = Account("A001", 10000)


    def test_get_transactions_empty_account(self):
       """
      Retrieves transactions of an employee
       Return:
         """
       expected = []
       actual=self.account.get_transactions()
       self.assertEqual(actual,expected)

    def test_buy_transaction_added_to_list(self):

        # buy AAPL (initial quantity)
        self.account.buy('AAPL', 10)
        self.assertIsInstance(self.account.transactions[0], Transaction)
        self.assertEqual(self.account.transactions[-1].operation, 'Buy')
        self.assertEqual(self.account.transactions[-1].symbol, 'AAPL')

    def test_sell_transaction_added_to_list(self):
       current_balance =10000
       expected_cost_price =  (12.45 * 5) + ((12 *15))
       balance =self.account.buy('AAPL',10)
       self.assertIsNotNone(balance)
       share_price AAPL=1500
       self.assertEqual(current_balance ,expected_cost_price+balance)


    def test_deposit_transaction_added_to_list(self):
        """
           Transaction: Adds a deposit transaction for each $ deposited.
        """

        current_value =10000

        # Test balance before and after adding transactions is the same as initial balance + deposit amount
        initial = 0
        expected_cost_price =  (12.45 * 15)
        price = self.account.get_share_price('AAPL')
        shares_purchased  =self.account.buy('AAPL', 5)

        # Add deposit transaction for $6000 to balance of $10000
        amount = 500
        final_balance = current_value + amount
      #print("Current Balance AAPL cost is", expected_cost_price)
        self.assertEqual(final_balance,amount +initial)

    def test_withdraw_transaction_added_to_list(self):
        """

         :return:
         """
    
class TestAccountMethods(unittest.TestCase):

    def setUp(self):
        self.account= Account("A001",10000)


    def test_account_number_initalized_in_create_accnt_method(self):

        created_account = self.account
        expected='A001'
        actual=create_acnt['account_number']
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()

```

You probably want to use the following commands (or their equivalent) as well:

1. `python -m unittest discover` or simply `unittest`  if not available
2. The test class `TestAccount` above defines how you want your code behavior and edge cases to be checked