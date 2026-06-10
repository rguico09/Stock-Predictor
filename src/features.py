# a function that takes in raw OHLCV data and returns a DataFrame with engineered features

# features such as:
#   - lag returns: % price change over a period of time (1, 5, 10, 20 days etc.)
#   - rolling means: e.g. 10-day / 50-day SMA
#   - rolling volatility: e.g. 10-day standard deviation of returns
#   - volume change: % change in volume vs. previous day

