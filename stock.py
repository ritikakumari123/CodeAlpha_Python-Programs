# Stock Portfolio Tracker

# Stock price dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 300
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock_name = input("\nEnter stock name (or type 'done'): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Added", stock_name, "->", investment)

    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total_investment)

# Optional: save to file
file = open("portfolio.txt", "w")
file.write("Total Investment Value: " + str(total_investment))
file.close()

print("Saved in portfolio.txt")
