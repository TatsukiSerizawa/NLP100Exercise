import pandas as pd
import sys

df = pd.read_table('data/popular-names.txt', header=None)

if len(sys.argv) < 2:
    print("Please input a number")
    sys.exit()
else:
    N = int(sys.argv[1])
    print(df.head(N))