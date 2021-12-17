
# List variables are iterable and hold elements in series

shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]
print(f"Here's the shopping list:\n{shopping_list}.\n")

# You can count the number of items in a list
num_items = len(shopping_list)
print(f"There are {num_items} things on it.")

# You can also count the number of times a given string appears
# This is case-sensitive, so "bananas" with a lowercase "b" won't work
bananas_count = shopping_list.count('Bananas')
print(f"\"Bananas\" is there {bananas_count} times, for some reason.\n")

# Use sort() to re-order the list. Note that you don't need a new variable
# to store the result in; the sort() method modifies the existing variable.
# Good explanation here: http://opensask.ca/Python/Lists/ListMethods.html#id1
shopping_list.sort()
print("Now the list is in alphabetical order:")
print(shopping_list)

# There's also an append() method:
shopping_list.append("Milk")
print("\nAfter adding milk, the list looks like this:")
print(shopping_list)
print(f"Here's the shopping list:\n{shopping_list}.\n")