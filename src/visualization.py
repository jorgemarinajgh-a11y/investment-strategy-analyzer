import matplotlib.pyplot as plt

def plot_stock_history(stock, data):
    plt.plot(data["Close"], label=f"{stock} Close Price")
    plt.title(f"{stock} Stock History")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)
    plt.show()s