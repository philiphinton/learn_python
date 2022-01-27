
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
list_of_mapped = list(map(str.capitalize, pencil_case_contents))

print(list_of_mapped)
