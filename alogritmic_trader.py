import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_data(stock_symbol, start_date, end_date):
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    return data['Adj Close']


def calculate_moving_averages(prices, short_window, long_window):
    moving_averages = pd.DataFrame(index=prices.index)
    moving_averages['Short_MA'] = prices.rolling(window=short_window).mean()
    moving_averages['Long_MA'] = prices.rolling(window=long_window).mean()
    return moving_averages


def generate_signals(moving_averages):
    signals = pd.DataFrame(index=moving_averages.index)
    signals['Signal'] = 0
    signals['Signal'] = np.where(moving_averages['Short_MA'] > moving_averages['Long_MA'], 1, 0)
    signals['Position'] = signals['Signal'].diff()
    return signals

def backtest_strategy(signals, prices, initial_capital=10000):
    portfolio = pd.DataFrame(index=signals.index)
    portfolio['Holdings'] = signals['Signal'].shift(1) * prices * initial_capital / prices.iloc[0]
    portfolio['Cash'] = initial_capital - (signals['Signal'].shift(1) * prices * initial_capital / prices.iloc[0])
    portfolio['Total'] = portfolio['Holdings'] + portfolio['Cash']
    portfolio['Returns'] = portfolio['Total'].pct_change()
    return portfolio



# Parameters
stock_symbol = 'AAPL'
start_date = '2020-01-01'
end_date = '2021-01-01'
short_window = 40
long_window = 100

# Fetch Data
stock_data = fetch_data(stock_symbol, start_date, end_date)

# Calculate Moving Averages
moving_averages = calculate_moving_averages(stock_data, short_window, long_window)

# Generate Buy/Sell Signals
signals = generate_signals(moving_averages)

#Back testting
portfolio = backtest_strategy(signals, stock_data)


# Plot
plt.figure(figsize=(10,5))
plt.plot(stock_data.index, stock_data, label='Adjusted Close Price')
plt.plot(moving_averages.index, moving_averages['Short_MA'], label=f'Short {short_window}-day MA')
plt.plot(moving_averages.index, moving_averages['Long_MA'], label=f'Long {long_window}-day MA')
plt.plot(signals[signals['Position'] == 1].index,
         moving_averages['Short_MA'][signals['Position'] == 1],
         '^', markersize=10, color='g', label='Buy Signal')
plt.plot(signals[signals['Position'] == -1].index,
         moving_averages['Short_MA'][signals['Position'] == -1],
         'v', markersize=10, color='r', label='Sell Signal')
plt.title('Stock Trend Following Strategy')
plt.xlabel('Date')
plt.ylabel('Price in $')
plt.legend()
plt.show()

#Ploting Back testing

plt.figure(figsize=(10,5))
plt.plot(stock_data.index, stock_data, label='Adjusted Close Price')
plt.plot(stock_data.index, signals['Signal'] * max(stock_data), label='Signals', alpha=0.5)
plt.title('Buy and Sell Signals over Stock Price')
plt.xlabel('Date')
plt.ylabel('Price in $')
plt.legend()
plt.show()


#testting

print(signals.head(20))
print(portfolio[['Holdings', 'Cash', 'Total']].head(20))
