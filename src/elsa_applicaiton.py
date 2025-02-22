import src.service.get_data as av

def main():
    API_KEY = "CBU3HK62CDA53MJU"
    alpha_vantage = av.AlphaVantageAPI(API_KEY)

    daily_data = alpha_vantage.get_weekly_stock_prices("AAPL")
    print(daily_data.head())

if __name__ == "__main__":
    main()