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

def add_roc(df: pd.DataFrame, windows: list = [5, 10, 20]) -> pd.DataFrame:
    #Rate of Change
    for window in windows:
        df[f"roc_{window}"] = df["close"].pct_change(periods=window) * 100
    
    return df

def add_bolllinger_bands(df: pd.DataFrame, window: int = 20, num_std: float = 2.0) -> pd.DataFrame:
    rolling_mean = df["close"].rolling(window=window).mean()
    rolling_std = df["close"].rolling(window=window).std()

    df["bb_upper"] = rolling_mean + (num_std * rolling_std)
    df["bb_lower"] = rolling_mean - (num_std * rolling_std)
    df["bb_width"] = df["bb_upper"] - df["bb_lower"]
    df["bb_pct_b"] = (df["close"] - df["bb_lower"]) / df["bb_width"]

    return df

def add_rsi(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    # RSI measures momentum on a scale of 0-100
    # > 70 -> potentially overbought
    # < 30 -> potentially oversold
    
    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(com=window- 1, adjust=False).mean()
    avg_loss = loss.ewm(com=window - 1, adjust=False).mean()

    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))

    return df

def add_volatility(df: pd.DataFrame, windows: list = [5, 20]) -> pd.DataFrame:
    # Rolling Standard Deviation of Daily Returns

    daily_return = df["close"].pct_change()
    for window in windows:
        df[f"volatility_{window}"] = daily_return.rolling(window=window).std()

    return df

def add_atr(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    # Average True Range
    prev_close = df["close"].shift(1)
    true_range = pd.concat([
        df["high"] - df["low"],
        (df["high"] - prev_close).abs(),
        (df["low"] - prev_close).abs()
    ], axis=1).max(axis=1)

    df["atr"] = true_range.ewm(span=window, adjust=False).mean()

    return df

def add_obv(df: pd.DataFrame) -> pd.DataFrame:
    # On-Balance Volume
    direction = df["close"].diff().apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
    df["obv"] = (direction * df["volume"]).cumsum()

    return df

def add_volume_ratio(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    df["volume_ratio"] = df["volume"] / df["volume"].rolling(window=window).mean()

    return df

def add_lag_features(df: pd.DataFrame, lags: list = [1, 2, 5, 10]) -> pd.DataFrame:
    # how much the stock moved N days ago
    daily_return = df["close"].pct_change()
    for lag in lags:
        df[f"return_lag_{lag}"] = daily_return.shift(lag)

    return df

def add_calendar_features(df: pd.DataFrame) -> pd.DataFrame:
    # days of week (0=Mon, 4=Fri) and month
    df["day_of_week"] = df.index.dayofweek
    df["month"] = df.index.month

    return df

def add_all_features(df, drop_na=True):
    df = df.copy()
    
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")

    df = add_moving_averages(df)
    df = add_macd(df)
    df = add_roc(df)
    df = add_bolllinger_bands(df)
    df = add_rsi(df)
    df = add_volatility(df)
    df = add_atr(df)
    df = add_obv(df)
    df = add_volume_ratio(df)
    df = add_lag_features(df)
    df = add_calendar_features(df)

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
