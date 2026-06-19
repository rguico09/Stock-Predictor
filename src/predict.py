# a function that:
#   - loads the saved model
#   - runs inference/prediction on new data
#   - predicts the stock direction for the next trading day

import argparse
import os
import pandas as pd
import numpy as np
import joblib
from typing import Dict, Any

from src.features import add_all_features

def predict_next_day(ticker: str, model_path: str = "models/xgb_model.pkl") -> Dict[str, Any]:
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model file not found at {model_path}. "
            f"Please run model training first using: python3 -m src.model --ticker {ticker}"
        )
    
    # 1. Load the trained model
    model = joblib.load(model_path)
    
    # Get expected features from model if available
    if hasattr(model, "feature_names_in_"):
        feature_cols = list(model.feature_names_in_)
    else:
        # Fallback to general expectation
        feature_cols = None

    # 2. Load latest cleaned data
    data_path = f"data/processed/{ticker}_cleaned.csv"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Cleaned data not found at {data_path}. Please download/clean data first.")
    
    df = pd.read_csv(data_path)

    # 3. Generate all technical features
    df = add_all_features(df, drop_na=False)

    # Drop rows where features are NaN (usually the first N rows due to rolling windows)
    # We do NOT drop the last row here, as it contains the features we need to predict tomorrow
    if feature_cols is not None:
        # Only drop NaNs in the required feature columns (excluding tomorrow's target since we don't have it)
        df = df.dropna(subset=feature_cols)
    else:
        # Fallback: drop NaNs except in raw/target columns
        df = df.dropna()
        
    if df.empty:
        raise ValueError("No valid data rows remaining after feature engineering.")

    # 4. Extract the last row (most recent trading day)
    latest_row = df.iloc[[-1]]
    latest_date = latest_row.index[0]
    
    if feature_cols is not None:
        X_latest = latest_row[feature_cols]
    else:
        # Fallback
        exclude = ["open", "high", "low", "close", "volume", "target"]
        cols = [c for c in df.columns if c not in exclude]
        X_latest = latest_row[cols]

    # 5. Run inference
    pred = int(model.predict(X_latest)[0])
    prob = float(model.predict_proba(X_latest)[0][1])

    return {
        "ticker": ticker,
        "latest_trading_date": latest_date.strftime("%Y-%m-%d") if hasattr(latest_date, "strftime") else str(latest_date),
        "prediction_label": pred,
        "prediction_text": "UP" if pred == 1 else "DOWN/FLAT",
        "probability_up": prob,
        "confidence": prob if pred == 1 else 1 - prob
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run prediction for the next trading day.")
    parser.add_argument("--ticker", type=str, default="NQ=F", help="Stock ticker symbol (e.g. AAPL, NVDA, NQ=F)")
    args = parser.parse_args()

    try:
        result = predict_next_day(args.ticker)
        print(f"\n{'='*15} Prediction for {result['ticker']} {'='*15}")
        print(f"Latest Trading Date: {result['latest_trading_date']}")
        print(f"Predicted Direction: {result['prediction_text']}")
        print(f"Probability (UP): {result['probability_up']:.2%}")
        print(f"Confidence Level: {result['confidence']:.2%}")
        print(f"{'='*(36 + len(result['ticker']))}\n")
    except Exception as e:
        print(f"Error running prediction: {e}")
