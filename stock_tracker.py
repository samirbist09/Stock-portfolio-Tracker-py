# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "SYPANEL": 1500,
    "TSLA": 2050,
    "SAGAR": 1140,
    "SOLU": 1320
}

total_investment = 0
portfolio = []

print(" Welcome to Stock Portfolio Tracker")

num_stocks = int(input("How many different stocks do you want to add? "))

for i in range(num_stocks):
    stock_name = input("\nEnter stock symbol (SYPANEL, TSLA, SAGAR, SOLU): ").upper()

    if stock_name not in stock_prices:
        print(" Stock not found! Skipping...")
        continue

    quantity = int(input(f"Enter quantity for {stock_name}: "))

    price = stock_prices[stock_name]
    value = price * quantity

    portfolio.append((stock_name, quantity, value))
    total_investment += value

print("\n Portfolio Summary")
for stock in portfolio:
    print(f"Stock: {stock[0]}, Quantity: {stock[1]}, Value: {stock[2]}")

print(f"\n Total Investment Value: {total_investment}")

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")
    for stock in portfolio:
        file.write(f"{stock[0]} - Quantity: {stock[1]}, Value: {stock[2]}\n")
    file.write(f"\nTotal Investment: {total_investment}")

print("\n Portfolio saved to portfolio.txt")
