# Strings and string concatenation

# Strings can be wrapped in single or double quotes.
first_word = "Hello"
second_word = 'world'

# Concatenation, the old (Python 2.x) way
print(first_word + " " + second_word + "!")

# Concatenation, the new way — in a "format string", which starts with an 'f'
print(f"{first_word} {second_word}!")

# You could also concatenate variables in a new variable
full_sentence = first_word + " " + second_word + "!"
print(full_sentence)
