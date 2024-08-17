import requests
import json

url = 'https://www.alphavantage.co/'
SYMBOL = 'AAPL'
API_KEY = 'XDCQCRJWCBKUTU8N'
#query?function=TIME_SERIES_DAILY&symbol=AAPL&interval=5min&apikey=XDCQCRJWCBKUTU8N'

def _get_stock_prices(url, symbol, api_key):
    url = f"{url}query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url=url).json()
    data = response['Time Series (Daily)']
    return data

_get_stock_prices(
    url,
    SYMBOL,
    API_KEY
)
