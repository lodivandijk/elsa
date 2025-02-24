import src.service.get_data as av
import src.model.SplitData as sd
import src.model.WindowGenerator as wg
import logging
import argparse
import tensorflow as tf
import src.model.Baseline as bl
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

    single_step_window = wg.WindowGenerator(
        input_width=1, label_width=1, shift=1, split_data=split_data,
        label_columns=['close'])

    baseline = bl.Baseline(label_index=single_step_window.column_indices['close'])

    baseline.compile(loss=tf.keras.losses.MeanSquaredError(),
                     metrics=[tf.keras.metrics.MeanAbsoluteError()])

    val_performance = {}
    performance = {}
    val_performance['Baseline'] = baseline.evaluate(single_step_window.val, return_dict=True)
    performance['Baseline'] = baseline.evaluate(single_step_window.test, verbose=0, return_dict=True)

if __name__ == "__main__":
    main()