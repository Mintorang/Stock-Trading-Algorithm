import alpaca_trade_api as tradeapi
from constants import API_KEY, API_SECRET, BASE_URL
# authentication and connection details


def order(api_key, api_secret, base_url, quantity, bs):
    # instantiate REST API
    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
    account = api.get_account()
    # obtain account information
    account = api.get_account()
    api.submit_order(
        symbol='CVX',
        qty=quantity,
        side=f"{bs}",
        type='market',
        time_in_force='gtc'
    )
    print(f"Succesfully {bs} {quantity} shares of CVX!")
    


