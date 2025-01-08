import time
import pandas as pd
from alpaca_trade_api.rest import REST
import ta
from constants import API_KEY, API_SECRET
from orders import order

# Alpaca API credentials
BASE_URL = 'https://paper-api.alpaca.markets'
alpaca = REST(API_KEY, API_SECRET, BASE_URL)

# Calculate RSI and MACD
def calculate_indicators(data):
    data['RSI'] = ta.momentum.RSIIndicator(data['close'], window=14).rsi()
    macd = ta.trend.MACD(data['close'], window_slow=26, window_fast=12, window_sign=9)
    data['MACD_Line'] = macd.macd()
    data['Signal_Line'] = macd.macd_signal()
    data['MACD_Histogram'] = macd.macd_diff()
    return data

# Trading algorithm
def algorithim(data):
    last_row = data.iloc[-1]
    if (last_row["RSI"] < 30) and (last_row["MACD_Line"] > last_row["Signal_Line"]):
        order(API_KEY, API_SECRET, BASE_URL, 1, "buy")
        print(f"Bought one apple stock.")
    if (last_row["RSI"] > 70) and (last_row["MACD_Line"] < last_row["Signal_Line"]):
        order(API_KEY, API_SECRET, BASE_URL, 1, "sell")
        print("Sold one apple stock")
    print(f"RSI: {last_row["RSI"]}, MACD Line: {last_row["MACD_Line"]}, Signal Line: {last_row["Signal_Line"]}")

# Main function
def main():
    symbol = "CVX"
    while True:
        # Fetch the latest data
        data = alpaca.get_bars(symbol, "1Min", limit=100).df
        data.reset_index(inplace=True)
        data.set_index('timestamp', inplace=True)

        # Calculate indicators and apply the algorithm
        data = calculate_indicators(data)
        algorithim(data)

        # Wait for a minute before fetching new data
        print(f"Processed data at {pd.Timestamp.now()}")
        time.sleep(60)

if __name__ == "__main__":
    main()
