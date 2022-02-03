
# CSVs, a basic guide; see
# https://www.opentechguides.com/how-to/article/python/181/csv-read-write.html

import csv
from pathlib import Path

filepath = Path('./data/VernonAuthority.csv')
print(f"\nWorking with {filepath.absolute()}\n")

with open(filepath, mode='r', newline='') as auth_list:

    dict_reader = csv.DictReader(auth_list)

    dict_reader.fieldnames = [field.strip().lower().replace(' ', '_')
                              for field in dict_reader.fieldnames]
    print(f"Headers: {'; '.join(dict_reader.fieldnames)}\n")

    for row in dict_reader:
        print(row["system_id"] + "|" + row['name'] + "|" + row["long_name"])

# For a more fulsome explanation, see https://thispointer.com/?p=4309
