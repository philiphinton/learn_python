

# This time let's append to a file. By default files are opened for reading,
# in "text" mode. More: https://riptutorial.com/python/example/978/file-modes

from pathlib import Path
files_dir = Path('./07-files')
filepath = files_dir / 'soliloquy.txt'

new_lines = ["To sleep, perchance to dream; ay, there's the rub;",
             "For in that sleep of death what dreams may come",
             "When we have shuffled off this mortal coil,",
             "Must give us pause."]

# Open for reading; note the variable name given to the file object
with open(filepath, mode='r') as reader:

    # Enumerate over the file, but do nothing ("pass") with its contents
    for position, line in enumerate(reader):
        pass

# The line count will be the position given by `enumerate()`, plus 1
num_lines = position + 1
print(f"\nFile is {num_lines} lines long.\n")

print("-" * 26)
print(" Hamlet, Act III, scene I")
print("-" * 26 + '\n')

# Open in append mode ('a')
with open(filepath, mode='a') as writer:

    # Append each line in the list to the file, and add a newline character;
    # without it, all the new lines would have been concatenated.
    for line in new_lines:
        writer.write(line + '\n')

# Print the newly added-to file, with line numbers.
with open(filepath, mode='r') as reader:
    for line_num, line in enumerate(reader, start=1):
        print(line_num, line, end='')

print(f"\nWrote {len(new_lines)} extra lines.\n")
