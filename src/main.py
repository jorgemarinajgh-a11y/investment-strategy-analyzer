import yfinance as yf 

stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META"]

def out_info(ticker_symbol, period="1y"):
    data = get_data(ticker_symbol, period=period)
    print(f"\n{ticker_symbol}:")
    print("First price:")
    print(data["Close"].iloc[0])
    print("Most recent price:")
    print(data["Close"].iloc[-1])
    print("\nMaximum in last year:")
    print(data["High"].max())
    print("\nMinimum in last year:")
    print(data["Low"].min())
    return data

def get_data(ticker_symbol, period="1y"):
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period=period)
    return data

def calculate_return(ticker_symbol, period, data):
    if data is None:
        ticker = yf.Ticker(ticker_symbol)
        data = yf.Ticker(ticker_symbol).history(period = period)
    initial_price = data["Close"].iloc[0]
    final_price = data["Close"].iloc[-1]
    return_pct = ((final_price - initial_price) / initial_price) * 100
    return return_pct

def compare_returns(annual_returns):
    ordered = sorted(annual_returns.items(), key=lambda item: item[1], reverse=True)
    
    return ordered

def simulator(money, time, stock, data):
    gain = calculate_return(stock, time, data) * money / 100
    res = gain + money
    return res, gain

def simulate_all(stocks, money, time, data):
    results = {}
    for stock in stocks:
        res, gain = simulator(money, time, stock, data[stock])
        results[stock] = (res, gain)
    return results

returns = {}
data = {}
for stock in stocks:
    data[stock] = out_info(stock, period="1y")
    return_pct = calculate_return(stock, "1y", data[stock])
    returns[stock] = return_pct
    print(f"{stock}: Annual Return: {return_pct:.2f}%")
    

annual_returns = compare_returns(returns)
print("\nAnnual Returns (Ordered):")
for stock, return_pct in annual_returns:
    print(f"{stock}: {return_pct:.2f}%")


results = simulate_all(stocks, 1000, "1y", data)

print("\n$1000 Investment Simulation")

for stock, (value, gain) in results.items():
    print(f"{stock}:")
    print(f"Current Value: ${value:.2f}")
    print(f"Profit: ${gain:.2f}")