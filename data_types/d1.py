# Strings and string concatenation

# Strings can be wrapped in single or double quotes.
string_variable = "Hello"
second_string_variable = 'world'

# the old (Python 2) way
print(string_variable + " " + second_string_variable + "!")

# You can print a string multiple times by… multiplying it!
print("-" * 10)

# The new way; a format string
print(f"{string_variable} {second_string_variable}!")

# If you want to include apostrophes in your string, it's easiest to wrap it
# in double quotes.
niceday = "It's a nice day!"
print(niceday)
