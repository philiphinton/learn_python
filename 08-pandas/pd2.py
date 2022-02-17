
# Remove leading/trailing and double spaces from CatCallNumber
# https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html

import pandas as pd
from pathlib import Path

infile = Path('./data/publications.csv')
pubs = pd.read_csv(infile)

pubs["CatCallNumber"] = pubs["CatCallNumber"].str.strip()

print(pubs["CatCallNumber"])
