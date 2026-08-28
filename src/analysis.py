import pandas as pd

def calculate_return(data):
    initial_price = data["Close"].iloc[0]
    final_price = data["Close"].iloc[-1]
    return_pct = ((final_price - initial_price) / initial_price) * 100
    return return_pct

def compare_returns(annual_returns):
    return sorted(annual_returns.items(), key=lambda item: item[1], reverse=True)

def calculate(num, denom):
    if denom == 0:
        return 0
    return (num / denom) * 100

def normalize_data(data):
    res = {}
    for column in data.columns:
        res[column] = calculate(data[column].values, data["Close"].iloc[0])
    return pd.DataFrame(res)

def normalize_all(data):
    res = {}
    for stock, stock_data in data.items():
        res[stock] = normalize_data(stock_data)
    return res

def dependent_normalize(data, spy_data):
    const = spy_data["Close"].iloc[0] / data["Close"].iloc[0] * 100
    res = data["Close"] / spy_data["Close"] * const
    res.name = "Close"
    
    return pd.DataFrame(res)

def dependent_normalize_all(data, spy_data):
    res = {}
    for stock, stock_data in data.items():
        res[stock] = dependent_normalize(stock_data, spy_data)
    return res

def beat_spy(stock_return, spy_return):
    return stock_return > spy_return

def calculate_volatility(data):
    returns = data["Close"].pct_change()
    return returns.std()