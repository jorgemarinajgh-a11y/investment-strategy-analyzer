import pandas as pd

def calculate_return(data):
    initial_price = data["Close"].iloc[0]
    final_price = data["Close"].iloc[-1]
    return_pct = ((final_price - initial_price) / initial_price) * 100
    return return_pct

def compare_returns(annual_returns):
    return sorted(annual_returns.items(), key=lambda item: item[1], reverse=True)

def normalize_data(data):
    res = {}
    for column in data.columns:
        res[column] = data[column] / data[column].iloc[0] * 100
    return pd.DataFrame(res)


def normalize_all(data):
    res = {}
    for stock, stock_data in data.items():
        res[stock] = normalize_data(stock_data)
    return res