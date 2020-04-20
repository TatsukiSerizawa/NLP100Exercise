 #coding: utf-8
import pandas as pd

df = pd.read_table('data/popular-names.txt', header=None)

print(len(df))