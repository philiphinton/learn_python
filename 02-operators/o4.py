
values = [1, 2, 3, 4, 5]
valuesearch = [1,3]

# You can check the veracity of either one statement or another statement;
# if either check evaluates to True, the whole expression will be True

# statement = 1 in values or 6 in values
# statement = [1,3] in values or 6 in values
statement = valuesearch in values or 5 in values

# statement = [1,3,6] in values # False
print(statement)
# statement = 1 in values or 500 > 50

# print(f"{statement}: either 1 or 6 is in 'values'.")

# Note that you can't write something like:
#     statement = 1 or 6 in values
# You have to do 2 whole checks
