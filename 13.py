import pandas as pd

col1 = pd.read_csv('data/col1.txt', header=None)
col2 = pd.read_csv('data/col2.txt', header=None)

df = pd.concat([col1, col2], axis=1)

df.to_csv('data/ans13.txt', sep='\t', header=None, index=False)