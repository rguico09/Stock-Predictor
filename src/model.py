# functions to:
#   - split features and target (X, y)
#   - train a baseline model (e.g. DummyRegressor or DummyClassifier)
#   - train a RandomForestRegressor or RandomForestClassifier
#   - train an XGBRegressor or XGBClassifier
#   - evaluate and compare all 3
#   - save the best model with joblib

import os
import argparse
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
import xgboost as xgb

from src.features import add_all_features
from src.evaluate import calculate_metrics, print_evaluation_summary

def chronological_split(ticker: str):
    # Load data
    df = pd.read_csv(f"data/processed/{ticker}_cleaned.csv")
    
    # Add features (keep NaNs for now to avoid premature dropping)
    df = add_all_features(df, drop_na=False)

    # Define target: 1 if tomorrow's close is higher than today's close, 0 otherwise
    df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)

    # Drop any remaining NaNs (e.g., indicator warm-up periods and the last row)
    df = df.dropna()

    # Define features X and target y
    feature_cols = [col for col in df.columns if col not in ["open", "high", "low", "close", "volume", "target"]]
    X = df[feature_cols]
    y = df["target"]

    # 80/20 split
    split_idx = int(len(df) * 0.8)

    X_train = X.iloc[:split_idx]
    X_test = X.iloc[split_idx:]
    y_train = y.iloc[:split_idx]
    y_test = y.iloc[split_idx:]

    return X_train, X_test, y_train, y_test

def walk_forward_validation(ticker: str):
    X_train, _, y_train, _ = chronological_split(ticker)

    tscv = TimeSeriesSplit(n_splits=5)

    # Define candidate models
    models = {
        "Baseline (Dummy)": DummyClassifier(strategy="most_frequent", random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42),
        "XGBoost": xgb.XGBClassifier(
            n_estimators=100, 
            max_depth=3, 
            learning_rate=0.05, 
            random_state=42, 
            eval_metric="logloss"
        )
    }

    # Dict to collect fold metrics
    fold_results = {name: [] for name in models}

    print(f"\nRunning 5-Fold Walk-Forward Validation on Training Data for {ticker}...")
    print("-" * 75)

    for fold, (train_idx, val_idx) in enumerate(tscv.split(X_train)):
        X_tr, X_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
        y_tr, y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]

        print(f"\n--- Fold {fold + 1} ---")
        for name, model in models.items():
            model.fit(X_tr, y_tr)
            preds = model.predict(X_val)
            probs = model.predict_proba(X_val)[:, 1] if hasattr(model, "predict_proba") else None
            
            metrics = calculate_metrics(y_val, preds, probs)
            fold_results[name].append(metrics)
            
            auc_val = f"{metrics['roc_auc']:.4f}" if metrics.get('roc_auc') is not None else "N/A"
            print(f"  {name:16s} | Accuracy: {metrics['accuracy']:.4f} | F1: {metrics['f1_score']:.4f} | AUC: {auc_val}")

    # Compute and print averages
    print("\n" + "="*20 + " Walk-Forward Validation Summary " + "="*20)
    avg_results = {}
    for name in models:
        avg_acc = np.mean([r["accuracy"] for r in fold_results[name]])
        avg_f1 = np.mean([r["f1_score"] for r in fold_results[name]])
        
        auc_list = [r["roc_auc"] for r in fold_results[name] if r.get("roc_auc") is not None]
        avg_auc = np.mean(auc_list) if auc_list else None
        
        avg_results[name] = {"accuracy": avg_acc, "f1_score": avg_f1, "roc_auc": avg_auc}
        auc_str = f"{avg_auc:.4f}" if avg_auc is not None else "N/A"
        print(f"{name:16s} | Avg Accuracy: {avg_acc:.4f} | Avg F1: {avg_f1:.4f} | Avg AUC: {auc_str}")
    print("=" * 73)

    return avg_results

def train_and_save_best_model(ticker: str):
    X_train, X_test, y_train, y_test = chronological_split(ticker)

    # 1. Run Walk-Forward Validation
    avg_results = walk_forward_validation(ticker)
    
    # Save validation metrics to JSON
    os.makedirs("models", exist_ok=True)
    import json
    with open("models/evaluation_metrics.json", "w") as f:
        json.dump(avg_results, f)

    # 2. Train final XGBoost model on all training data
    print(f"\nTraining final XGBoost model on all training data for {ticker}...")
    final_model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.05,
        random_state=42,
        eval_metric="logloss"
    )
    final_model.fit(X_train, y_train)

    # 3. Evaluate on unseen test data
    test_preds = final_model.predict(X_test)
    test_probs = final_model.predict_proba(X_test)[:, 1]
    
    test_metrics = calculate_metrics(y_test, test_preds, test_probs)
    print_evaluation_summary(test_metrics, f"Final XGBoost Test Set Evaluation ({ticker})")

    # 4. Save model
    os.makedirs("models", exist_ok=True)
    model_path = f"models/xgb_model.pkl"
    joblib.dump(final_model, model_path)
    print(f"\nModel successfully saved to {model_path}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train and evaluate stock direction prediction models.")
    parser.add_argument("--ticker", type=str, default="NQ=F", help="Stock ticker symbol (e.g. AAPL, NVDA, NQ=F)")
    args = parser.parse_args()

    train_and_save_best_model(args.ticker)
