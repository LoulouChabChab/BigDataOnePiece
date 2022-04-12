import csv

import pandas as pd

metadata = pd.read_csv('overview.csv', low_memory=False)
data = []

for i in range(metadata.shape[0]):
    line = (metadata['Personnage'].iloc[i] + ' ' + metadata['Couleur 1'].iloc[i] + ' ' + metadata['Couleur 2'].iloc[
        i] + ' ' + metadata['Sexe'].iloc[i] + ' ' + metadata['Faction'].iloc[i] + ' ' + metadata['Fruits'].iloc[i])
    if line is not None:
        data.append(line)
df = pd.DataFrame(data)
df.to_csv('test_overview.csv')
