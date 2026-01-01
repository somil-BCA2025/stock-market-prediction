!pip install yfinance finnhub-python pandas numpy matplotlib scikit-learn tensorflow

import yfinance
import finnhub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf

print("All libraries imported successfully!")

import yfinance as yf

data = yf.download('ORCL', start='2025-01-01', end=today, interval='1h')
print(data.head())

from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')

data = yf.download('AAPL', start='2025-01-01', end=today, interval='1h')

data['Percent Change'] = data['Close'].pct_change() * 100

print(data[['Close', 'Percent Change']].head())
print(data.head())

!pip install finnhub-python

pip install yfinance

import yfinance as yf
print("yfinance imported successfully!")

import yfinance as yf
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')

try:
    data = yf.download('AAPL', start='2025-01-01', end=today, interval='1h')
    print(data.head())
except Exception as e:
    print(f"Error downloading data: {e}")

import finnhub
from datetime import datetime
import time

# Initialize the Finnhub client
finnhub_client = finnhub.Client(api_key='cskudr9r01qhc8s4luk0cskudr9r01qhc8s4lukg')

# List of companies to fetch data for
symbols = ["TSLA", "WMT", "AAPL", "MSFT", "ORCL", "CSCO", "TCS", "GOOG"]

# Today's date
today = datetime.now().strftime('%Y-%m-%d')

# Fetch and print data for each company
for symbol in symbols:
    try:
        # Fetch current share price
        quote = finnhub_client.quote(symbol)
        share_price = quote['c']

        # Fetch company profile
        company_profile = finnhub_client.company_profile2(symbol=symbol)
        market_cap = company_profile['marketCapitalization']

        # Fetch company news
        news = finnhub_client.company_news(symbol, _from="2024-01-01", to=today)

        # Output results
        print(f"\nCompany: {symbol}")
        print(f"The market capitalization of {symbol} is: ${market_cap:,}")
        print(f"The current share price of {symbol} is: ${share_price:.2f}")
        print("Recent News:")
        for article in news[:3]:  # Show only the latest 3 news items
            print(f"- {article['headline']} ({article['datetime']})")

        # Avoid hitting API rate limits
        time.sleep(1)

    except Exception as e:
        # Handle errors gracefully
        print(f"Error fetching data for {symbol}: {e}")

import finnhub
from datetime import datetime

finnhub_client = finnhub.Client(api_key='cskudr9r01qhc8s4luk0cskudr9r01qhc8s4lukg')

today = datetime.now().strftime('%Y-%m-%d')

news = finnhub_client.company_news('ORCL', _from="2025-01-01", to=today)

print(news)

!zip -r /content/project.zip /content/sample_data/
from google.colab import files
files.download("/content/project.zip") 
