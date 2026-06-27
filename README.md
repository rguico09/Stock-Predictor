# Stock Direction Predictor

A machine learning pipeline that predicts whether a stock or index will go **up or down** the following trading day. Built with Python, Scikit-Learn, XGBoost, and Streamlit.

> **Disclaimer:** This project is for learning and educational purposes only. It is not financial advice and should not be used to make real investment decisions.

---

## 🏗️ What it does

1. **Ingests historical price data** from Yahoo Finance via `yfinance` ([raw_data.py](file:///Users/rianelaurenceguico/Personal/Projects/Stock%20Predictor/Stock-Predictor/src/raw_data.py)).
2. **Cleans and structures** the raw data, aligning columns and index parameters ([process_data.py](file:///Users/rianelaurenceguico/Personal/Projects/Stock%20Predictor/Stock-Predictor/src/process_data.py)).
3. **Engineers technical indicators** (momentum, mean reversion, volatility, volume ratios, return lags, and calendar effects) ([features.py](file:///Users/rianelaurenceguico/Personal/Projects/Stock%20Predictor/Stock-Predictor/src/features.py)).
4. **Trains models using walk-forward validation** (time-series safe cross-validation) and compares a baseline `DummyClassifier` against `RandomForestClassifier` and `XGBClassifier` ([model.py](file:///Users/rianelaurenceguico/Personal/Projects/Stock%20Predictor/Stock-Predictor/src/model.py)).
5. **Evaluates model performance** using Accuracy, F1-score, Confusion Matrix, and ROC-AUC metrics ([evaluate.py](file:///Users/rianelaurenceguico/Personal/Projects/Stock%20Predictor/Stock-Predictor/src/evaluate.py)).
6. **Performs standalone next-day predictions** utilising serialised weights ([predict.py](file:///Users/rianelaurenceguico/Personal/Projects/Stock%20Predictor/Stock-Predictor/src/predict.py)).
7. **Serves forecasts and charts** via a dark-theme, responsive Streamlit dashboard dashboard ([dashboard.py](file:///Users/rianelaurenceguico/Personal/Projects/Stock%20Predictor/Stock-Predictor/app/dashboard.py)).

---

## 📂 Project Structure

```
stock-predictor/
│
├── data/
│   ├── raw/                  # Downloaded price data (untouched CSV files)
│   └── processed/            # Cleaned dataframes with date indexes
│
├── src/
│   ├── raw_data.py           # Ingests raw data from yfinance
│   ├── process_data.py       # Cleans OHLCV columns and handles indexes
│   ├── features.py           # Technical indicators & feature engineering logic
│   ├── evaluate.py           # Computes classification performance metrics
│   ├── model.py              # Chronological splits, validation folds, and model training
│   └── predict.py            # Model loader and standalone next-day predictor
│
├── app/
│   └── dashboard.py          # Streamlit UI with Plotly charts and sync capabilities
│
├── models/
│   └── xgb_model.pkl         # Serialised final XGBoost Classifier model
│
├── notebooks/
│   └── 01_testing.ipynb      # Interactive testing notebook
│
├── requirements.txt          # Requirements/dependencies list
└── README.md                 # Project README (This file)
```

---

## 🚀 Getting Started

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/your-username/stock-predictor.git
cd stock-predictor

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows (cmd)

# Install dependencies
pip install -r requirements.txt
```

*Note for macOS users:* XGBoost requires the OpenMP library to run. If you run into missing library errors, run:
```bash
brew install libomp
```

---

## 💻 Usage & CLI Guide

Run the pipeline steps sequentially from the project root:

### 1. Ingest Data
```bash
python3 src/raw_data.py
```
This fetches 5 years of daily data for default tickers (`AAPL`, `NVDA`, `AMZN`, `QQQ`, `NQ=F`, `ES=F`) and saves them to `data/raw/`.

### 2. Clean & Format Data
```bash
python3 src/process_data.py
```
Cleans row inconsistencies, structures headers, indexes on dates, and saves files to `data/processed/`.

### 3. Train Model
```bash
python3 -m src.model --ticker AAPL
```
Runs 5-fold walk-forward cross-validation on the training set, prints performance metrics comparisons for Baseline vs. Random Forest vs. XGBoost, fits the final XGBoost model, prints holdout test results, and serialises the model to `models/xgb_model.pkl`.

### 4. Standalone Predict
```bash
python3 -m src.predict --ticker AAPL
```
Loads `models/xgb_model.pkl`, structures features for the latest trading day, and returns next-day direction, probability, and confidence.

### 5. Launch the Dashboard
```bash
python3 -m streamlit run app/dashboard.py
```
Launches the interactive dashboard in your default browser at `http://localhost:8501`.

---

## 📊 Technical Indicators Engineered

* **Moving Averages**: 5, 10, and 20-day Simple (SMA) and Exponential (EMA) values.
* **Momentum**: MACD Line, Signal Line, Histogram, and Rate of Change (ROC 5, 10, 20 days).
* **Mean Reversion**: RSI (14-day) and Bollinger Bands (20-day width, %b position).
* **Volatility**: Rolling standard deviations of daily returns (5, 20 days) and Average True Range (ATR).
* **Volume**: On-Balance Volume (OBV) and volume ratio (current volume vs 20-day average).
* **Lags & Calendar**: Multi-day return lags (1, 2, 5, 10 days), day of the week, and month of the year.

---

## 📈 Evaluation Approach

Time-series data cannot use randomised splits since they cause **data leakage** by letting models look into the future. 

Instead, this project implements a strict time-ordered pipeline:
1. **Chronological Splitting**: 80% of historical data is used for training/validation, and the remaining 20% is set aside as an unseen test holdout.
2. **Walk-Forward Validation**: Inside the 80% training set, `TimeSeriesSplit` splits the data into 5 moving chronological folds. For each fold, models are trained on past data and validated on the subsequent segment.

---

## 💡 Potential Extensions

* Support multiple tickers with a portfolio view.
* Add a React + Recharts frontend for a richer, customised dashboard interface.
* Experiment with LSTM or Transformer-based deep learning models for time-series forecasting.
* Add backtesting logic to simulate hypothetical trade entries and performance metrics over time.
