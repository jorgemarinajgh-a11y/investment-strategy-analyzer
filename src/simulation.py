from analysis import calculate_return

def simulator(money, data):
    gain = calculate_return(data) * money / 100
    return gain + money, gain 

def simulate_all(stocks, money, data):
    results = {}
    for stock in stocks:
        res, gain = simulator(money, data[stock])
        results[stock] = (res, gain)
    return results