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