import src.service.get_data as av
import src.model.SplitData as sd
import src.model.WindowGenerator as wg
import logging
import argparse

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='API key')
    parser.add_argument('api_key', type=str, help='Alphavantage API key')
    args = parser.parse_args()

    API_KEY = args.api_key
    alpha_vantage = av.AlphaVantageAPI(API_KEY)

    stock_data = alpha_vantage.get_weekly_stock_prices("AAPL")
    logging.info(f"Stock data shape: {stock_data.shape}")

    split_data = sd.SplitData(stock_data)

    logging.info(f"{split_data}")

    window = wg.WindowGenerator(input_width=120, label_width=1, shift=1, split_data=split_data, label_columns=['close'])
    logging.info(f"Window details \n {window}")
    
if __name__ == "__main__":
    main()