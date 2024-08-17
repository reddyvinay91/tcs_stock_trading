import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Choose the stock symbol, e.g., TCS (Tata Consultancy Services)
stock_symbol = 'TCS.NS'

# Download data for the last two years
data = yf.download(stock_symbol, start='2022-08-16', end='2024-08-16', progress=False)

# Display the first few rows of the data
print(data.head())

# Calculate the 20-day and 50-day SMAs
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

print(data['SMA_20'][20:])
print(data['SMA_50'][20:] )

# Define Buy and Sell signals
data['Signal'] = 0
data['Signal'][20:] = np.where(data['SMA_20'][20:] > data['SMA_50'][20:], 1, -1)
data['Position'] = data['Signal'].diff()

# Display the first few rows with signals
print(data.tail(10))

# Initial capital
initial_capital = 100000

# Create a new DataFrame to store the strategy results
strategy = pd.DataFrame(index=data.index)
strategy['Close'] = data['Close']
strategy['Signal'] = data['Position']
strategy['Daily Returns'] = data['Close'].pct_change()
strategy['Strategy Returns'] = strategy['Daily Returns'] * strategy['Signal'].shift(1)

# Calculate cumulative returns
strategy['Equity Curve'] = initial_capital * (1 + strategy['Strategy Returns']).cumprod()

# Calculate total returns
total_returns = strategy['Equity Curve'][-1] - initial_capital

# Calculate number of trades
num_trades = len(strategy[strategy['Signal'] != 0])

# Calculate winning and losing trades
winning_trades = len(strategy[strategy['Strategy Returns'] > 0])
losing_trades = len(strategy[strategy['Strategy Returns'] < 0])

# Calculate maximum drawdown
max_drawdown = strategy['Equity Curve'].min() - initial_capital

# Print out the results
print(f"Total Returns: ₹{total_returns:.2f}")
print(f"Number of Trades: {num_trades}")
print(f"Winning Trades (%): {winning_trades / num_trades * 100:.2f}%")
print(f"Losing Trades (%): {losing_trades / num_trades * 100:.2f}%")
print(f"Maximum Drawdown: ₹{max_drawdown:.2f}")
