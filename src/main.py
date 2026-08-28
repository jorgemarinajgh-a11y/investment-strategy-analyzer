from data_collection import get_data
from stock_info import display_stock_info
from analysis import calculate_return, compare_returns
from simulation import simulate_all
from visualization import plot_stock_history

#stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META"]
stocks = ["AAPL"]
returns = {}
data = {}
for stock in stocks:
    data[stock] = get_data(stock, period="1y")
    display_stock_info(stock,data[stock])
    return_pct = calculate_return(data[stock])
    returns[stock] = return_pct
    print(f"{stock}: Annual Return: {return_pct:.2f}%")
    plot_stock_history(stock, data[stock])
    

annual_returns = compare_returns(returns)
print("\nAnnual Returns (Ordered):")
for stock, return_pct in annual_returns:
    print(f"{stock}: {return_pct:.2f}%")


results = simulate_all(stocks, 1000, data)

print("\n$1000 Investment Simulation")

for stock, (value, gain) in results.items():
    print(f"{stock}:")
    print(f"Current Value: ${value:.2f}")
    print(f"Profit: ${gain:.2f}")