
# Split concatenated CallNumbers on "|" delimiter
# https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html

import pandas as pd
from pathlib import Path

infile = Path('./data/publications.csv')

pubs = pd.read_csv(infile)

pubs["CatCallNumber"] = pubs["CatCallNumber"].str.strip()

delim = "|"
headers = "CatCallNumber"
new_df = pubs["CatCallNumber"].str.split(
    pat=delim, regex=False, expand=True)

print(pubs)
