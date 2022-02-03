
# We have to specify the whole path (including the directory) because the
# script's Current Working Directory (CWD) is the root of the project.

# We can access the CWD using the `getcwd()` function in the `os` module.
import os

print(os.getcwd())
