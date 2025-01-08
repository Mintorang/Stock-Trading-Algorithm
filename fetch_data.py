import yfinance as yf 
import pandas as pd

def fetch_stock_data():

    apple = yf.Ticker("CVX")
    data = apple.history(period="1mo")
    return data

fetch_stock_data()
