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