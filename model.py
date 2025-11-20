"""
Credit Risk / Stock Analysis Model
----------------------------------
Functions only (no execution).
"""

import yfinance as yf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Load stock prices
# -------------------------------------------------------
def load_stock_prices(tickers: list, period="1y"):
    data = yf.download(tickers, period=period, auto_adjust=True)
    df = data.copy()
    df.columns = [f"{col}_{ticker}" for col, ticker in df.columns]
    return df.dropna()

# -------------------------------------------------------
# Calculate returns
# -------------------------------------------------------
def calculate_returns(df: pd.DataFrame):
    return df.pct_change().dropna()

# -------------------------------------------------------
# Scale numeric columns
# -------------------------------------------------------
def scale_data(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include="number").columns
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df_scaled

# -------------------------------------------------------
# Plot closing prices
# -------------------------------------------------------
def plot_closing_prices(df: pd.DataFrame, tickers: list):
    plt.figure(figsize=(12, 5))
    for t in tickers:
        col = f"Close_{t}"
        if col in df.columns:
            plt.plot(df.index, df[col], label=t)
    plt.title("Stock Closing Prices (1 Year)")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
