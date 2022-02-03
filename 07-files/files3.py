
# It's best to use context handlers (the `with` keyword) to open and
# automatically close files; previously we had try/with instead.
# See https://www.educative.io/edpresso/the-with-statement-in-python

filepath = r'07-files/shopping_list.csv'

print(f"\nContents of {filepath}:\n")

# Use the `read()` method to get the contents of the file for printing
with open(filepath) as file:
    print(file.read())

# We no longer need `file.close()`; the context handler does that for us.
