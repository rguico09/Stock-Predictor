# functions to:
#   - split features and target (X, y)
#   - train a baseline model (e.g. DummyRegressor or DummyClassifier)
#   - train a RandomForestRegressor or RandomForestClassifier
#   - train an XGBRegressor or XGBClassifier
#   - evaluate and compare all 3
#   - save the best model with joblib

import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score
import xgboost as xgb

def chronological_split(ticker):
    df = pd.read_csv(f"data/processed/{ticker}_cleaned.csv")

    # features
    X = 
    # target
    y = 

    # 80/20 split
    split_idx = int(len(df) * 0.8)

    X_train, X_test = 
    y_train, y_test = 

    pass

def walk_forward_validation(ticker):
    df = pd.read_csv(f"data/processed/{ticker}_cleaned.csv")

    # features
    X = 
    # target
    y = 

    tscv = TimeSeriesSplit(n_splits=5)

    pass
