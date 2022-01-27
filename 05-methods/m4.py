# Within this folder is a file called calculator.py, which is our calculator
# module from the previous lot of exercises (in the "functions" folder).

import calculator as calc

# Get all properties and methods of the "calc" method using dir()
# See https://www.askpython.com/python/built-in-methods/python-dir-method

props_and_methods = dir(calc)

print("Props and methods for `calc`:\n", props_and_methods)

# You can see there are lots of "dunder" (double underscore) methods and two
# other ones at the end — author (a string), and the `calculate` function

# Let's print the docstring for `calc`
print()
print("Docstring for `calc`:\n", calc.__doc__)
