
# Itemised, alphabetical list of unique items — just one bunch of bananas!

shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]

shopping_list.sort()

# Start with an empty list that we'll use to hold just unique items
unique_shopping_list = []

for item in shopping_list:
    if item not in unique_shopping_list:
        unique_shopping_list.append(item)

# So, for each item in the list, add it to the "unique" list if it's not
# already there. We don't need an "else" because no more work is needed.

print("Itemised, alphabetical shopping list of unique items:")

for position, item in enumerate(unique_shopping_list, start=1):
    print(f"{position}. {item}")
