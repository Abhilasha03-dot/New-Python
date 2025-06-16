# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3400,
    "MSFT": 320
}

# To store user portfolio
portfolio = {}

print("Enter stock details (type 'done' to finish):")

while True:
    stock_name = input("Stock symbol (AAPL, TSLA, etc.): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        portfolio[stock_name] = quantity
    except ValueError:
        print("❌ Invalid quantity. Enter an integer.")

# Calculate total investment
total_investment = 0
summary = []

print("\n🧾 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    summary_line = f"{stock}: {qty} shares x ${price} = ${value}"
    print(summary_line)
    summary.append(summary_line)

print(f"\n💰 Total Investment: ${total_investment}")

# Optionally save to a file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("\n".join(summary))
        file.write(f"\n\nTotal Investment: ${total_investment}")
    print("✅ Portfolio saved to 'portfolio_summary.txt'")
