import requests
import pandas as pd

request_alpha = "https://www.alphavantage.co/query?function="
series_type = "TIME_SERIES_WEEKLY"
ticker_prefix = "&symbol="
api_alpha_key = "&apikey=CBU3HK62CDA53MJU"

def get_alpha_weekly(stock_ticker):
    url = request_alpha + series_type + ticker_prefix+ stock_ticker +api_alpha_key
    response = requests.get(url)
    data = response.json()
    return data

def json_to_dataframe(json_data):
    time_series = json_data.get("Weekly Time Series", {})
    data = [{"date": date, "close": float(values["4. close"])} for date, values in time_series.items()]
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    return df