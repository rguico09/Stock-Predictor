# Stock Direction Predictor

A beginner-friendly end-to-end machine learning pipeline that predicts whether a stock will go **up or down** the following day. Built with Python, XGBoost, and Streamlit.

> **Disclaimer:** This project is for learning purposes only. It is not financial advice and should not be used to make real investment decisions.

---

## What it does

1. Fetches historical price data from Yahoo Finance via `yfinance`
2. Engineers technical features (moving averages, momentum, volatility, lag features)
3. Trains an XGBoost classifier using walk-forward validation (time-series safe)
4. Evaluates performance with accuracy, AUC, and F1 score
5. Serves predictions via a Streamlit dashboard

---

## Project structure

```
stock-predictor/
│
├── data/
│   ├── raw/                  # Downloaded price data (untouched)
│   └── processed/            # Engineered features, cleaned dataframes
│
├── notebooks/
│   ├── 01_testing.ipynb
│
├── src/
│   ├── raw_data.py           # Fetches data from yfinance, saves to data/raw/
|   ├── process_data.py       # Processes and cleans data, saves to data/processed
│   ├── features.py           # All feature engineering logic lives here
│   ├── model.py              # Training, walk-forward validation, saving model
│   ├── evaluate.py           # Metrics — accuracy, AUC, F1, confusion matrix
│   └── predict.py            # Load saved model, run inference on new data
│
├── app/
│   └── dashboard.py          # Streamlit dashboard (or FastAPI if doing React)
│
├── models/
│   └── xgb_model.pkl         # Saved trained model
│
├── requirements.txt
└── README.md
```

---

## Getting started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/your-username/stock-predictor.git
cd stock-predictor

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Environment variables

Create a `.env` file in the project root. If you are using the OpenAI API or any other key-based service, add it here:

```
# .env
OPENAI_API_KEY=your_key_here   # optional, only needed if extending with LLM features
```

> **Never commit `.env` to GitHub.** It is already listed in `.gitignore`.

---

## Usage

### 1. Fetch data

```bash
python src/data.py --ticker AAPL --period 5y
```

This downloads historical price data and saves it to `data/raw/AAPL.csv`.

### 2. Engineer features and train the model

Run the notebooks in order for an interactive walkthrough:

```bash
jupyter notebook notebooks/
```

Or run the pipeline directly:

```bash
python src/model.py --ticker AAPL
```

This trains the model using walk-forward validation and saves it to `models/xgb_model.pkl`.

### 3. Launch the dashboard

```bash
streamlit run app/dashboard.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser. Enter any ticker symbol and click **Run prediction**.

---

## Features engineered

### Trend / Momentum
 
| Feature | Description |
|---|---|
| `sma_5`, `sma_10`, `sma_20` | Simple moving averages over 5, 10, and 20 days |
| `ema_5`, `ema_10`, `ema_20` | Exponential moving averages — weight recent prices more heavily |
| `macd` | Difference between EMA(12) and EMA(26) — captures trend direction |
| `macd_signal` | EMA(9) of MACD — used to spot crossover signals |
| `macd_hist` | MACD minus signal line — shows momentum strength |
| `roc_5`, `roc_10`, `roc_20` | Rate of change — percentage price movement over N days |
 
### Mean Reversion
 
| Feature | Description |
|---|---|
| `rsi` | Relative Strength Index (14-day) — 0–100 scale; >70 overbought, <30 oversold |
| `bb_upper`, `bb_lower` | Bollinger Bands — rolling mean ± 2 standard deviations |
| `bb_width` | Width of the bands — proxy for current volatility |
| `bb_pct_b` | Where price sits within the bands (0 = lower, 1 = upper) |
 
### Volatility
 
| Feature | Description |
|---|---|
| `volatility_5`, `volatility_20` | Rolling standard deviation of daily returns over 5 and 20 days |
| `atr` | Average True Range (14-day) — captures daily price swing magnitude |
 
### Volume
 
| Feature | Description |
|---|---|
| `obv` | On-Balance Volume — cumulative volume weighted by price direction |
| `volume_ratio` | Today's volume relative to its 20-day average; >1 means above-average activity |
 
### Lag Features
 
| Feature | Description |
|---|---|
| `return_lag_1`, `return_lag_2` | Daily return from 1 and 2 days ago |
| `return_lag_5`, `return_lag_10` | Daily return from 5 and 10 days ago |
 
### Calendar Effects
 
| Feature | Description |
|---|---|
| `day_of_week` | Day of the week (0 = Monday, 4 = Friday) |
| `month` | Month of the year — captures seasonal patterns |

---

## Evaluation approach

Standard random train/test splits **cannot** be used for time-series data — they cause data leakage by allowing the model to indirectly learn from the future.

This project uses **walk-forward validation**: the dataset is split into `n` folds. For each fold, the model is trained on all past data and tested on the next period only. The window then slides forward. This mirrors how a real model would be deployed.

Key metrics reported per fold:

- Accuracy
- AUC (area under the ROC curve)
- F1 score

---

## Tech stack

| Purpose | Library |
|---|---|
| Data fetching | `yfinance` |
| Data wrangling | `pandas`, `numpy` |
| Modelling | `scikit-learn`, `xgboost` |
| Visualisation | `matplotlib`, `seaborn` |
| Dashboard | `streamlit` |
| Environment | `python-dotenv` |

---

## Limitations

- Stock markets are noisy. No model reliably predicts short-term price direction — this is a known-hard problem.
- The value of this project is the **pipeline and evaluation methodology**, not the predictions themselves.
- Features are intentionally simple to keep the project beginner-friendly. Real quant systems use far richer signals.

---

## Potential extensions

- Support multiple tickers with a portfolio view
- Add a React + Recharts frontend for a richer dashboard
- Experiment with LSTM or transformer-based models for sequence modelling
- Add backtesting to simulate hypothetical trades
