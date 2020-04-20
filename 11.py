import pandas as pd

df = pd.read_table('data/popular-names.txt', header=None)

df.to_csv('data/ans11.txt', sep=" ", header=None, index=False)