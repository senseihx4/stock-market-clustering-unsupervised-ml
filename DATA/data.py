import yfinance as yf
import pandas as pd

tickers = [
    # US Tech
    'AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META', 'NVDA', 'TSLA', 'NFLX', 'AMD', 'INTC',
    'CRM', 'ORCL', 'ADBE', 'PYPL', 'UBER', 'LYFT', 'SNAP', 'TWTR', 'SQ', 'SHOP',

    # US Finance
    'JPM', 'BAC', 'GS', 'WFC', 'MS', 'C', 'AXP', 'BLK', 'SCHW', 'COF',

    # US Healthcare
    'JNJ', 'PFE', 'UNH', 'ABBV', 'MRK', 'TMO', 'ABT', 'BMY', 'AMGN', 'GILD',

    # US Energy
    'XOM', 'CVX', 'BP', 'COP', 'SLB', 'EOG', 'PXD', 'MPC', 'VLO', 'PSX',

    # US Consumer
    'WMT', 'TGT', 'COST', 'MCD', 'SBUX', 'NKE', 'DIS', 'CMCSA', 'PG', 'KO',

    # Indian IT
    'INFY.NS', 'TCS.NS', 'WIPRO.NS', 'HCLTECH.NS', 'TECHM.NS',
    'MPHASIS.NS', 'LTIM.NS', 'PERSISTENT.NS', 'COFORGE.NS', 'OFSS.NS',

    # Indian Finance
    'HDFCBANK.NS', 'ICICIBANK.NS', 'SBIN.NS', 'AXISBANK.NS', 'KOTAKBANK.NS',
    'INDUSINDBK.NS', 'BAJFINANCE.NS', 'HDFCLIFE.NS', 'SBILIFE.NS', 'ICICIGI.NS',

    # Indian Energy
    'RELIANCE.NS', 'ONGC.NS', 'BPCL.NS', 'IOC.NS', 'GAIL.NS',

    # Indian Consumer & Others
    'HINDUNILVR.NS', 'ITC.NS', 'NESTLEIND.NS', 'BRITANNIA.NS', 'DABUR.NS',
    'TATAMOTORS.NS', 'MARUTI.NS', 'BAJAJ-AUTO.NS', 'HEROMOTOCO.NS', 'EICHERMOT.NS',
]

print(f"Downloading {len(tickers)} stocks...")
data = yf.download(tickers, start='2023-01-01', end='2024-01-01')['Close']

# Drop columns with too many missing values
data.dropna(axis=1, thresh=int(0.9 * len(data)), inplace=True)
data.dropna(inplace=True)

print(f"Downloaded: {data.shape[0]} days x {data.shape[1]} stocks")
print(f"Stocks successfully downloaded: {list(data.columns)}")

data.to_csv('stocks_100.csv')
print("Saved to stocks_100.csv ✅")