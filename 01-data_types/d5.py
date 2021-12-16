
# Using len() to count the number of characters in a string

name = "Phil Hinton"
num_characters_in_name = len(name)

# If you want to include quote marks in a string, escape them with a backslash
print(f"There are {num_characters_in_name} characters in the name \"{name}\".")

# Just be careful not to go out of bounds; uncomment this to see why!
# print(name[11])
