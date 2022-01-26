
"""
The  functions `map`, `filter`, and `reduce` are "paradigms of functional
programming", "a style of programming in which the primary method of
computation is the application of functions to arguments".

All three functions take as their first argument a function object, and as
their second, an iterable object (such as a list). They also all return
function objects. This makes them higher-order functions (in contrast to
first-order functions).

Their purpose is to apply the function to each element in the iterable.

More info:
1. https://ocw.tudelft.nl/courses/introduction-to-functional-programming/
2. https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce
3. https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/
4. https://en.wikipedia.org/wiki/Higher-order_function

"""

# The first, `map()`, performs the function on the iterable and returns a
# "one-to-one" iterable in the form of a map-type object.

pencil_case_contents = ['pencil', 'pen', 'fountain pen', 'felt pen',
                        'ruler', 'eraser', 'highlighter', 'scissors']

# Let's use the built-in string function to capitalise each element in the list
mapped = map(str.capitalize, pencil_case_contents)

# Note the lack of parentheses after "str.capitalize"; we're not running
# that function, just passing its name to `map` so it can run it for us.

# Because `map()` returns a generator object, we cast it to a list for printing
list_from_mapped = list(mapped)

print(list_from_mapped)

# Had we not cast it to a list and instead simply printed `mapped`, we'd
# get the address in memory of the generator object itself, as you can see
# by uncommenting the next line.

# print(mapped)
