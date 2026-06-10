# takes the raw OHLCV data of each ticker and cleans them
# and saves it to data/processed

import pandas as pd

def clean_data(ticker):
    raw_path = f"data/raw/{ticker}.csv"
    processed_path = f"data/processed/{ticker}_cleaned.csv"

    # load data, skipping the "noisy" 2nd row
    df = pd.read_csv(raw_path, header=[0, 1], index_col=0)

    # flatten the multi-index headers
    df.columns = df.columns.get_level_values(0)
    df.index.name = "date"
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    df = df.ffill()

    df.to_csv(processed_path)

ticker_symbols = ["ES=F", "NQ=F", "QQQ", "AAPL", "NVDA", "AMZN"]

for ticker in ticker_symbols:
    clean_data(ticker)
