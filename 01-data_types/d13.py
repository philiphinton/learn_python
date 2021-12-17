# Dictionary object
shopping_list = {
    'Tomatoes': 6,
    'Bananas': 5,
    'Crackers': 2,
    'Sugar': 1,
    'Icecream': 1,
    'Bread': 3,
    'Chocolate': 2
}
# Just the keys
# print(shopping_list.keys())
# Just the values
# print(shopping_list.values())
# Both keys and values
print(shopping_list.items())
phils_variable = shopping_list.keys()
print(f"Number of items in list: {len(phils_variable)}")
