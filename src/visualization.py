import matplotlib.pyplot as plt

def plot_stock_history(stock, data):
    plt.plot(data["Close"], label=f"{stock} Close Price")
    plt.title(f"{stock} Stock History")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.close()

def plot_multiple(stocks, data):
    for stock, stock_data in data.items():
        plt.plot(stock_data["Close"], label=f"{stock} Close Price")
    plt.title("Multiple Stock History")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.close()