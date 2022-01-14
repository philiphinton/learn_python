# Within this folder is a file called calculator.py, which is our calculator
# module from the previous lot of exercises (in the "functions" folder).

# Let's import it:
import calculator as calc

# Get all properties and methods of the "calc" method using dir()
# See https://www.askpython.com/python/built-in-methods/python-dir-method
props_and_methods = dir(calc)

print(props_and_methods)

# You can see there are lots of "dunder" (double underscore) methods and two
# other ones at the end — author (a string), and the `calculate` function
