# You can also use the `readlines()` method to iterate over the lines of a file

filepath = r'07-files/shopping_list.csv'

print(f"\nContents of {filepath}:\n")

with open(filepath) as file:
    for line in file.readlines():
        print(line, end='')
