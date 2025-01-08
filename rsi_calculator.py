def calculate_avg_gain_loss(data, period):
    """
    Calculate the average gain and loss for RSI calculation.
    """
    data["Change"] = data["Close"].diff()
    data["Gain"] = data["Change"].apply(lambda x: x if x > 0 else 0)
    data["Loss"] = data["Change"].apply(lambda x: abs(x) if x < 0 else 0)

    data["Avg_Gain"] = data["Gain"].ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    data["Avg_Loss"] = data["Loss"].ewm(alpha=1/period, min_periods=period, adjust=False).mean()    

    return data

def calculate_rsi(data):

    
    if "Avg_Gain" not in data or "Avg_Loss" not in data:
        raise ValueError("Data must include 'Avg_Gain' and 'Avg_Loss' columns.")
    
    rs = data["Avg_Gain"] / data["Avg_Loss"]
    data["RSI"] = 100 - 100 / (1 + rs)
    return data





