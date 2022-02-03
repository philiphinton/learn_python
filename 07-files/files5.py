
# This time let's open a file for appending.

# Define file path with an "r"-string
filepath = r'07-files/soliloquy.txt'

new_lines = ["To sleep, perchance to Dream; aye, there's the rub,",
             "For in that sleep of death, what dreams may come,",
             "When we have shuffled off this mortal coil,",
             "Must give us pause."]

# Open for reading
with open(filepath, mode='r') as reader:

    # Enumerate over the file, but do nothing ("pass") with its contents
    for position, line in enumerate(reader):
        pass

# The line count will be the position given by `enumerate()`, plus 1
num_lines = position + 1
print(f"File is {num_lines} lines long.")

# Open in append mode ('a')
with open(filepath, mode='a') as writer:

    # Write each line in the list to the file, and add a newline character;
    # without it, all the new lines would have been concatenated.
    for line in new_lines:
        writer.write(line + '\n')

# Print the newly added-to file, with line numbers.
with open(filepath, mode='r') as reader:
    for line_num, line in enumerate(reader, start=1):
        print(line_num, line)

print(f"Wrote {len(new_lines)} extra lines.")
