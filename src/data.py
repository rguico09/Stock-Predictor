import yfinance as yf
import pandas as pd
import datetime
import os


def load_data(ticker):
    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(5*365)
    
    data = yf.download(ticker, start=start_date, end=end_date)
    df = pd.DataFrame(data)

    return df


ticker_symbols = ["ES=F", "NQ=F", "QQQ", "AAPL", "NVDA", "AMZN"]

for ticker in ticker_symbols:
    file_path = f"/Users/rianelaurenceguico/Personal/Projects/Stock Predictor/Stock-Predictor/data/raw/{ticker}.csv"
    
    if os.path.exists(file_path):
        continue
        
    df = pd.DataFrame(load_data(ticker))
    df.to_csv(file_path, index=False)