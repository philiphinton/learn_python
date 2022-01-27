
# Use the `sorted()` method to sort a list (here, alphabetically) and store
# the results in a new variable. The original list variable is untouched.

shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]


print("Printout of shopping_list:")
for item in shopping_list:
    print(item)


# Sort the list using `sorted()` and store the results in a new variable
sorted_shopping_list = sorted(shopping_list)

print()
print("Printout of sorted_shopping_list:")
for item in sorted_shopping_list:
    print(item)
