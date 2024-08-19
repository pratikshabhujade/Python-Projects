import pandas as pd
import pandas_datareader as pdr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb
import yfinance as yf
import matplotlib.pyplot as plt


import yfinance as yf

rcParams['figure.figsize'] = 8,6
sb.set()
# Fetch data for Amazon (AMZN)
amzn = yf.download('AMZN')
print(amzn)

# Download historical data for Amazon (AMZN)
amzn = yf.download('AMZN', start='2020-01-01', end='2023-12-31')

# Display the first few rows of the data
amzn.head()

# Plot the closing price over time
plt.figure(figsize=(10, 6))
plt.plot(amzn['Close'], label='AMZN Closing Price')
plt.title('Amazon (AMZN) Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the 20-day and 50-day moving averages
amzn['20 Day MA'] = amzn['Close'].rolling(window=20).mean()
amzn['50 Day MA'] = amzn['Close'].rolling(window=50).mean()

# Plot the closing price along with the moving averages
plt.figure(figsize=(14, 7))
plt.plot(amzn['Close'], label='AMZN Closing Price', color='blue')
plt.plot(amzn['20 Day MA'], label='20 Day MA', color='red')
plt.plot(amzn['50 Day MA'], label='50 Day MA', color='green')
plt.title('Amazon (AMZN) Stock Price with 20 & 50 Day Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Calculate daily returns
amzn['Daily Return'] = amzn['Close'].pct_change()

# Plot the daily returns
plt.figure(figsize=(14, 7))
plt.plot(amzn['Daily Return'], label='AMZN Daily Return', color='purple')
plt.title('Amazon (AMZN) Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return (%)')
plt.legend()
plt.grid(True)
plt.show()

# Display statistics of daily returns
amzn['Daily Return'].describe()

# Plot a histogram of daily returns
plt.figure(figsize=(10, 6))
plt.hist(amzn['Daily Return'].dropna(), bins=50, color='purple', alpha=0.75)
plt.title('Amazon (AMZN) Daily Returns Distribution')
plt.xlabel('Daily Return (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# Download data for Google and Apple
tickers = ['AMZN', 'GOOGL', 'AAPL']
stocks = yf.download(tickers, start='2020-01-01', end='2023-12-31')['Close']

# Plot closing prices of Amazon, Google, and Apple
plt.figure(figsize=(14, 7))
for ticker in tickers:
    plt.plot(stocks[ticker], label=f'{ticker} Closing Price')

plt.title('Stock Prices of Amazon, Google, and Apple')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
