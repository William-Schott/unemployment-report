import os

from dotenv import load_dotenv

from app import APP_ENV
from app.stocks import fetch_stocks_data, format_usd
from app.email_service import send_email

load_dotenv()

DEFAULT_SYMBOL = os.getenv("DEFAULT_SYMBOL", default="NFLX")


if __name__ == "__main__":

    print("STOCKS EMAIL...")

    # if we are running this app locally, ask the user for a symbol
    # otherwise if running on the server, use the default symbol
    # ... to enable automation
    if APP_ENV=="development":
        symbol = input("Please input a stock symbol (e.g. 'NFLX'): ")
    else:
        symbol = DEFAULT_SYMBOL

    df = fetch_stocks_data(symbol)
    latest = df.iloc[0]

    # keeping the email content simple for example purposes, but
    # ... for an example of attaching the data as a CSV file
    # ... and attaching the chart as an image file
    # ... see: https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/codebase-cleanup/starter/app/unemployment_email.py#L56-L132
    # ... (you might need to create a more complex email sending function)

    html_content = f"""
        <h1>Stocks Report Email</h1>
        <p>Selected symbol: '{symbol}' </p>
        <p>Latest price: {format_usd(latest['adjusted_close'])} </p>
        <p>As of: {latest['timestamp']} </p>
    """

    send_email(subject="[Daily Briefing] Stocks Report", html=html_content)