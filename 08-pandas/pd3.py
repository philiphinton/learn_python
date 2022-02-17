
# Count concatenated CallNumbers. (Find and Rplace, or COUNTIF)
# https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html

import pandas as pd
from pathlib import Path

infile = Path('./data/publications.csv')
pubs = pd.read_csv(infile)

pubs["CatCallNumber"] = pubs["CatCallNumber"].str.strip()

search_char = "|"
count_concat = pubs["CatCallNumber"].str.contains(search_char, regex=False)

print(
    f"The character '{search_char}' appears in {count_concat.sum()} rows in the CatCallNumber column.")
