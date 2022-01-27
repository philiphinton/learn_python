
# Long strings and built-in methods
# (See https://www.codecademy.com/resources/docs/python/strings for more)

# To create long strings that span several lines, wrap them in """ or '''
speech = """To be, or not to be, that is the question,
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;"""

# Multi-line strings maintain their linebreaks when printed
print(speech)

# There are lots of built-in methods you can use to operate on strings;
# one of them, count(), counts the number of occurrences of a substring.
count_of_to = speech.count('to')
print(f"\nThe word 'to' appears {count_of_to} times in that speech.")

# The "\n" at the start of that print call creates a new line
