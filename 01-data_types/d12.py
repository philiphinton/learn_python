
shopping_list = {
    'Tomatoes': 6,
    'Bananas': 5,
    'Crackers': 2,
    'Sugar': 1,
    'Icecream': 1,
    'Bread': 3,
    'Chocolate': 2
}

# Let's say we want three blocks of chocolate, and a bottle of milk...
# Pass a dictionary to the update() method on the shopping_list object
shopping_list.update({
    'Milk': 1,
    'Chocolate': 3
})

print(f"Here's the shopping list:\n{shopping_list}.\n")
# Notice that "Milk" appears last
