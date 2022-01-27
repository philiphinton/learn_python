
"""
While `map()` creates a one-to-one generator object, `filter()` requires
that each element in the iterable meet a condition before it is added
to the generator object to be returned.

In lambda expressions, there's an implied "return" keyword after the colon,
and, with the lambda in `filter()`, there is an implied conditional statement.
"""

shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]
print(shopping_list)

filtered = filter(lambda item: item[0] == "B", shopping_list)


def starts_with_B(item):
    # Lambda written out in full:
    if item[0] == "B":
        return item
    else:
        return None


print(list(filtered))
