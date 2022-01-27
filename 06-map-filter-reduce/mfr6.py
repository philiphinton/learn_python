
# Let's use the 'collections' module to make a Class called "Product"
# to contain our shopping-list items and some metadata about each of them.

import collections

Product = collections.namedtuple(
    'Product',
    [
        'name',
        'brand',
        'price',
        'price_measure',
        'aisle',
        'on_special'
    ]
)

shopping_list = [
    Product("Tomatoes", None, .38, "kg", "01", False),
    Product("Bananas", None, .67, "kg", "12", False),
    Product("Crackers", "Griffin's", 2.35, "box", "02", True),
    Product("White sugar", "Chelsea", 5.5, "1.5kg", "D", True),
    Product("Vanilla icecream", "Tip Top", 6.5, "2L", "10", True),
    Product("Toast bread", "Vogel's", 3.89, "loaf", "02", False),
    Product("Chocolate", "Whittaker's", 5.49, "block", "R", True)
]

# You can index into lists and print an element by calling it by name
first_item_name = shopping_list[0].name
print(f"The first item in the list is {first_item_name.upper()}")

last_item_brand = shopping_list[-1].brand
print(f"The brand name of the last item in the list is \"{last_item_brand}\".")

print(f"The first item in the list is {first_item_name}")
