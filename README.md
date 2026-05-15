# Stock Market Clustering — Unsupervised ML

An unsupervised machine learning project that discovers natural sector groupings across 90 global stocks (Indian NSE + US S&P 500) using K-Means clustering, PCA visualization, and real-world financial analysis tools.

---

## What This Project Does

No labels. No sector information given. The machine discovered everything on its own.

Given 90 stocks and 237 days of price data, the model identified 7 natural market sectors purely from return behaviour patterns — Indian Stocks, US Tech, US Healthcare, US Finance & Energy, US Consumer, Fintech, and High Risk / Volatile stocks.

---

## Features

**Portfolio Builder**
Automatically picks one stock from each cluster — guaranteed diversification across sectors. Run it multiple times to generate different portfolios.

**Stock Risk Detector**
Assigns a risk score to every stock based on cluster size. Smaller cluster = more unique behaviour = higher risk. LYFT scores 1.0 (maximum risk). Indian stocks score 0.03 (most stable).

**Market Crash Analyser**
Enter any stock name. Instantly see which other stocks are most likely to crash with it — all stocks in the same cluster move together.

**Sector Discovery Dashboard**
A 2D PCA map of the entire stock universe with sector labels, colour coding, and stock name annotations.

---

## Tech Stack

- Python
- yfinance — stock data download
- pandas, numpy — data processing
- scikit-learn — KMeans, PCA, StandardScaler
- matplotlib — visualization
- pickle — model saving

---

## Results

| Cluster | Sector | Stocks | Risk Score |
|---------|--------|--------|------------|
| 0 | Indian Stocks | 32 | 0.03 |
| 1 | US Tech | 14 | 0.07 |
| 2 | US Healthcare | 8 | 0.12 |
| 3 | Fintech | 2 | 0.50 |
| 4 | US Finance & Energy | 18 | 0.06 |
| 5 | US Consumer | 15 | 0.07 |
| 6 | High Risk / Volatile | 1 | 1.00 |

---

## How to Run

```bash
pip install yfinance scikit-learn pandas numpy matplotlib
python data.py        # download stock data
jupyter notebook      # open and run the notebook
```

---

## Key Learnings

- Used daily returns instead of raw prices to handle currency differences (INR vs USD)
- Applied StandardScaler before clustering to normalise volatility differences
- Transposed the data matrix so stocks become rows and days become features
- Used Elbow Method to find optimal K=7
- Applied PCA to compress 236-dimensional data to 2D for visualization

---

## Next Steps

This project clusters stocks by historical behaviour. The next version will use **LSTM (Long Short-Term Memory)** neural networks for actual stock price prediction — a time series approach that respects the sequential nature of market data.

---

## Project Structure

```
stock-market-clustering-unsupervised-ml/
├── data.py               # download 90 stocks via yfinance
├── stocks_100.csv        # raw stock price data
├── notebook.ipynb        # full analysis notebook
├── stock_model.pkl       # saved model, scaler, PCA, labels
└── README.md
```
