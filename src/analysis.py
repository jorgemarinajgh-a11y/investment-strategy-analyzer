def calculate_return(data):
    initial_price = data["Close"].iloc[0]
    final_price = data["Close"].iloc[-1]
    return_pct = ((final_price - initial_price) / initial_price) * 100
    return return_pct

def compare_returns(annual_returns):
    return sorted(annual_returns.items(), key=lambda item: item[1], reverse=True)