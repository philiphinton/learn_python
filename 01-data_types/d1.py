# Strings and string concatenation

# Strings can be wrapped in single or double quotes.
string_variable = "Hello"
second_string_variable = 'world'

# Concatenation, the old (Python 2.x) way
print(string_variable + " " + second_string_variable + "!")

# Concatenation, the new way — in a "format string", which starts with an 'f'
print(f"{string_variable} {second_string_variable}!")
