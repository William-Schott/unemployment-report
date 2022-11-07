


#this is the global scope which removes user input so when the test runs the whole code is not executed

from pandas import read_csv

from App.alpha import API_KEY

def format_usd(my_price):  
    return f"${my_price:,.2f}"

## need to pass in symobol parameter!!! in the () in the def
def fetch_stocks_data(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv"

    df = read_csv(request_url)
    return df


if __name__ == "__main__":

    print("Stocks Report...")

    symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
    print("SYMBOL:", symbol)

    df = fetch_stocks_data(symbol)
    
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
