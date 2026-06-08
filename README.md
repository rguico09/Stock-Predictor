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
│   ├── 01_exploration.ipynb  # EDA — plot prices, check for nulls
│   ├── 02_features.ipynb     # Experiment with feature engineering
│   └── 03_modelling.ipynb    # Train, evaluate, compare models
│
├── src/
│   ├── data.py               # Fetches data from yfinance
│   ├── features.py           # All feature engineering logic
│   ├── model.py              # Training and walk-forward validation
│   ├── evaluate.py           # Metrics — accuracy, AUC, F1
│   └── predict.py            # Load saved model and run inference
│
├── app/
│   └── dashboard.py          # Streamlit dashboard
│
├── models/
│   └── xgb_model.pkl         # Saved trained model
│
├── requirements.txt
├── .env                      # API keys — never commit this to GitHub
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

| Feature | Description |
|---|---|
| `ma_7` | 7-day rolling average of closing price |
| `ma_30` | 30-day rolling average of closing price |
| `momentum` | 5-day percentage change in price |
| `volatility` | 14-day rolling standard deviation |
| `lag_1` | Closing price from 1 day ago |
| `target` | Binary label — 1 if tomorrow's close > today's close |

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

- Add RSI and MACD as additional technical indicators
- Support multiple tickers with a portfolio view
- Add a React + Recharts frontend for a richer dashboard
- Experiment with LSTM or transformer-based models for sequence modelling
- Add backtesting to simulate hypothetical trades

---

## License

MIT — free to use, modify, and distribute.
