from orders import order
from constants import API_KEY, API_SECRET, BASE_URL
def stock_algorithim(data):
    # BUYING STOCK
    if (data["MACD Line"] > data["Signal Line"]).any() and (data["RSI"] < 30).any():
        order(API_KEY, API_SECRET, BASE_URL, 1, "buy")

    # SELLING STOCK

    if (data["MACD Line"] < data["Signal Line"]).any() and (data["RSI"] > 70).any():
        order(API_KEY, API_SECRET, BASE_URL, 1, "sell")