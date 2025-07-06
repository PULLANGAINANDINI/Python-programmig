# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3300,
    "MSFT": 350
}

# Dictionary to store user input
portfolio = {}

print("Enter stock names and quantity (type 'done' to finish):")

while True:
    stock = input("Stock Symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in the database.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\n--- Investment Summary ---")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares x ${price} = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Option to save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    file_type = input("Choose file type: 'txt' or 'csv': ").lower()
    filename = f"portfolio.{file_type}"
    with open(filename, 'w') as f:
        if file_type == 'txt':
            for stock, quantity in portfolio.items():
                f.write(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${stock_prices[stock]*quantity}\n")
            f.write(f"\nTotal Investment: ${total_investment}")
        elif file_type == 'csv':
            f.write("Stock,Quantity,Price,Total\n")
            for stock, quantity in portfolio.items():
                f.write(f"{stock},{quantity},{stock_prices[stock]},{stock_prices[stock]*quantity}\n")
            f.write(f",,,{total_investment}")
    print(f"Portfolio saved to {filename}")
AA