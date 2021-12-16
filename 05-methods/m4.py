
# Okay, let's import our calculator

import calculator as calc

# Get all properties and methods of the "calc" method using dir()
# See https://www.askpython.com/python/built-in-methods/python-dir-method
props_and_methods = dir(calc)

print(props_and_methods)

# You can see there are lots of "dunder" (double underscore) methods and two
# other ones at the end — author, a string variable as it turns out, and
# our actual calculate function
