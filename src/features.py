# functions that takes in raw OHLCV data and returns a DataFrame with engineered features

import pandas as pd
import numpy as np

def add_moving_averages(df: pd.DataFrame) -> pd.DataFrame:
    # SMA and EMA
    for window in [5, 10, 20]:
        df[f"sma_{window}"] = df["close"].rolling(window=window).mean()
        df[f"ema_{window}"] = df["close"].ewm(span=window, adjust=False).mean()

    return df

def add_macd(df: pd.DataFrame) -> pd.DataFrame:
    # MACD = EMA(12) - EMA(26)
    # Signal line = EMA(9) of MACD
    # Histogram = MACD - Signal

    ema_12 = df["close"].ewm(span=12, adjust=False).mean()
    ema_26 = df["close"].ewm(span=26, adjust=False).mean()

    df["macd"] = ema_12 - ema_26
    df["macd_signal"] = df["macd"].ewm(span=9, adjust=False).mean()
    df["macd_histogram"] = df["macd"] - df["macd_signal"]

    return df

def add_rate_of_change(df: pd.DataFrame, windows: list = [5, 10, 20]) -> pd.DataFrame:
    for window in windows:
        df[f"roc_{window}"] = df["close"].pct_change(periods=window) * 100
    
    return df

def add_bolllinger_bands(df):

    return df

def add_rsi(df):

    return df

def add_volatility(df):

    return df

def add_atr(df):

    return df

def add_obv(df):

    return df

def add_volume_ratio(df):

    return df

def add_lag_features(df):

    return df

def add_calendar_features(df):

    return df

def add_all_features(df, drop_na=True):
    df = df.copy()

    df = add_moving_averages(df)
    df = add_macd(df)
    df = add_rate_of_change(df)
    #df = add_bolllinger_bands(df)
    #df = add_rsi(df)
    #df = add_volatility(df)
    #df = add_atr(df)
    #df = add_obv(df)
    #df = add_volume_ratio(df)
    #df = add_lag_features(df)
    #df = add_calendar_features(df)

    if drop_na:
        df.dropna(inplace=True)

    return df

if __name__ == "__main__":
    # TESTING
    raw = pd.read_csv("data/processed/NQ=F_cleaned.csv")
    featured = add_all_features(raw)

    print(f"Shape: {featured.shape}")
    print(f"\nFeature columns:\n{[c for c in featured.columns if c not in ['Open','High','Low','Close','Volume']]}")
    print(featured)
