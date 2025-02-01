# Sal's Shipping project gives you the chance to build a program that gives three shipping options to a customer. Build
# a program that will take the weight of a package and determine the cheapest way to ship that package using Sal's
# Shippers. The three shipping methods should be ground, ground premium and drone shipping.

weight = 4.8

# Ground shipping
if weight <= 2:
  cost = (weight * 1.50) + 20.00
elif weight <= 6:
  cost = (weight * 3.00) + 20.00
elif weight <= 10:
  cost = (weight * 4.00) + 20.00
else:
  cost = (weight * 4.75) + 20.00
print("Ground Shipping cost:", cost)

# Premium ground shipping
premium_ground_shipping = 125.00
print("Premium Ground Shipping cost:", premium_ground_shipping)

# Drone shipping
if weight <= 2:
  cost = (weight * 4.50)
elif weight <= 6:
  cost = (weight * 9.00)
elif weight <= 10:
  cost = (weight * 12.00)
else:
  cost = (weight * 14.25)
print("Drone Shipping cost:", cost)