import pandas as pd

data = {
    'cars': [5, 4, 1, 7], #series
    'boats': [2, 6, 0, 2] #series
}

vehicles = pd.DataFrame(data, index=['Peter', 'Sara', 'Ali', 'John'])

print(vehicles.info())
print()
print(vehicles.loc['Ali'])
print()
print(vehicles.head())