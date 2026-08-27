import yfinance as yf 

stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META"]

def out_info(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period="1y")
    print(f"\n{ticker_symbol}:")
    print("First price:")
    print(data["Close"].iloc[0])
    print("Most recent price:")
    print(data["Close"].iloc[-1])
    print("\nMaximum in last year:")
    print(data["High"].max())
    print("\nMinimum in last year:")
    print(data["Low"].min())

def calculate_annual_return(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period="1y")
    initial_price = data["Close"].iloc[0]
    final_price = data["Close"].iloc[-1]
    return_pct = ((final_price - initial_price) / initial_price) * 100
    return return_pct

def compare_returns(annual_returns):
    ordered = sorted(annual_returns.items(), key=lambda item: item[1], reverse=True)
    
    return ordered

returns = {}

for stock in stocks:
    out_info(stock)
    return_pct = calculate_annual_return(stock)
    returns[stock] = return_pct
    print(f"{stock}: Annual Return: {return_pct:.2f}%")

annual_returns = compare_returns(returns)
print("\nAnnual Returns (Ordered):")
for stock, return_pct in annual_returns:
    print(f"{stock}: {return_pct:.2f}%")
