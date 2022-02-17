
# Create a Pandas DataFrame from CSV data
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html

import pandas as pd
from pathlib import Path

infile = Path('./data/publications.csv')
pubs = pd.read_csv(infile)

print(pubs.info())
# print(pubs)
# print(pubs.dtypes)
