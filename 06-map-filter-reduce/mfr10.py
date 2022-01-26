
from functools import reduce
from supermarket import shopping_list

# Create a list of prices and use `reduce()` to add them up
prices = list(item.price for item in shopping_list)
total = reduce(lambda x, y: x + y, prices)

print(f"The bill for this supermarket trip is ${total:.2f}", end="")

# Filter the shopping list to just those items on special
items_on_special = filter(lambda item: item.on_special, shopping_list)

# Create a list of prices and use `reduce()` to add them up
prices_of_items_on_special = list(item.price for item in items_on_special)
specials_only_total = reduce(lambda x, y: x + y, prices_of_items_on_special)

savings = total - specials_only_total

print(" -- but if you just bought things that were on special, it'd be ", end="")
print(f"${specials_only_total:.2f} (saving you ${savings:.2f}).")
