import requests
import pandas as pd

class AlphaVantageAPI:
    BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weekly_stock_prices(self, symbol, output_size="full"):
        """
        Fetches daily stock prices.
        :param symbol: Stock ticker symbol (e.g., "AAPL").
        :param output_size: "compact" (last 100 days) or "full" (all historical data).
        :return: Pandas DataFrame with daily stock prices.
        """
        params = {
            "function": "TIME_SERIES_WEEKLY",
            "symbol": symbol,
            "apikey": self.api_key,
            "outputsize": output_size
        }

        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if "Weekly Time Series" in data:
            df = pd.DataFrame.from_dict(data["Weekly Time Series"], orient="index")
            df = df.rename(columns={
                "1. open": "open",
                "2. high": "high",
                "3. low": "low",
                "4. close": "close",
                "5. volume": "volume"
            })
            df = df.astype(float)  # Convert to float values
            df.index = pd.to_datetime(df.index)  # Convert index to datetime
            df = df.sort_index()  # Sort by date
            return df
        else:
            raise ValueError("Error fetching data. Check API key and symbol.")

