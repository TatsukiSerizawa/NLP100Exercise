import pandas as pd

df = pd.read_table('data/popular-names.txt', header=None)

df[0].to_csv('data/col1.txt', header=None, index=False)
df[1].to_csv('data/col2.txt', header=None, index=False)