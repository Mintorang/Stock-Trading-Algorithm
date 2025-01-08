from constants import PERIOD, TICKER, SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD, CSV_PATH, BODY, API_KEY, API_SECRET, BASE_URL
from rsi_calculator import calculate_avg_gain_loss, calculate_rsi
from fetch_data import fetch_stock_data
from macd_calculator import calculate_macd
from email_sender import send_email
from algorithim import stock_algorithim

# Main function
def main():
    ticker = TICKER


    subject = f"{ticker} CSV File with Technical Indicators"

    

    # Fetch stock data
    data = fetch_stock_data()

    # Calculate average gain and loss
    data = calculate_avg_gain_loss(data, PERIOD)

    # Calculate RSI
    data = calculate_rsi(data)
    # Calculate MACD
    data = calculate_macd(data)
    stock_algorithim(data)

    # Display the last few rows of data
    csvf = data[["Open", "Close", "Change", "Gain", "Loss", "Avg_Gain", "Avg_Loss", "RSI", "MACD Line", "Signal Line", "MACD Histogram"]].tail(20)
    csvf.to_csv(f"{ticker}_data.csv")
    print(data)
    #send_email(SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD, subject, BODY, CSV_PATH)
    

if __name__ == "__main__":
    main()
