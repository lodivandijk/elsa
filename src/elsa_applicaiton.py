import argparse
from data_service.get_data import get_alpha_weekly, json_to_dataframe

def main():
    print("Starting elsa")
    parser = argparse.ArgumentParser(description='Process stock ticker.')
    parser.add_argument('stock_ticker', type=str, help='The stock ticker symbol')
    args = parser.parse_args()

    stock_ticker = args.stock_ticker #"IBM"
    json_data = get_alpha_weekly(stock_ticker)
    df_ticker = json_to_dataframe(json_data)
    print(df_ticker.head())
    print(df_ticker.dtypes)

if __name__ == "__main__":
    main()