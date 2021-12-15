
values = [1, 2, 3, 4, 5]

# You can check the veracity of either one statement or another statement;
# if either check evaluates to True, the whole expression will be True

statement = 1 in values or 6 in values
print(f"{statement}: either 1 or 6 is in 'values'.")

# Note that you can't write "1 or 6 in values"; you have to do 2 whole checks.
