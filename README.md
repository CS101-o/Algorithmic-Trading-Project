# Algorithmic-Trading-Project
Implementation of a trend-following strategy algorithm 

## Introduction

This project is an implementation of an algorithmic trading strategy using Python. It includes scripts for data collection, a trend-following trading strategy, backtesting, and visualization of the strategy's performance.

## Technologies Used

- Python
- Pandas, NumPy, Matplotlib
- yfinance (for fetching historical stock data)

## Setup and Installation

"pip install pandas numpy matplotlib yfinance" or set-up the requirements.txt file

## How to run the code

git clone [URL of your repository]
cd Algorithmic-Trading-Project
python algorithmic_trader.py

## Features

-Implements a moving average-based trading strategy.
-Backtests the strategy with historical data.
-Visualizes the strategy's performance and potential trades.

##Strategy 

The strategy uses two moving averages: a short-term 40-day moving average and a long-term 100-day moving average. Buy signals are generated when the short-term moving average crosses above the long-term moving average, suggesting the beginning of an upward trend. Conversely, sell signals are triggered when the short-term moving average crosses below, indicating a potential downward trend

## Results and analysis from Back testing

The backtest results indicate that the strategy would have performed well during the observed period, which was characterized by a general upward trend in the stock price of AAPL. This can be attributed to the robust performance of technology stocks during that period, which saw increased demand for tech solutions and services.

##Key Observations
-Buy Signals: The strategy generated a key buy signal around May 2020, which would have allowed the algorithm to capitalize on the significant uptrend that followed.

-Sell Signals: A sell signal was generated towards the end of September 2020, helping to avoid a temporary downturn.

-Overall Performance: The strategy appears to have captured the major trend movements well, entering and exiting positions in alignment with the broader market movements.

## Generated graphs using Matplotlib
![image](https://github.com/CS101-o/Algorithmic-Trading-Project/assets/148367671/8932615b-a24d-4a18-a5e0-3760d61d66a5)
![image](https://github.com/CS101-o/Algorithmic-Trading-Project/assets/148367671/f5225333-ace2-44b4-aa3b-7976e55ecd0b)

## Future development 

Although it peforemed well in this instance, this startegy may not perform as well in a market without a clear trend or in a highly volatile market with frequent price reversals. Moreover, many other details such as cost of transactions has not been taken into consideration. Given that, I would be impracticale to use this trading algorithm in real world. Hence, I will try to widen my scope and generate better startegy that would yield reliable data in even a volatile market.





