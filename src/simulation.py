from analysis import calculate_return, beat_spy

def simulator(money, data):
    gain = calculate_return(data) * money / 100
    return gain + money, gain 

def simulate_all(stocks, money, data, spy_return):
    results = {}
    for stock in stocks:
        res, gain = simulator(money, data[stock])
        better_than_spy = beat_spy(gain, spy_return)
            
        results[stock] = (res, gain, better_than_spy)
    return results
