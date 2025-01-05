import alpaca_trade_api as tradeapi

# authentication and connection details
api_key = "PK4WAX1FXZ9DF7DAHFAH"
api_secret = 'kqgqeCt2CI07OgMC2eyo84W6hyMuoNRpVJg0nvjX'
base_url = 'https://paper-api.alpaca.markets'

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# obtain account information
account = api.get_account()
api.submit_order(
    symbol='CVX',
    qty=100,
    side='buy',
    type='market',
    time_in_force='gtc'
)
