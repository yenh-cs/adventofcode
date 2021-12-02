import pandas as pd
import numpy as np

data = pd.read_csv('input.txt', sep=' ', header=None)
position = { 'horizontal': 0, 'depth': 0}
aim = 0

for index, row in data.iterrows():
    if row[0] == 'forward':
        position['horizontal'] += row[1]
        position['depth'] += aim*row[1]
    elif row[0] == 'down':
        aim += row[1]
    elif row[0] == 'up':
        aim -= row[1]

print(position['horizontal'] * position['depth'])
