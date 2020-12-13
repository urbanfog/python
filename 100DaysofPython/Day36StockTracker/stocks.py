import requests
import os


class StockGetter:

    def __init__(self, ticker: str):
        self.yesterday_price: float
        self.day_before_yesterday_price: float
        self.ticker = ticker
        self.key = os.getenv('ALPHA_VANTAGE_KEY')

    def get_stock_price(self):
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.ticker,
            "outputsize": "compact",
            "apikey": ENV_VAR,
        }

        response = requests.get(
            "https://www.alphavantage.co/query", params=params)
        response.raise_for_status()
        data = response.json()['Time Series (Daily)']
        data_list = [v for (k, v) in data.items()]

        self.yesterday_price = float(data_list[0]['4. close'])
        self.day_before_yesterday_price = float(data_list[1]['4. close'])

    def price_change(self) -> float:
        return float(
            (self.yesterday_price - self.day_before_yesterday_price) / self.day_before_yesterday_price) * 100
