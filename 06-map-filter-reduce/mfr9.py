"""
So, `map()` returns a one-to-one generator object, and `filter()` returns
a generator object containing only those elements in the iterable that met
a condition.

The final tool in the trio, `reduce()`, cumulatively performs a function on
each element in an iterable such that only one value is returned.
"""

# `reduce()` used to be built-in but now has to be imported
from functools import reduce

num_list = [1, 3.14159, 6, 93, 102]
total = reduce(lambda x, y: x + y, num_list)

print(total)

# Ultimately adding numbers together like this is not a great use of `reduce()`
# because built-ins like "sum" and the "add" module in "operator" exist, but it
# gives you some idea of how cumulative functions work.
# See https://stackoverflow.com/a/33772246/10267529 and
# https://realpython.com/python-reduce-function/ for more.
