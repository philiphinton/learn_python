
# Compare CSVs: https://stackoverflow.com/a/49444878/10267529

import csv
from pathlib import Path

before_file = Path('./data/ALA_before.csv')
after_file = Path('./data/ALA_after.csv')
outfile = Path('./data/ALA_diff.csv')

before = set(
    map(
        tuple,
        csv.reader(open(before_file))
    )
)

after = set(map(tuple, csv.reader(open(after_file))))

differences = before ^ after

output = csv.writer(open(outfile, mode='w'))

compared = sorted(differences, key=lambda x: x[0], reverse=True)

for iter, row in enumerate():
    output.writerow(row)

print(f"Wrote {iter} rows to output file.")
