
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
    Product("Bananas", "no brand", .67, "kg", "12", True),
    Product("Crackers", "Griffin's", 2.35, "box", "02", True),
    Product("White sugar", "Chelsea", 5.5, "1.5kg", "S", True),
    Product("Vanilla icecream", "Tip Top", 6.5, "2L", "10", True),
    Product("Toast bread", "Vogel's", 3.89, "loaf", "02", False),
    Product("Chocolate", "Whittaker's", 5.49, "block", "R", True)
]
