
# Use the Path class from pathlib to create OS-agnostic file paths
from pathlib import Path

# Create a Path subclass object that starts in this directory
files_dir = Path('./07-files')

# Append the name of the file we want to work with using slash notation
filepath = files_dir / 'shopping_list.csv'

print(f"\nContents of {filepath.absolute()}:\n")

# Use `readlines()` to iterate over the lines of the file
with open(filepath) as file:
    for line in file.readlines():
        print(line, end='')



# Pathlib can do all sorts of things -- make directories, check if a path is
# a file or a directory, list the contents of directories, and more:
# https://rednafi.github.io/digressions/python/2020/04/13/python-pathlib.html
