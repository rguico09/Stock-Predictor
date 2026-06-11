# functions that takes in raw OHLCV data and returns a DataFrame with engineered features

def add_moving_averages(df):

    return df

def add_macd(df):

    return df

def add_rate_of_change(df):

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
