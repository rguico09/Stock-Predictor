import yfinance as yf
import pandas as pd
import datetime


# ticker (symbol), period (time in years)
def load_data(ticker, period):
    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(period*365)
    
    data = yf.download(ticker, start=start_date, end=end_date)
    df = pd.DataFrame(data)

    return df

# can change tickers according to what you want
ticker_symbols = ["ES=F", "NQ=F", "QQQ", "AAPL", "NVDA", "AMZN"]

for ticker in ticker_symbols:
    file_path = f"data/raw/{ticker}.csv"
        
    df = pd.DataFrame(load_data(ticker, 5))
    df = df.reset_index()
    df.to_csv(file_path, index=False)
