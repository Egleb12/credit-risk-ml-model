# %%
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


# %%
tickers = ["AAPL", "MSFT", "GOOG"]

df = yf.download(tickers, period="1y")

# Flatten MultiIndex columns
df.columns = ['_'.join(col).strip() for col in df.columns]

df.head()


# %%
numeric_cols = df.select_dtypes(include=np.number).columns

scaler = MinMaxScaler()
df_scaled = pd.DataFrame(
    scaler.fit_transform(df[numeric_cols]),
    columns=numeric_cols,
    index=df.index
)

df_scaled.head()


# %%
returns = df[numeric_cols].pct_change().dropna()
risk_scores = returns.std().sort_values(ascending=False)
risk_scores


# %%
plt.figure(figsize=(10,5))
for t in tickers:
    plt.plot(df.index, df[f"Close_{t}"], label=t)

plt.title("Stock Closing Prices (1 Year)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()


# %%
plt.figure(figsize=(6,4))
risk_scores.plot(kind="bar", color="orange")

plt.title("Volatility-Based Risk Score")
plt.ylabel("Standard Deviation of Returns")
plt.grid(axis="y")
plt.show()



