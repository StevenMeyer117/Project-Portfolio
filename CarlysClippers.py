# You are the Data Analyst at Carly's Clippers. Your job is to go through the lists of data that have been collected in
# the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation
# of the business for the rest of the month

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Find the average price of a haircut
total_price = 0
# Loop function to find and print average price of haircuts
for price in prices:
  total_price += price
average_price = total_price / len(prices)
print("Average Haircuts Price: $" + str(average_price))

# Carly expected the average price to be cheaper. Reduce all prices by $5
# List comprehension to reduce haircuts by $5.00
new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0

# Find last week's revenue to ensure business is remaining profitable
# Loop to find total revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: $" + str(total_revenue))

# Find average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# List comprehension to make i go from 0 to last index of new_prices
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)