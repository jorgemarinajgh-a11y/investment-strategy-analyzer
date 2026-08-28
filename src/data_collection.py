import yfinance as yf 

def get_data(ticker_symbol, period="1y"):
    return yf.Ticker(ticker_symbol).history(period=period)