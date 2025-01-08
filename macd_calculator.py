def calculate_macd(data):
    data['Fast EMA'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['Slow EMA'] = data['Close'].ewm(span=26, adjust=False).mean()
    data["MACD Line"] = data["Fast EMA"] - data["Slow EMA"]
    data['Signal Line'] = data['MACD Line'].ewm(span=9, adjust=False).mean()
    data["MACD Histogram"] = data["MACD Line"] - data["Signal Line"]
    return data


