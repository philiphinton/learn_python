
# This time let's use our shopping list from `d7.py` and define a
# custom function to use with `map()`

shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]
print(shopping_list)


def starts_with_B(item):
    # Return `True` if the first character of the item is "B".
    return item[0] == "B"


mapped = map(starts_with_B, shopping_list)

mapped_to_list = list(mapped)

print(mapped_to_list)

for item in mapped_to_list:
    print(item)

# We end up with a "one-to-one" list of True and False values that is
# "mapped" perfectly onto the original iterable/list.
