# app.py
import gradio as gr
from accounts import Account, Transaction, MarketInfo

def create_shadows_demo():
    market_info = MarketInfo()
    account = Account('A001', 10000)
    
    def refresh_account_ui(account):
        return [
            "Account: A001",
            f"Current Balance: ${account.get_balance():.2f}",
            f"Holdings: {account.get_holdings()}",
            "Portfolio Value: ${:.2f}".format(account.get_portfolio_value()),
            "Profit/Loss: ${:.2f}".format(account.get_profit_loss())
        ]

    demo = gr.Blocks()
    with demo:
        gr.Markdown("Select actions to interact with your trading account:")
        
        # create_account
        create_button = gr.Button('Create Account')
        create_button.on_click(lambda: create_account(account))
        
        deposit_input = gr.Number(label="Deposit Amount:")
        withdraw_input = gr.Number(label="Withdraw Amount:")
        buy_input = gr.Number(label="Shares to Buy:")
        symbol_dropdown = gr.Dropdown(label="Stock Ticker Symbol", value='AAPL', options=[{'label': 'AAPL', 'value': 'AAPL'}, {'label': 'TSLA', 'value': 'TSLA'}])
        
        # deposit
        deposit_button = gr.Button('Deposit')
        deposit_button.on_click(lambda: account.deposit(deposit_input.value))
        
        # withdraw
        withdraw_button = gr.Button('Withdraw')
        withdraw_button.on_click(lambda: account.withdraw(withdraw_input.value))
        
        # buy
        buy_button = gr.Button('Buy Symbol')
        buy_button.on_click(lambda: account.buy(symbol_dropdown.value, buy_input.value))
        
        # sell
        sell_dropdown = gr.Dropdown(label='Sell Stocks of:', value=None, options=[{'label': None, 'value': None}])
        for key in account.holdings:
            sell_dropdown.options.append({'label': key, 'value': key}) 
        sell_button = gr.Button('Sellers (no functionality)')
        
        # transaction history
        history_table = gr.Table(label="Trans.", show_index=False)
        def update_history(account):
            transactions = account.get_transactions()
            info = []
            for transaction in transactions:
                action = "Buy" if transaction.operation == 'Buy' else "Sell"
                time_str = ""
                
                #formatting a cell with a bunch of info inside to be presented to the table.
                info.append([action, "$ {quantity} {symbol}".format(quantity=transaction.quantity, symbol=transaction.symbol),
                             transaction.price,
                              ])
            
            history_table.update(
                table_data = info
            )
        
        demo.add(refresh_account_ui(account), create_button)
        # display account info, buttons for user interaction
    return demo

def create_account(current_account):
    current_account.deposit(10000)

def main():
    # Get the dashboard object with our blocks added
    demo = create_shadows_demo()
    
    # Show the Gradiometer logo and automatically launch the development server.
    gr.Interface(demo, layout="vertical", title="Gradio Demo").launch()

if __name__ == "__main__":
    main()