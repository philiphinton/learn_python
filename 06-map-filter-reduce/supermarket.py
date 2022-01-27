
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
    Product("Tomatoes", None, .38, "kg", "A", False),
    Product("Bananas", None, .67, "kg", "C", False),
    Product("Crackers", "Griffin's", 2.35, "box", "F", True),
    Product("White sugar", "Chelsea", 5.5, "1.5kg", "D", True),
    Product("Vanilla icecream", "Tip Top", 6.5, "2L", "X", True),
    Product("Toast bread", "Vogel's", 3.89, "loaf", "A", False),
    Product("Chocolate", "Whittaker's", 5.49, "block", "R", True)
]
