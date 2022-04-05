import pandas as pd

data = pd.read_csv('data.csv')

# read row line by line
for d in data.values:
  # read column by index
  print(d[2])