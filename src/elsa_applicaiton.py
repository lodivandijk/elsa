import src.service.get_data as av
import src.model.SplitData as sd
import src.model.WindowGenerator as wg
import logging
import argparse
import tensorflow as tf
import numpy as np

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

    # Stack three slices, the length of the total window.
    example_window = tf.stack([np.array(split_data.train_df[:window.total_window_size]),
                               np.array(split_data.train_df[100:100+window.total_window_size]),
                               np.array(split_data.train_df[200:200+window.total_window_size])])

    example_inputs, example_labels = window.split_window(example_window)

    logging.info('All shapes are: (batch, time, features)')
    logging.info(f'Window shape: {example_window.shape}')
    logging.info(f'Inputs shape: {example_inputs.shape}')
    logging.info(f'Labels shape: {example_labels.shape}')

if __name__ == "__main__":
    main()