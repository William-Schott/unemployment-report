print("Stocks Report...")

import os
from dotenv import load_dotenv
from pandas import read_csv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
print("SYMBOL:", symbol)

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv"

df = read_csv(request_url)
print(df.columns)
print(df.head())

#Chalange A
# print latest closing price
print("LATEST:", '${:,.2f}'.format(latest["adjusted_close"]), "as of", latest["timestamp"])


#chalenge B
# What is the highest high price (formated USD)
# What is the lowest low price

print("HIGH:", '${:,.2f}'.format(df["high"].max()))
print("LOW:", '${:,.2f}'.format(df["low"].min()))
