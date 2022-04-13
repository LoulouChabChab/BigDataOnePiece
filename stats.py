# Import Pandas
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plot

# Load Movies Metadata
from sklearn.metrics.pairwise import linear_kernel

metadata = pd.read_csv('data_latest.csv', low_memory=False)

groupByFaction = metadata["Faction"].value_counts()
print(groupByFaction)
groupByFaction.plot(kind='bar', title='Group by faction', ylabel='Count',
                 xlabel='Faction')
plot.show()
print("-----------------------------------")

top5Colors1 = metadata['Couleur 1'].value_counts()
top5Colors1 = top5Colors1.nlargest(n=5)
top5Colors1.plot(kind='bar', title='Top 5 Colors1', ylabel='Count',
                 xlabel='Color')
plot.show()

print("-----------------------------------")

top10Colors1 = metadata['Couleur 1'].value_counts()
print(top10Colors1.nlargest(n=10))
print("-----------------------------------")

top10Colors2 = metadata['Couleur 2'].value_counts()
print(top10Colors2.nlargest(n=10))
print("-----------------------------------")

UnionTop10Colors = pd.concat([top10Colors1, top10Colors2]).drop_duplicates()
UnionTop10Colors = UnionTop10Colors.nlargest(n=10)
print(UnionTop10Colors)
UnionTop10Colors.plot(kind='bar', title='Top 10 Colors', ylabel='Count',xlabel='Color')
plot.show()
print("-----------------------------------")

groupByFruits = metadata["Fruits démon"].value_counts()
print(groupByFruits)
groupByFruits.plot(kind='bar', title='Group by Fruit', ylabel='Count',
                 xlabel='Fruits')
plot.show()


