#######################################################
# JANREI
# Computer Science 30
# sept. 10, 2024
#
# Project Overview:
# Develop a Python-based cryptocurrency tracker application that allows users to monitor prices and performance of various cryptocurrencies in real-time by interfacing with cryptocurrency APIs.
#
# Key Learning Outcomes:
# API Integration: Learn to fetch real-time cryptocurrency data from APIs.
# Python Programming: Strengthen Python skills, focusing on data handling and OOP.
# Data Storage and Management: Understand how to manage cryptocurrency data.
# Data Visualization: Create visual representations of cryptocurrency trends.
# Blockchain Understanding: Gain insights into blockchain technology.
# Project Requirements:
# Real-Time Cryptocurrency Tracking:
# 
# Integrate with a cryptocurrency API (e.g., CoinGecko, CoinMarketCap).
# Allow users to input cryptocurrencies to track.
# Historical Data and Trends:
# 
# Fetch and display historical price data.
# Visualize data using libraries like Matplotlib or Plotly.
# User Interface:
#
# Create a CLI for user interaction.
# Optionally develop a GUI using Tkinter or PyQt.
# Portfolio Tracking:
# 
# Enable users to create a virtual portfolio to track cryptocurrency holdings.
# Notifications and Alerts:
#
# Implement price alerts for specific cryptocurrencies.
# Educational Component:
#
# Include explanations of blockchain technology and cryptocurrency security.
# Suggested Tools and Libraries:
# Python Libraries:
# Requests, Matplotlib/Plotly, Pandas, Tkinter/PyQt, SQLite/JSON.
# Cryptocurrency APIs:
# CoinGecko API, CoinMarketCap API.
#######################################################
import requests
import pandas as pd
import sqlite3
from datetime import datetime
from matplotlib import pyplot as plt

# Connect to the database
def create_database():
    connect = sqlite3.connect('crypto_tracker.db')
    cursor = connect.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cryptocurrencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            symbol TEXT NOT NULL,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    connect.commit()
    connect.close()
    print('Database created.')

# Fetch cryptocurrency data from CoinGecko API
def fetch_crypto_data(symbol):
    response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd')
    return response.json()

# Insert cryptocurrency data into the database
def insert_crypto_data(symbol, data):
    connect = sqlite3.connect('crypto_tracker.db')
    cursor = connect.cursor()

    cursor.execute('''
        INSERT INTO cryptocurrencies (name, symbol)
        VALUES (?, ?)
    ''', (data['name'], symbol))
    connect.commit()
    connect.close()
    print(f'Data for {symbol} inserted.')

# Fetch historical price data from CoinGecko API
def fetch_historical_price_data(symbol):
    response = requests.get(f'https://api.coingecko.com/api/v3/coins/{symbol}/market_chart?vs_currency=usd&days=365')
    return response.json()

# Insert historical price data into the database
def insert_historical_price_data(symbol, data):
    connect = sqlite3.connect('crypto_tracker.db')
    cursor = connect.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historical_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin_id INTEGER,
            price REAL,
            timestamp DATETIME,
            FOREIGN KEY (coin_id) REFERENCES cryptocurrencies(id)
        )
    ''')
    connect.commit()
    connect.close()
    print(f'Historical price data for {symbol} inserted.')
    
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.to_sql('historical_prices', con=sqlite3.connect('crypto_tracker.db'), if_exists='append', index=False)
    print(f'Historical price data for {symbol} saved to database.')
    return df

# Fetch cryptocurrency data
def fetch_crypto_data_all():
    response = requests.get('https://api.coingecko.com/api/v3/coins/list')
    return response.json()['coins']

# Create the database
create_database()

# Fetch cryptocurrency data
crypto_data_all = fetch_crypto_data_all()

# Insert cryptocurrency data into the database
for coin in crypto_data_all:
    insert_crypto_data(coin['symbol'], coin)
    fetch_historical_price_data(coin['symbol'])
    insert_historical_price_data(coin['symbol'], fetch_historical_price_data(coin['symbol']))
    print(f'Data for {coin["symbol"]} fetched and saved.')
    print('----------------------------------------')

# Fetch cryptocurrency data from the database
def fetch_crypto_data_from_db(symbol):
    connect = sqlite3.connect('crypto_tracker.db')
    cursor = connect.cursor()

    cursor.execute('SELECT * FROM cryptocurrencies WHERE symbol = ?', (symbol,))
    data = cursor.fetchone()
    connect.close()
    return data

# Fetch historical price data from the database
def fetch_historical_price_data_from_db(symbol):
    connect = sqlite3.connect('crypto_tracker.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM historical_prices WHERE coin_id = (SELECT id FROM cryptocurrencies WHERE symbol = ?)', (symbol,))
    data = cursor.fetchall()
    connect.close()
    return data

# Fetch and display historical price data

symbol = 'bitcoin'
data = fetch_crypto_data_from_db(symbol)
historical_prices = fetch_historical_price_data_from_db(symbol)

df = pd.DataFrame(historical_prices, columns=['timestamp', 'price'])