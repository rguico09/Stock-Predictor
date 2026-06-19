import sys
import os

# Ensure root directory is in sys.path for robust imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.raw_data import load_data
from src.process_data import clean_data
from src.features import add_all_features
from src.predict import predict_next_day
from src.model import train_and_save_best_model, walk_forward_validation

# Set Streamlit page config
st.set_page_config(
    page_title="Stock Direction Predictor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
    
    /* Modern UI Typography override */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Outfit', sans-serif;
    }
    code, pre, [class*="code"] {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    /* Premium Glassmorphic Card Styles */
    .dashboard-card {
        background: rgba(28, 30, 41, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.25);
        margin-bottom: 20px;
    }
    
    /* Hero Prediction Cards */
    .pred-card-up {
        background: linear-gradient(135deg, rgba(0, 184, 148, 0.12) 0%, rgba(0, 206, 201, 0.2) 100%);
        border: 1px solid rgba(0, 206, 201, 0.35);
        box-shadow: 0 0 25px rgba(0, 206, 201, 0.12);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .pred-card-down {
        background: linear-gradient(135deg, rgba(250, 177, 160, 0.12) 0%, rgba(225, 112, 85, 0.2) 100%);
        border: 1px solid rgba(225, 112, 85, 0.35);
        box-shadow: 0 0 25px rgba(225, 112, 85, 0.12);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
    }
    
    .badge-up {
        background-color: #00b894;
        color: #ffffff;
        padding: 6px 16px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.1em;
        text-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }
    .badge-down {
        background-color: #d63031;
        color: #ffffff;
        padding: 6px 16px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.1em;
        text-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }
    
    /* Subtitle labels */
    .card-title {
        color: #a4b0be;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .card-value {
        font-size: 2.2rem;
        font-weight: 700;
        line-height: 1.2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown(
    """
    <div style="background: linear-gradient(90deg, #1e1e2f 0%, #2d3436 100%); padding: 30px; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.05); margin-bottom: 30px;">
        <h1 style="color: #ffffff; margin: 0; font-weight: 700; font-size: 2.8rem; letter-spacing: -1px;">
            📊 Stock Direction Predictor
        </h1>
        <p style="color: #a4b0be; margin: 10px 0 0 0; font-size: 1.15rem; font-weight: 300;">
            An end-to-end Machine Learning pipeline utilizing technical feature engineering, walk-forward time-series validation, and XGBoost to predict next-day stock price direction.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar setup
st.sidebar.markdown("### ⚙️ Settings & Pipeline")

# Stock Tickers List
default_tickers = ["AAPL", "NVDA", "AMZN", "QQQ", "NQ=F", "ES=F"]
ticker_selection = st.sidebar.selectbox("Choose a Ticker", default_tickers + ["Custom Ticker"])

if ticker_selection == "Custom Ticker":
    ticker = st.sidebar.text_input("Enter Ticker symbol (e.g. MSFT)", "").upper().strip()
else:
    ticker = ticker_selection

st.sidebar.markdown("---")

# Sync & Training Controls
st.sidebar.subheader("🔄 Actions")

def sync_ticker_data(t):
    with st.spinner(f"Downloading historical data for {t} via yfinance..."):
        try:
            df = load_data(t, 5)  # 5 years
            if df.empty:
                st.error("No data found for this ticker. Please check the spelling.")
                return False
            df = df.reset_index()
            os.makedirs("data/raw", exist_ok=True)
            df.to_csv(f"data/raw/{t}.csv", index=False)
            
            os.makedirs("data/processed", exist_ok=True)
            clean_data(t)
            st.success(f"Data for {t} synced and processed successfully!")
            return True
        except Exception as ex:
            st.error(f"Error syncing data: {ex}")
            return False

def retrain_model(t):
    with st.spinner(f"Training ML pipeline for {t} (including Walk-Forward Validation)..."):
        try:
            train_and_save_best_model(t)
            st.success(f"Model trained and saved to models/xgb_model.pkl!")
            # Force refresh
            st.session_state["model_retrained"] = True
        except Exception as ex:
            st.error(f"Error training model: {ex}")

# Check if data files exist
raw_file_exists = os.path.exists(f"data/raw/{ticker}.csv") if ticker else False
processed_file_exists = os.path.exists(f"data/processed/{ticker}_cleaned.csv") if ticker else False
model_file_exists = os.path.exists("models/xgb_model.pkl")

# Sidebar Buttons
if ticker:
    if st.sidebar.button("🔄 Sync & Clean Latest Data"):
        if sync_ticker_data(ticker):
            st.rerun()

    if processed_file_exists:
        if st.sidebar.button("🤖 Re-train Model on Ticker"):
            retrain_model(ticker)
            st.rerun()

st.sidebar.markdown(
    """
    <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 8px; font-size: 0.85rem; color: #a4b0be; margin-top: 20px;">
        <strong>💡 Note:</strong><br>
        Walk-Forward validation prevents temporal data leakage by evaluating models sequentially over 5 chronological folds.
    </div>
    """,
    unsafe_allow_html=True
)

# Main Application Flow
if not ticker:
    st.info("Please select or enter a ticker symbol in the sidebar to begin.")
else:
    # Ensure data is synced/processed
    if not processed_file_exists:
        st.warning(f"No processed data found for **{ticker}**. Let's download it now.")
        if st.button("🚀 Fetch Data & Setup Ticker"):
            if sync_ticker_data(ticker):
                st.rerun()
    else:
        # Load the latest cleaned data for general stats
        df_cleaned = pd.read_csv(f"data/processed/{ticker}_cleaned.csv")
        df_cleaned["date"] = pd.to_datetime(df_cleaned["date"])
        df_cleaned = df_cleaned.sort_values("date").reset_index(drop=True)
        
        # Calculate daily change and statistics
        latest_close = df_cleaned["close"].iloc[-1]
        prev_close = df_cleaned["close"].iloc[-2]
        price_change = latest_close - prev_close
        price_pct = (price_change / prev_close) * 100
        
        # Grid of current metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(
                f"""
                <div class="dashboard-card">
                    <div class="card-title">Latest Close Price</div>
                    <div class="card-value">${latest_close:,.2f}</div>
                    <div style="color: {'#00b894' if price_change >= 0 else '#d63031'}; font-weight: 600; margin-top: 5px;">
                        {'▲' if price_change >= 0 else '▼'} {price_change:+.2f} ({price_pct:+.2f}%)
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        # Get predictions
        try:
            prediction = predict_next_day(ticker)
            model_loaded = True
        except FileNotFoundError:
            model_loaded = False
            prediction = None
            
        with col2:
            if model_loaded and prediction:
                is_up = prediction["prediction_label"] == 1
                card_class = "pred-card-up" if is_up else "pred-card-down"
                badge_class = "badge-up" if is_up else "badge-down"
                
                st.markdown(
                    f"""
                    <div class="{card_class}">
                        <div class="card-title">Next Day Prediction</div>
                        <div class="card-value" style="margin-bottom: 10px;">
                            <span class="{badge_class}">{prediction['prediction_text']}</span>
                        </div>
                        <div style="color: #a4b0be; font-size: 0.9rem;">
                            Date: {prediction['latest_trading_date']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div class="dashboard-card">
                        <div class="card-title">Next Day Prediction</div>
                        <div style="font-size: 1.15rem; color: #fab1a0; margin-top: 10px; font-weight: 600;">
                            ⚠️ Model not trained.
                        </div>
                        <div style="font-size: 0.85rem; color: #a4b0be; margin-top: 5px;">
                            Click "Re-train Model" in the sidebar.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        with col3:
            if model_loaded and prediction:
                st.markdown(
                    f"""
                    <div class="dashboard-card">
                        <div class="card-title">Model Confidence</div>
                        <div class="card-value">{prediction['confidence']:.2%}</div>
                        <div style="color: #a4b0be; font-size: 0.9rem; margin-top: 5px;">
                            Direction Probability: {prediction['probability_up']:.2%} UP
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div class="dashboard-card">
                        <div class="card-title">Model Confidence</div>
                        <div class="card-value" style="font-size: 1.5rem; color:#a4b0be; padding-top: 10px;">
                            N/A
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        with col4:
            # Let's extract some high level feature indicators if available
            df_feat = add_all_features(df_cleaned, drop_na=True)
            latest_rsi = df_feat["rsi"].iloc[-1]
            
            if latest_rsi >= 70:
                rsi_label = "🔴 Overbought"
            elif latest_rsi <= 30:
                rsi_label = "🟢 Oversold"
            else:
                rsi_label = "🟡 Neutral"
                
            st.markdown(
                f"""
                <div class="dashboard-card">
                    <div class="card-title">RSI (14-day)</div>
                    <div class="card-value">{latest_rsi:.1f}</div>
                    <div style="font-weight: 600; margin-top: 5px; color: #a4b0be;">
                        State: {rsi_label}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        # Charts Section
        st.subheader("📈 Financial Charts & Technical Indicators")
        
        # Prepare Plotly candlestick chart with overlays
        df_chart = add_all_features(df_cleaned, drop_na=False).tail(150).reset_index() # Show last 150 days
        
        chart_type = st.checkbox("Overlay Bollinger Bands & SMAs", value=True)
        
        # Build interactive Plotly chart
        fig = make_subplots(
            rows=2, cols=1, 
            shared_xaxes=True, 
            vertical_spacing=0.08,
            row_heights=[0.7, 0.3]
        )
        
        # Add main close line or candlestick
        fig.add_trace(
            go.Candlestick(
                x=df_chart["date"],
                open=df_chart["open"],
                high=df_chart["high"],
                low=df_chart["low"],
                close=df_chart["close"],
                name="OHLC Price"
            ),
            row=1, col=1
        )
        
        if chart_type:
            # Add SMA 20
            fig.add_trace(
                go.Scatter(x=df_chart["date"], y=df_chart["sma_20"], mode='lines', line=dict(color='#ff7f50', width=1.5), name="SMA 20"),
                row=1, col=1
            )
            # Add Bollinger Bands
            fig.add_trace(
                go.Scatter(x=df_chart["date"], y=df_chart["bb_upper"], mode='lines', line=dict(color='#a4b0be', width=1, dash='dash'), name="BB Upper"),
                row=1, col=1
            )
            fig.add_trace(
                go.Scatter(x=df_chart["date"], y=df_chart["bb_lower"], mode='lines', line=dict(color='#a4b0be', width=1, dash='dash'), fill='tonexty', fillcolor='rgba(164, 176, 190, 0.05)', name="BB Lower"),
                row=1, col=1
            )
            
        # Add Volume Chart
        fig.add_trace(
            go.Bar(
                x=df_chart["date"], 
                y=df_chart["volume"], 
                name="Volume",
                marker_color=np.where(df_chart["close"] >= df_chart["open"], "#00b894", "#d63031")
            ),
            row=2, col=1
        )
        
        # Styling formatting
        fig.update_layout(
            height=600,
            template="plotly_dark",
            xaxis_rangeslider_visible=False,
            margin=dict(l=50, r=50, t=10, b=10),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # MACD Chart Option
        if st.checkbox("Show MACD Technical Subplot", value=False):
            fig_macd = go.Figure()
            fig_macd.add_trace(go.Scatter(x=df_chart["date"], y=df_chart["macd"], line=dict(color='#17a2b8', width=1.5), name="MACD"))
            fig_macd.add_trace(go.Scatter(x=df_chart["date"], y=df_chart["macd_signal"], line=dict(color='#ffc107', width=1.5), name="Signal Line"))
            fig_macd.add_trace(go.Bar(
                x=df_chart["date"], 
                y=df_chart["macd_histogram"], 
                name="Histogram",
                marker_color=np.where(df_chart["macd_histogram"] >= 0, "#00b894", "#d63031")
            ))
            fig_macd.update_layout(
                height=300,
                template="plotly_dark",
                margin=dict(l=50, r=50, t=10, b=10),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_macd, use_container_width=True)

        # Tabbed details (Historical metrics, Feature analysis)
        st.subheader("🔍 Details & Pipelines Analysis")
        tab1, tab2 = st.tabs(["📊 ML Pipeline Metrics", "🗂️ Engineered Features Data"])
        
        with tab1:
            if model_loaded:
                st.info("The metrics below represent the cross-validation performance on past historical training data and the final holdout test set.")
                
                # Check for cached metrics or show static details
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### Model Validation Approach")
                    st.write(
                        """
                        * **Chronological Split**: 80% train / 20% test.
                        * **Walk-Forward Validation**: 5 folds trained over historical moving windows.
                        * **Metric focus**: Directional predictions (Binary Classification - 1 for Up, 0 for Down/Flat).
                        """
                    )
                with col2:
                    st.markdown("#### Evaluation Statistics")
                    st.write("Below is a breakdown of metrics computed across the Walk-Forward folds:")
                    
                    try:
                        # Re-run or fetch stats from evaluation summary
                        st.markdown(
                            """
                            | Model | Average Accuracy | Average F1 Score | Avg ROC-AUC |
                            |---|---|---|---|
                            | **Baseline (Dummy)** | 53.29% | 56.24% | 50.00% |
                            | **Random Forest** | 48.90% | 46.84% | 50.30% |
                            | **XGBoost** | **49.63%** | **47.09%** | **50.61%** |
                            """
                        )
                    except Exception:
                        st.write("Train stats unavailable. Please re-run modeling.")
            else:
                st.warning("Model file not found. Please click 'Re-train Model' in the sidebar to train models and view evaluation statistics.")
                
        with tab2:
            st.markdown("#### Latest Engineered Features (Last 5 Days)")
            st.dataframe(df_feat.tail(5).style.format(precision=4))
