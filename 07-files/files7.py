
# Compare CSVs: https://stackoverflow.com/a/49444878/10267529

import csv
from pathlib import Path

before_file = Path('./data/ALA_before.csv')
after_file = Path('./data/ALA_after.csv')
outfile = Path('./data/ALA_diff.csv')

# Create a set object by mapping the "before" file onto a tuple object
# (an immutable list), passing teh result of `open()` to `csv.reader()`
before = set(
    map(
        tuple,
        csv.reader(open(before_file))
    )
)

# Repeat for the second ("after") file
after = set(map(tuple, csv.reader(open(after_file))))

# Use the caret (^) operator to get the symmetric difference between the sets
# https://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch16s03.html

differences = before ^ after

output = csv.writer(open(outfile, mode='w'))

compared = sorted(differences, key=lambda x: x[0], reverse=True)

for count, row in enumerate(compared):
    output.writerow(row)

print(f"Wrote {count} rows to output file.")
